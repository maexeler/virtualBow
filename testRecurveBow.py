from numpy import core
from bowlib2 import *

dimensions = Dimensions(
    brace_height=0.25,
    draw_length=0.712,
    handle_angle=-0.36,
    handle_length=0.527,
    handle_setback=0.0
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
    [0.40, 0.038],   # start of limb taper
    [0.85, 0.023],  
    [1.00, 0.012]
]

layers =  [
    Layer.initFromMaterial(material.cfk, 0.0005),
    Layer.initFromMaterial(material.core, []), # empty array is OK
    Layer.initFromMaterial(material.glass, 0.001),
]

bow = recurve.RecurveBow(
    p2 = 0.30, p5 = 0.85,
    t0 = 0.0100, t2 = 0.0045, t5 = 0.0016,
    
    width = width,
    layers = layers,
    profile = profile,
    dimensions = dimensions,

    masses = masses.arrow20limb10,
    string = string.fastFlight12,
    damping = damping.damping12,
    settings = settings.recurve,
)

symutil.saveBowToFile(bow, './tmp/@RecurveBow0.bow')
print(bow.layers[1]._height)

# Optimize bow and write it to file
bow.setDrawForce(155.7)
symutil.saveBowToFile(bow, './tmp/@RecurveBow1.bow')

print(bow.layers[1]._height)
