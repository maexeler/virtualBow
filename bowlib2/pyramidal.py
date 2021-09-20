from typing import Tuple

from bowlib2 import symutil
from bowlib2.conversations import *
from bowlib2.bow import Bow, Layer, Masses, String, Damping, Settings, Dimensions

"""
Create a pyramidal bow

bowParam is a list [
    bowLength, handleLength, "braceHeight", curvature,
    drawLengthMeter, drawForceNewton
]
Example: [1.7, 0.5, 0.16, 1.3, i2m(23), p2n(50)]

bowProperties is a list [
    [topMaterial, coreMaterial, bottomMaterial],
    masses, string, damping, settings
]
Example: [
    [material.glass, material.ash, material.glass],
    masses.arrow30, string.fastFlight12, damping.damping12, settings.pyramid
]
"""
def createPyramidalBow(bowParam, bowProperties, startWidth=0.038, endWidth=0.015) -> Bow:
    return PyramidalBow(
        bowLength=bowParam[0],
        handleLength=bowParam[1],
        braceHeight=bowParam[2],
        drawLength=bowParam[4],
        startWidth=startWidth,
        endWidth=endWidth,
        curvature=bowParam[3],

        topLayer=Layer.initFromMaterial(bowProperties[0][0], 0.001),
        coreLayer=Layer.initFromMaterial(bowProperties[0][1], 0.007),
        bottomLayer=Layer.initFromMaterial(bowProperties[0][2], 0.001),
        masses=bowProperties[1],
        string=bowProperties[2],
        damping=bowProperties[3],
        settings=bowProperties[4]
    )

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

    def optimize(self, drawWeight: float, curvature: float = 0.0):
        self.curvature = curvature
        self.optimizeForDrawForce(drawWeight) # 50pd
        self.optimizeForCurvature((0.40, 0.50), 0.005, drawWeight)
        self.optimizeForDrawForce(drawWeight) # 50pd

    def summary(self, imperial: bool = False) -> str:
        if not self._symRes or self._symRes.dynamics.final_vel_arrow == 0.0:
            symutil.runSimulation(self)
        final_draw_force = self._symRes.statics._final_draw_force
        final_vel_arrow = self._symRes.dynamics.final_vel_arrow
        draw_length = self.dimensions.draw_length
        if imperial:
            final_draw_force /= 4.448
            final_vel_arrow *= 3.281
            draw_length *= 39.37
            return 'arrow velocity: {:0.1f} fps, ({:0.1f} lbs @ {:0.1f}")'.format(final_vel_arrow, final_draw_force, draw_length)
        else:
            return 'arrow velocity: {:0.3f} m/s, ({:0.3f} N @ {:0.3f} m)'.format(final_vel_arrow, final_draw_force, draw_length)

    @property
    def coreLayerHight(self) -> float:
        return self.coreLayer.height[0][1]

    @coreLayerHight.setter
    def coreLayerHight(self, v: float):
        self.coreLayer.height[0][1] = v
        self.coreLayer.height[1][1] = v

    def calculateDrawForce(self) -> float:
        return symutil.runSimulation(self, dynamic=False).statics._final_draw_force

    def adjustForDrawForce(self, drawForce: float)-> float:
        actForce = self._symRes.statics._final_draw_force
        actHeight = self.coreLayerHight
        optHeight = actHeight * ((drawForce/actForce)**(1/3))
        self.coreLayerHight = optHeight
        return self.coreLayerHight

    def optimizeForDrawForce(self, drawForce: float)-> float:
        self.calculateDrawForce()
        return self.adjustForDrawForce(drawForce)

    def calculateCurvatureError(self) -> float:
        return symutil.runSimulation(self, dynamic=True).calculateCurvatureError(0, self.taperedLimbPercent)

    def calculateCurvatureErrorForTaperedLimbLength(self, taperedLimbLength: float, drawForce: float) -> float:
        """
        This function is used by openmdao
        She alters the bow (its taperedLimbLength) and calculates the new curvature error.
        Afterwards, the draw force is adjusted.
        She then retuns the actual curvature error
        """
        self.taperedLimbLength = taperedLimbLength
        res = self.calculateCurvatureError()
        self.adjustForDrawForce(drawForce)
        return res

    def optimizeForCurvature(self, range: Tuple[float, float], stepp: float = 0.005, drawForce: float = None, ) -> float:
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
            if drawForce:
                self.adjustForDrawForce(drawForce)
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
        if v > self.limbLength:
            v = self.limbLength
        taperedLengthPercent = v / self.limbLength
        if (taperedLengthPercent > 0.95):
            taperedLengthPercent = 0.95
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
        angle = ''
        if self.dimensions.handle_angle != 0.0:
            angle = '({:0.1f})-'.format(r2d(self.dimensions.handle_angle))
        bowName = 'pb({:0.2f}-{:0.2f}-{:}({:0.3f}-{:0.3f})-{:0.2f})[{:0.2f}-{:0.2f}])-{:0.3f}'.format(
            self.bowLength, self.handleLength, angle,
            self.startWidth, self.endWidth,
            self.curvature,
            self.dimensions.brace_height, self.dimensions.draw_length,
            self.taperedLimbLength,)
        bowSym = ""
        if self.cachedSymRes:
            bowSym = " ({:0.2f}@{:0.2f}) {:0.2f}mps".format(
                self.cachedSymRes.statics.final_draw_force,
                self.dimensions.draw_length,
                self.cachedSymRes.dynamics.final_vel_arrow)
        return "{}{}".format(bowName, bowSym)
