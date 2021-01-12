from numpy import core
from bowlib2 import *

dimensions = Dimensions(
    brace_height=0.196,
    draw_length=0.7,
    handle_angle=-0.36,
    handle_length=0.527,
    handle_setback=0.02
)

profile = [ # Curvature [m, 1/m]
    [0.00, 0.0],
    [0.17, 0.0],
    [0.25, 2.0],
    [0.36, 3.5],
    [0.43, 8.0],
    [0.50, 9.0],
    [0.56, 15.0]
]

width = [ # Limb width [%, m]
    [0.00, 0.038],   # parallel
    [0.40, 0.038],
    [0.45, 0.0365],  # start of limb taper
    [1.00, 0.012]
]

coreHeight = [ # Limb height [%, m]
    [0.00, 0.01],    # <- stiff (constant)
    [0.30, 0.0043],
    [0.32, 0.0041],  # <- start taper
                     # optimize taper for bending
    [0.84, 0.00172], # <- end taper
    [0.86, 0.0016],  # <- constant
    [1.00, 0.0016]
]

layers =  [
    Layer.initFromMaterial(material.cfk, 0.0005),
    Layer.initFromMaterial(material.core, coreHeight),
    Layer.initFromMaterial(material.glass, 0.001),
]

bow = Bow(
    width = width,
    layers = layers,
    profile = profile,
    dimensions = dimensions,

    masses = masses.arrow20limb10,
    string = string.fastFlight12,
    damping = damping.damping12,
    settings = settings.recurve,
)

symRes = symutil.runSimulation(bow)
print('CurvatureError: {}'.format(symRes.calculateCurvatureError(coreHeight[2][0], coreHeight[3][0])))
print('CurvatureError: {:0.3f}'.format(symRes.calculateCurvatureError(0, 1)))

print("Arrow vel.: {:0.2f}".format(bow.cachedSymRes.dynamics.final_vel_arrow))


with open("./tmp/aRecurveBow.bow", "w") as file:
    file.write(bow.asJson())

