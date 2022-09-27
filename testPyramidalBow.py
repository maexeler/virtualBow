from bowlib2.pyramidal import PyramidalBow
from bowlib2 import Bow, Layer, material, masses, string, damping, settings, pyramidal, symutil

def createPyramidalBow(bowParam) -> Bow:
    bowProperties = [
        [material.glass, material.ash, material.glass],
        masses.arrow30, string.fastFlight12, damping.damping12, settings.pyramid
    ]
    return pyramidal.createPyramidalBow(bowParam=bowParam, bowProperties=bowProperties)


def optimizePyramidalBow(bow: PyramidalBow, drawForce):
    bow.optimizeForDrawForce(drawForce)
    bow.optimizeForCurvature(
        (0.5 * bow.limbLength, 0.8 * bow.limbLength), 0.005, drawForce=drawForce)
    return bow

def optimizePyramidalBows(bowParams):
    result = []
    for bowParam in bowParams:
        try:
            bow = createPyramidalBow(bowParam)
            result.append(optimizePyramidalBow(bow, 4.448*bowParam[5]))
        except:
            print("Failed: " + str(bow))
    return result

test = bowParams23to32_35pd = [
    # [1.70, 0.50, 0.14, 1.3, 31, 40],
    # [1.70, 0.50, 0.14, 1.3, 32, 40],
    # [1.70, 0.50, 0.16, 1.3, 0.58, 50],
    [1.65, 0.50, 0.16, 1.3, 0.58, 50],
    [1.60, 0.50, 0.16, 1.3, 0.58, 50]
]

# simRes = optimizePyramidalBows(test)
# for bow in simRes:
#     print(bow)
#     symutil.saveBowToFile(bow, "./tmp/opt/{}.bow".format(bow))


def calcProductionBow(bowParam):
    bow = createPyramidalBow(bowParam)
    bow.taperedLimbLength = 0.4
    drawForce = bowParam[5]*4.44
    bow.optimizeForDrawForce(drawForce)
    bow.optimizeForDrawForce(drawForce)
    bow.optimizeForDrawForce(drawForce)
    bow.optimizeForDrawForce(drawForce)
    bow.optimizeForDrawForce(drawForce)
    symutil.runSimulation(bow, dynamic=True)
    print(bow)
    print(bow.layers[1].height)
    symutil.saveBowToFile(bow, "./tmp/prod/{}.bow".format(bow))

bowParam = [1.60, 0.50, 0.16, 1.3, 0.58, 50]
calcProductionBow(bowParam)
bowParam = [1.65, 0.50, 0.16, 1.3, 0.58, 50]
calcProductionBow(bowParam)
bowParam = [1.70, 0.50, 0.16, 1.3, 0.58, 50]
calcProductionBow(bowParam)
bowParam = [1.60, 0.50, 0.16, 1.3, 0.58, 45]
calcProductionBow(bowParam)
bowParam = [1.60, 0.50, 0.16, 1.3, 0.58, 40]
calcProductionBow(bowParam)

