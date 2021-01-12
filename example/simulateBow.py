# Python drives me mad. Couldn't find a better way to import bowlib2
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

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