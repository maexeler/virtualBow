
# VirtualBow
## Bow & Arrow Physics Simulation support code  

There exists a program for simulation of (archery) bows at https://www.virtualbow.org/  
You shold first read this site and download the provided code.

## What is it?
bowlib2 contains support code for the creation of *bow files and the evaluation of *.res files.
Read the VirtualBow [user manual](https://www.virtualbow.org/files/user_manual.pdf) for further explanations.  

bowlib2 contains mapping structures for the bow and result files as well as support for reading and writing them.

## Python
Since I had not written Python code for a long long time, my code may not be as pythonesque as it could be.  
In hindsight, I should not have used Python because I am more a kind of a 'strict typed' guy. I tryed to augment the code with type information but watch out, Python does not really respect it, but it really helps in the editor.

# How to use bowlib2

## Start with a *.bow file
You can create a bow in the VirtualBow application and save it.  
Then you can build a bow from this file, modify the bow an write it back.

### [readAndModifyBow.py](./example/readAndModifyBow.py)

```python
from bowlib2 import bow, symutil

# read in the bow from file
aBow: bow.Bow = symutil.loadBowFromFile('./example/bows/bowFromGui.bow')

# Modify it
aBow.comment = 'Modifyed bow'

# and write it back
symutil.saveBowToFile(aBow, './example/bows/bowFromBowLib.bow')
```

## Build a bow from scratch
bowlib2 contains everything you need to build a bow from scratch.

### [buildFromScratch.py](./example/buildFromScratch.py)

```python
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
```
Notice that the material package contains some predefined materials and that we could have used to build our layers as following:

```python
layers = [
    Layer.initFromMaterial(material.glass, 0.001),
    Layer.initFromMaterial(material.ash, 0.006),
    Layer.initFromMaterial(material.glass, 0.001),
]
```
# Simulating a bow
The simulation of a bow is easy.  
Load or create an bow and use ```symutil.runSimulation(...)``` to simulate it.
### [simulateBow.py](./example/simulateBow.py)
```python
from bowlib2 import Bow, symutil
from bowlib2.symRes import SymRes

# read in the bow from file
aBow: Bow = symutil.loadBowFromFile('./example/bows/bowFromGui.bow')

# simulate it
res: SymRes = symutil.runSimulation(aBow)

# Print arrow velocity
print('Arrow velocity {:0.3f} m/s ({:0.3f} fps)'.format(
    res.dynamics.final_vel_arrow,
    3.281 * res.dynamics.final_vel_arrow))
```