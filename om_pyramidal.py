import openmdao.api as om

from bowlib2 import *
from bowlib2.conversations import *
from bowlib2.pyramidal import PyramidalBow

"""
Hi Thomi,
als erstes musst du dir überlegen was du optimieren willst.

In meinem fall ist es die Länge des getaperten Bereiches des Bogens.
Dazu lege ich ein Intevall fest und nenne die dazugehörige Variable 'x'
Weiter will ich die Zugkraft konsztant halten. Diese Konstante nenne ich 'drawForce'

Meine Bogenklasse braucht als nächstes eine Optimierungsfunktion. ich habe sie
calculateCurvatureErrorForTaperedLimbLength(x, drawForce) genannt. Sie will bei
ihren aufruf die beiden Werte für x und drawForce. Als Resultat gibt sie einen Wert
zurück, den die Optimierung minimieren soll.
Du findest diese Funktion in 'pyramidal.bow'

Anschliessend kannst du die Optimierung aufsetzen.

Die Klasse OmPyramidal beschreibt den Optimierungsjob.
In __main__ werden die Variablen 'x' und 'drawForce' initialisiert
und der Wert für das x-Intervall festgelegt.

Anschliessend kannst Du die Optimierung laufen lassen.


*** Do it yourself ***

Wenn Du selber eien Optimierung schreibst überlegst du dir erst, wieviele Parameter du durchprobieren möchtest.
(Ich nehme an, einige deiner t und p werte).
Dann ergänzt du deine Klasse RecurveBow um eine passende Optimierungsfunktion.

In der neuen Klasse OMRecurveBow passt du setup() und compute() an,
analog dazu wie ich es gemacht habe.
in __main__() musst du die benötigten Variablen initialisieren und den Wertebereich der
Optimierungsvariablen festlegen, ebenfalls analog dazu wie ich es gemacht habe.
Dann kannst Du die Optimierung laufen lassen.

recurveBow.setDrawForce() kannst Du ggf. verbessern, indem du die Anpassung in deiner Optimierungsfunktion
vornimmst, so wie ich das gemacht habe. Du sparst Dir dann einen Simulationslauf.

Viel Spass, und wenn es nicht klappt, komme ich gerne mal wieder vorbei.
"""
bowForSimulation: PyramidalBow = None

def getBowForSimulation():
    return bowForSimulation
class OmPyramidal(om.ExplicitComponent):
    """
    Die Klasse OmPyramidal stellt eine bestimmte Art von Optimierung dar.
    In unseren Fall optimiert sie die Länge des getaperten Bereiches eines Pyramidalbogens.
    """

    def getOptimizedBow(self) -> PyramidalBow:
        """
        Wir brauchen den Zugriff auf den optimierten Bogen nach dem Optimierungslauf
        """
        return self.bow

    def setup(self):
        """
        Festlegen dass es die Variablen 'x' und 'drawForce' braucht als Eingabeparameter.
        Das Ergebnis eines Optimierungsdurchlauf ist in der Ausgabevariablen 'f_x' enthalten
        """
        self.add_input('x', val=0.0)
        self.add_input('drawForce', val=222.4)
        self.add_output('f_x', val=0.0)

        """
        Als nächstes brauchen wir einen Bogen
        """
        self.bow: PyramidalBow = getBowForSimulation()
        """
        und optimieren die Die Zugkraft einmal vor wir mit der eigentlichen Optimierung beginnen
        """
        self.bow.optimizeForDrawForce(222.4)

    def setup_partials(self):
        # Finite difference all partials.
        self.declare_partials('*', '*', method='fd')

    def compute(self, inputs, outputs):
        """
        Dies ist die eigentliche Optimierungsfunktion.
        Sie ruft die Optimierungsfunktion des Bogens auf und gibt den erhaltenen Wert zurück.
        """

        """
        Zuerst besorgen wir uns die Eingabewerte.
        Achtung, diese werden als Arrays übermittelt und wir wollen nur den ersten Wert
        """
        x = inputs['x'][0]
        drawForce = inputs['drawForce'][0]

        # print('tapered limb length:', x) # Fortschrittsanzeige

        """
        Aufruf der Optimierungsfunktion des Bogens und rückgabe des Fehlewertes an die Optimierung
        """
        outputs['f_x'] = self.bow.calculateCurvatureErrorForTaperedLimbLength(x, drawForce)


def optimizeBow(bow: PyramidalBow, drawForce) -> PyramidalBow:
    global bowForSimulation

    """
    Aufsetzen aller Simulationseigenschaften
    """
    lower = 0.4
    upper = 0.9
    bowForSimulation = bow

    # build the model
    prob = om.Problem()
    """
    Unser Model als 'pyramidal' in der Optimierung installieren
    und ankündigen, dass wir 'x' und 'drawForce' als Parameter brauchen
    """
    prob.model.add_subsystem('pyramidal', OmPyramidal(), promotes_inputs=['x', 'drawForce'])

    """
    'x' und 'drawForce' müssen initialisiert werden
    """
    prob.model.set_input_defaults('x', lower)
    prob.model.set_input_defaults('drawForce', drawForce)

    # setup the optimization
    prob.driver = om.ScipyOptimizeDriver()
    prob.driver.options['optimizer'] = 'COBYLA'
    prob.driver.options['tol'] = 1e-4

    """
    Anschliessend müssen wir den Bereich festlegen, in welchen 'x' variieren soll
    """
    prob.model.add_design_var('x', lower=lower, upper=upper)

    """
    Dann legen wir das Ziel fest.
    """
    prob.model.add_objective('pyramidal.f_x')

    # prepare and run the simulation
    prob.setup()
    prob.run_driver()

    return prob.model._get_subsystem('pyramidal').getOptimizedBow()

def createPyramidalBow(bowParam) -> Bow:
    bowProperties = [
        [material.glass, material.ash, material.glass],
        masses.arrow30, string.fastFlight12, damping.damping12, settings.pyramid
    ]
    return pyramidal.createPyramidalBow(bowParam=bowParam, bowProperties=bowProperties)

def createAshBow(bowParam, startWidth=0.038, endWidth=0.015) -> Bow:
    bowProperties = [
        [material.ash, material.ash, material.ash],
        masses.arrow30, string.fastFlight12, damping.damping12, settings.pyramid
    ]
    return pyramidal.createPyramidalBow(
        bowParam=bowParam, bowProperties=bowProperties,
        startWidth=startWidth, endWidth=endWidth)

def optimizePyramidalSpace():
    bowParam = [0, 0.50, 0.14, 1.3, 0, 0]
    for bowLenght in [170, 1.75]: # 1.60, 1.65,
        for drawLength in [23, 24, 25, 26, 27, 28, 29, 30, 31, 32]:
            for drawWeight in [35, 40, 45, 50]:
                bowParam[0] = bowLenght
                bowParam[4] = i2m(drawLength)
                bowParam[5] = p2n(drawWeight)
                try:
                    bow: PyramidalBow = optimizeBow(
                        createPyramidalBow(bowParam), bowParam[5])
                    print(bow)
                    symutil.saveBowToFile(bow, "./om-opt/br14/{}.bow".format(bow))
                except:
                    print("Fail:" + str(bowParam))

if __name__ == "__main__":
    # optimizePyramidalSpace()

    # bowParam = [1.70, 0.50, 0.16, 1.3, i2m(23), p2n(50)]
    # bow = optimizeBow(createPyramidalBow(bowParam), bowParam[5])

    # for angle in [0.0, -5, -7.5, -10]:
    #     bowParam = [1.50, 0.50, 0.16, 1.3, i2m(23), p2n(50)]
    #     bow = createPyramidalBow(bowParam)
    #     bow.dimensions.handle_angle = d2r(angle)
    #     bow = optimizeBow(bow, bowParam[5])
    #     print(bow)
    #     symutil.saveBowToFile(bow, "./om-opt/{}.bow".format(bow))

    # # Kinderbogen
    # bowParam = [1.30, 0.24, 0.16, 0.0, 0.48, p2n(16)]
    # bow = optimizeBow(createAshBow(bowParam, startWidth=0.038), bowParam[5])

    # print(bow)
    # symutil.saveBowToFile(bow, "./om-opt/{}.bow".format(bow))

    # bowParam = [1.65, 0.50, 0.16, 1.3, i2m(23), p2n(50)]
    # bow = createPyramidalBow(bowParam)
    # bow.dimensions.handle_angle = d2r(-10.0)
    # bow = optimizeBow(bow, bowParam[5])
    # print(bow)
    # symutil.saveBowToFile(bow, "./om-opt/{}.bow".format(bow))

    for bowLength in [1.6]:
        for handleAngle in [-7.5]:
            bowParam = [bowLength, 0.50, 0.16, 1.3, i2m(23), p2n(50)]
            bow = createPyramidalBow(bowParam)
            # bow = createAshBow(bowParam)
            bow.dimensions.handle_angle = d2r(handleAngle)
            bow = optimizeBow(bow, bowParam[5])
            print(bow)
            # symutil.saveBowToFile(bow, "./om-opt/{}.bow".format(bow))
            symutil.saveBowToFile(bow, "./om-opt/{}.bow".format("bowUnderTest"))

    testBow: Bow = symutil.loadBowFromFile("./om-opt/{}.bow".format("bowUnderTest"))
    
 