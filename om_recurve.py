
# import numpy
import openmdao.api as om
from bowlib2 import *
from bowlib2.recurve import RecurveBow


def makeBow() -> RecurveBow:

    return RecurveBow(
            p2 = 0.25, p5 = 0.65,
            t0 = 0.0100, t2 = 0.0037, t5 = 0.0016,
            
            width = 
            [ # Limb width [%, m]
                [0.00, 0.038],   # parallel
                [0.40, 0.038],   # start of limb taper
                [0.85, 0.023],  
                [1.00, 0.012]
            ],
            layers = 
            [   Layer.initFromMaterial(material.cfk, 0.0005),
                Layer.initFromMaterial(material.core, []), # empty array is OK
                Layer.initFromMaterial(material.glass, 0.001),
            ],

            profile = 
            [ # Curvature [m, 1/m]
                [0.00, 0.0],
                [0.17, 0.0],
                [0.25, 2.0],
                [0.36, 3.5],
                [0.43, 8.0],
                [0.50, 9.0],
                [0.56, 15.0]
            ],

            dimensions = Dimensions
            (   brace_height=0.25,
                draw_length=0.712,
                handle_angle=-0.36,
                handle_length=0.527,
                handle_setback=0.0
            ),

            masses = masses.arrow20limb10,
            string = string.fastFlight12,
            damping = damping.damping12,
            settings = settings.recurve,
        )


class omRecurve(om.ExplicitComponent):

    def getOptimizedBow(self) -> RecurveBow:
        return self.bow


    def setup(self):
        # define inputs
        self.add_input('x',val=0.0)
        self.add_input('y',val=0.0)
        self.add_input('drawForce', val=155.7)

        # define outputs
        self.add_output('f_xy', val=0.0)

        # Bogen definirern
        self.bow: RecurveBow = makeBow()

        # Zugewicht an Vorgabe anpassen
        self.bow.setDrawForce(155.7)

       
        
    # define partials
    def setup_partials(self):
        # Finite difference all partials
        self.declare_partials(of='*', wrt='*', method='fd')
    

    def compute(self, inputs, outputs):

        # p2 = inputs['x'] # p2
        # p5 = inputs['y'] # p5
        # drawForce = inputs['drawForce']

        """
        Achtung, die Eingabewerte werden als Arrays übermittelt und wir wollen nur den ersten Wert,
        also müssen wir den ersten Wert aus dem Array auslesen mit
        inputs['paramName'][0]
        """
        p2 = inputs['x'][0] # p2
        p5 = inputs['y'][0] # p5
        drawForce = inputs['drawForce'][0]

        print('p2: ', p2) # Fortschrittsanzeige  
        
        # f_xy = self.bow.calculateArrowspeedforOM(p2,p5,drawForce)
        # (final_draw_force / final_vel_arrow *100)

        outputs['f_xy'] = self.bow.calculateArrowspeedforOM(p2,p5,drawForce)
        



if __name__ == "__main__":

    # build the model
    prob = om.Problem()
    # Unser Model als 'omrec' in der Optimierung installieren
    # und ankündigen, dass wir 'x', 'y' und 'drawForce' als Parameter brauchen

    prob.model.add_subsystem('omrec', omRecurve(), promotes_inputs=['x', 'y', 'drawForce'])
    

    prob.model.set_input_defaults('x', 0.25)
    prob.model.set_input_defaults('y', 0.65)
    prob.model.set_input_defaults('drawForce', 155.7)

    # setup the optimization "COBYLA SLSQP"
    prob.driver = om.ScipyOptimizeDriver()
    prob.driver.options['optimizer'] = 'COBYLA'
    prob.driver.options['tol'] = 1e-4
    # prob.driver.options['disp'] = True

    prob.model.add_design_var('x', lower=0.2, upper=0.49)
    prob.model.add_design_var('y', lower=0.51, upper=0.99)
       
    prob.model.add_objective('omrec.f_xy')

    prob.setup()

    prob.run_model()
    # prob.run_driver()

    