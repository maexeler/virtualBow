from bowlib2 import *

def symPyramidalForCurvature():
    settings.pyramid.n_limb_elements = 20

    bow = pyramidal.PyramidalBow(
        bowLength=1.70,
        handleLength=0.5,
        braceHeight=0.16,
        drawLength=0.58,
        startWidth=0.038,
        # startWidth=0.050,
        endWidth=0.015,
        curvature=1.0, # optimize for that

        topLayer=Layer.initFromMaterial(material.glass, 0.001),
        coreLayer=Layer.initFromMaterial(material.ash, 0.0067),
        bottomLayer=Layer.initFromMaterial(material.glass, 0.001),
        masses=masses.arrow30,
        string=string.fastFlight12,
        damping=damping.damping12,
        settings=settings.pyramid
    )

    bow.optimizeForDrawForce(222.4) # 50pd
    bow.optimizeForCurvature((0.40, 0.55), 0.005)
    bow.optimizeForDrawForce(222.4) # 50pd

    curvaturResults = []
    for curvature in range(1, 26):
        try:
            bow.curvature = curvature/10
            bow.optimizeForDrawForce(222.4) # 50pd

            # print(bow)

            symutil.saveBowToFile(bow, "./tmp/{}.bow".format(bow))
            symres: symRes.SymRes = symutil.runSimulation(bow)

            curvaturResults.append([
                str(bow), 
                symres.statics._final_draw_force, 
                symres.dynamics.final_vel_arrow, 
                symres.calculateCurvatureError(0, bow.taperedLimbPercent)])
        except:
            pass
    return curvaturResults

def saveCurvatureResults(curvaturResults):
    import pickle
    pickle.dump( curvaturResults, open("curvaturResults.p", "wb"))

def loadCurvatureResults():
    import pickle
    return pickle.load(open("curvaturResults.p", "rb"))

def printResults(curvaturResults):
    for result in curvaturResults:
        print(result[0] + " Df: {:0.3f}({:0.2f}) Av: {:0.3f}({:0.2f}) Av/Df: {:0.3f} Cerr: {:0.2f}".format(
            result[1], result[1] / 4.448,
            result[2], result[2] * 3.281,
            result[2] / result[1],
            result[3])
        )

res = symPyramidalForCurvature()
saveCurvatureResults(res)

res = loadCurvatureResults()
printResults(res)
