import os
import msgpack
import subprocess
from .bow import Bow
from .symRes import SymRes

def saveBowToFile(bow: Bow, fileName: str) :
    pos = fileName.rfind('/')
    path = fileName[:pos]
    if not os.path.exists(path): os.makedirs(path)
    
    with open(fileName, "w") as file:
        file.write(bow.asJson())

def loadBowFromFile(fileName: str) -> Bow:
    with open(fileName, "r") as file:
        return Bow.fromJson(file.read())

def loadSymFromFile(fileName: str) -> SymRes:
    with open(fileName, "rb") as file:
        return SymRes.initFromDict(msgpack.unpack(file, raw=False))

def runSimulation(bow: Bow, dynamic: bool = True, symName: str = None) -> SymRes:
    path = "./tmp"
    if not os.path.exists(path): os.makedirs(path)
    
    bowName = symName if symName else "tmp"
    bowName = path + "/" + bowName
    symName = bowName + ".res"
    bowName += ".bow"
    guard = 5 # Maximal number of retries
    while guard > 0:
        guard -= 1
        saveBowToFile(bow, bowName)
        subprocess.call([
            "virtualbow-slv",
                "--dynamic" if dynamic else "--static",
                bowName, symName])
        try:
            symRes = loadSymFromFile(symName)
            bow.cachedSymRes = symRes
            return symRes
        except:
            # Assuming that the solver can't solve for the bow,
            # try to change a symulation parameter to help him
            bow.settings.n_limb_elements += 1

def runVirtualBowGui(bowFileName: str):
    """ Not usable, subprocess.call() blocks.\n
    Anyone any idee how to solve that?"""
    subprocess.call([ "virtualbow-gui", bowFileName])
