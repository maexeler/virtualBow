# Python drives me mad. Couldn't find a better way to import bowlib2
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from bowlib2 import bow, symutil

# read in the bow from file
aBow: bow.Bow = symutil.loadBowFromFile('./example/bows/bowFromGui.bow')

# Modify it
aBow.comment = 'Modifyed bow'

# and write it back
symutil.saveBowToFile(aBow, './example/bows/bowFromBowLib.bow')
