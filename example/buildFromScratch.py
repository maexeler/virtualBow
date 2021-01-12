# Python drives me mad. Couldn't find a better way to import bowlib2
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from bowlib2 import *

damping = Damping(
    damping_ratio_limbs=0.1,
    damping_ratio_string=0.0)

dimensions = Dimensions(
    brace_height=0.16,
    draw_length=0.58,
    handle_angle=0.0,
    handle_length=0.5,
    handle_setback=0.0
)
masses = Masses(
    arrow=0.03,
    limb_tip=0.0, string_center=0.0, string_tip=0.0
)

settings = Settings(
    n_draw_steps = 150,
    n_limb_elements = 20,
    n_string_elements = 25,
    sampling_rate = 10000.0,
    time_span_factor = 1.5,
    time_step_factor = 0.2
)

string = String(
    n_strands = 12,
    strand_density = 0.0005,
    strand_stiffness = 3500.0
)

ash = Layer(name='Esche', E=12000000000.0, rho=720.0, height=[[0.0, 0.006], [1.0, 0.006]])
glass = Layer(name='Glas', E=41000000000.0, rho=1920.0, height=[[0.0, 0.001], [1.0, 0.001]])

profile = [[0.0, 1.0], [0.35, 1.0], [0.6, 0.0]]
width =   [[0.0, 0.038], [0.58, 0.015], [1.0, 0.015]]
layers =  [glass, ash, glass]

bow = Bow(
    profile=profile,
    width=width,
    layers=layers,
    damping=damping,
    dimensions=dimensions,
    masses=masses,
    settings=settings,
    string=string,
)

symutil.saveBowToFile(bow, "./example/bows/bowBuildFroScratch.bow")