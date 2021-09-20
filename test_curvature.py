from bowlib2 import *
from bowlib2.conversations import *

filename = './om-opt/testcurvature.bow'

"""
limbSimulationSteps = 32
pyramidalProfileSteps = 8

limbLength = 0.550 / 0.600
pyramidalLength = 0.400
"""
limbSimulationSteps = 32
pyramidalProfileSteps = 8

def prepareForOptimisation(
    bow: Bow,
    curvature: float = 1.3,
    pyramidalLength: float = 0.4,
    limpLength: float = 0.550
) -> Bow:
    # set simulation steps
    bow.settings.n_limb_elements = limbSimulationSteps
    # create profile
    pyramidalPartLength = pyramidalLength / pyramidalProfileSteps
    profile = [[i*pyramidalPartLength, curvature] for i in range(pyramidalProfileSteps+1)]
    profile.append([limpLength, 0.0])
    bow.profile = profile
    return bow

def updatedCurvature(
        bow: Bow,
    ) -> List[float]:
    symRes: SymRes = symutil.runSimulation(bow, dynamic=False)
    kappa = symRes.statics.states.kappa[-1]
    curvatures = [[kappa[i], kappa[i+1], kappa[i+2]] for i in range(pyramidalProfileSteps)]
    curvaturesMean = [sum(curvature)/len(curvature) for curvature in curvatures]
    curvatureMean = sum(curvaturesMean)/len(curvaturesMean)
    curvaturesFactors = [c/curvatureMean for c in curvaturesMean]
    for i in range(len(curvaturesFactors)):
        bow.profile[i][1] /= curvaturesFactors[i]
    bow.profile[len(curvaturesFactors)][1] = bow.profile[len(curvaturesFactors)-1][1]
    return bow

def optimizeDrawForce(bow: Bow, pounds: float = 50) -> Bow:
    symRes = symutil.runSimulation(bowUnderTest, True)
    for i in range(4):
        adjustForDrawForce(bowUnderTest, symRes, p2n(pounds))
        symRes = symutil.runSimulation(bowUnderTest, True)
    return bow

def adjustForDrawForce(bow: Bow, symRes: SymRes, drawForce: float)-> float:
        actForce = symRes.statics._final_draw_force
        actHeight = bow.layers[1].height[0][1]
        optHeight = actHeight * ((drawForce/actForce)**(1/3))
        bow.layers[1].height[0][1] = optHeight
        bow.layers[1].height[1][1] = optHeight
        return optHeight

if __name__ == "__main__":
    drawWight = 50
    for iterations in [0, 1, 5, 10, 20]:
        bowUnderTest: Bow = prepareForOptimisation(symutil.loadBowFromFile(filename))
        bowUnderTest = optimizeDrawForce(bowUnderTest, drawWight)
        for i in range(iterations):
            bowUnderTest = updatedCurvature(bowUnderTest)
        bowUnderTest = optimizeDrawForce(bowUnderTest, drawWight)
        symRes: SymRes = symutil.runSimulation(bowUnderTest, True)
        print('it: {}, dw: {}, av: {}'.format(
            iterations, symRes.statics._final_draw_force, symRes.dynamics.final_vel_arrow
        ))
        symutil.saveBowToFile(bowUnderTest, './om-opt/curved-{}-iteration.bow'.format(iterations))
