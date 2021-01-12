from typing import Tuple

from bowlib2 import symutil
from bowlib2.bow import Bow, Layer, Masses, String, Damping, Settings, Dimensions

class PyramidalBow(Bow):

    def __init__(self, 
        bowLength: float,
        handleLength: float,
        braceHeight: float,
        drawLength: float,
        endWidth: float,
        startWidth: float,
        topLayer: Layer,
        coreLayer: Layer,
        bottomLayer: Layer,

        masses: Masses,
        string: String,
        damping: Damping,
        settings: Settings,

        curvature: float = 0.0,
        taperedLimbLength: float = None):
        super().__init__(
            damping = damping,
            dimensions = Dimensions(
                handle_length=handleLength,
                brace_height=braceHeight,
                draw_length=drawLength,
                handle_angle=0,
                handle_setback=0
            ),
            layers = [topLayer, coreLayer, bottomLayer],
            masses = masses,
            profile = [[0.0, 0.0], [0.0, 0.0], [(bowLength-handleLength)/2.0, 0.0]],
            settings = settings,
            string = string,
            width = [[0.0,0.0],[0.0,0.0],[1.0,0.0]]
        )
        self._bowLength = bowLength
        self.endWidth = endWidth
        self.startWidth = startWidth
        self.curvature = curvature
        if taperedLimbLength:
            self.taperedLimbLength = taperedLimbLength
        else:
            self.taperedLimbPercent = 2.0/3.0
        self.coreLayer = coreLayer

    @property
    def coreLayerHight(self) -> float:
        return self.coreLayer.height[0][1]

    @coreLayerHight.setter
    def coreLayerHight(self, v: float):
        self.coreLayer.height[0][1] = v
        self.coreLayer.height[1][1] = v

    def calculateDrawForce(self) -> float:
        return symutil.runSimulation(self, False).statics._final_draw_force

    def optimizeForDrawForce(self, drawForce: float)-> float:
        actForce = self.calculateDrawForce()
        actHeight = self.coreLayerHight
        optHeight = actHeight * ((drawForce/actForce)**(1/3))
        self.coreLayerHight = optHeight
        return self.coreLayerHight

    def calculateCurvatureError(self) -> float:
        return symutil.runSimulation(self, True).calculateCurvatureError(0, self.taperedLimbPercent)

    def optimizeForCurvature(self, range: Tuple[float, float], stepp: float = 0.005) -> float:
        leftPos = range[0]
        rightPos = range[1]
        self.taperedLimbLength = leftPos
        leftError = self.calculateCurvatureError()
        self.taperedLimbLength = rightPos
        rightError = self.calculateCurvatureError()
        delta = rightPos-leftPos
        curvatureError = 0.0
        while delta > stepp:
            middlePos = leftPos+delta/2
            self.taperedLimbLength = middlePos
            curvatureError = self.calculateCurvatureError()
            dl = leftError-curvatureError
            dr = rightError-curvatureError
            if dl < dr:
                rightPos = middlePos
                rightError = curvatureError
            else:
                leftPos = middlePos
                leftError = curvatureError
            delta = rightPos-leftPos
        return curvatureError

    @property
    def bowLength(self) -> float: return self._bowLength

    @property
    def handleLength(self) -> float: return self.dimensions.handle_length
    
    @handleLength.setter
    def handleLength(self, v: float):  self.dimensions.handle_length = v

    @property
    def limbLength(self) -> float:
        return (self.bowLength - self.handleLength) / 2.0

    @property
    def taperedLimbLength(self) -> float:
        return self.profile[1][0]
    
    @property
    def taperedLimbPercent(self) -> float:
        return self.width[1][0]
    
    @taperedLimbLength.setter
    def taperedLimbLength(self, v: float):
        taperedLengthPercent = v / self.limbLength
        if (taperedLengthPercent > 0.95):
            raise Exception("taperedLimbLength to long!")
        self.width[1][0] = taperedLengthPercent
        self.profile[1][0] = v
    
    @taperedLimbPercent.setter
    def taperedLimbPercent(self, v: float):
        self.width[1][0] = v
        self.profile[1][0] = self.limbLength * v
    
    @property
    def curvature(self) -> float: return self.profile[0][1]
    
    @curvature.setter
    def curvature(self, v: float):
        self.profile[0][1] = v
        self.profile[1][1] = v

    @property
    def startWidth(self) -> float: return self.width[0][1]
    
    @startWidth.setter
    def startWidth(self, v: float): self.width[0][1] = v

    @property
    def endWidth(self) -> float:
        return self.width[1][1]
    
    @endWidth.setter
    def endWidth(self, v: float):
        self.width[1][1] = v
        self.width[2][1] = v

    def __str__(self):
        return 'pb({:0.2f}-{:0.2f}-{:0.3f})({:0.3f}-{:0.3f},{:0.2f})[{:0.2f}-{:0.2f}]'.format(
            self.bowLength, self.handleLength, self.taperedLimbLength,
            self.startWidth, self.endWidth, self.curvature,
            self.dimensions.brace_height, self.dimensions.draw_length)
