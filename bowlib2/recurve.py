from bowlib2.symRes import SymRes
from typing import List
from bowlib2 import symutil
from bowlib2.bow import Bow, Layer, Masses, String, Damping, Settings, Dimensions

class RecurveBow(Bow):

    def __init__(self,
         t0: float,    
         t2: float,  p2: float,
         t5: float,  p5: float,           
         damping: Damping, 
         dimensions: Dimensions, 
         layers: List[Layer], 

         masses: Masses, 
         profile: list, 
         settings: Settings, 
         string: String, 
         width: list, 
         comment: str = '', 
         version: str = "0.7.1"
        ):

        super().__init__(
            comment = comment,
            damping = damping,
            dimensions = dimensions,
            layers = layers,
            masses = masses,
            profile = profile,
            settings = settings,
            string = string,
            version = version,
            width = width
        )
        self.initCoreLayer(t0, t2, t5, p2, p5)
    
    def initCoreLayer(self, t0, t2, t5, p2, p5):
        self.layers[1]._height = [[0.0, 0.0] for e in range(7)]
        self.setT(0, t0)
        self.setT(2, t2)
        self.setT(5, t5)

        self.setP(0, 0.0)
        self.setP(2, p2)
        self.setP(5, p5)

        self.calccoreHight()

    def calccoreHight(self):
        t0 = self.getT(0)
        t2 = self.getT(2)
        t5 = self.getT(5)
        self.setT(1, t2  + 0.125 * (t0 - t2))
        self.setT(3, t2  - 0.125 * (t2 - t5))
        self.setT(4, t5  + 0.125 * (t2 - t5))
        self.setT(6, t5)
        
        p2 = self.getP(2)
        p5 = self.getP(5)
        self.setP(1, p2 - 0.125 * p2)
        self.setP(3, p2 + 0.125 * (p5-p2))
        self.setP(4, p5 - 0.125 * (p5-p2))
        self.setP(6, 1.0)
    
    def setDrawForce(self, desiredForce: float):
        actForce = symutil.runSimulation(self, False).statics._final_draw_force
        t2_old = self.getT(2)
        t5_old = self.getT(5)
        t2 = t2_old * ((desiredForce/actForce)**(1/1.4))
        t5 = t5_old * ((desiredForce/actForce)**(1/1.4))
        self.setT(2, t2)
        self.setT(5, t5)
        self.calccoreHight()
    
    def calculateArrowspeedforOM(self, p2: float, p5: float, drawForce: float) -> float:
        """
        This function is used by openmdao
        """
        self.setP(2, p2)
        self.setP(5, p5)
        self.setDrawForce(drawForce)
        symutil.runSimulation(self)
        final_draw_force = self._symRes.statics._final_draw_force
        final_vel_arrow = self._symRes.dynamics.final_vel_arrow
        res = final_draw_force / final_vel_arrow *10
        
        return res


    def getT(self, index: int) -> float:
        coreHeight = self.layers[1]._height
        return coreHeight[index][1]

    def setT(self, index: int, value: float):
        coreHeight = self.layers[1]._height
        coreHeight[index][1] = value

    def getP(self, index: int) -> float:
        coreHeight = self.layers[1]._height
        return coreHeight[index][0]

    def setP(self, index: int, value: float):
        coreHeight = self.layers[1]._height
        coreHeight[index][0] = value

    
