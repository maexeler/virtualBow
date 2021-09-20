def fps2mps(fps: float) -> float:
    return fps/3.281

def mps2fps(mps: float) -> float:
    return mps * 3.281

def pound2newton(pound: float) -> float:
    return pound * 4.4482216

def newton2pound(newton: float) -> float:
    return newton / 4.4482216

p2n = pound2newton
n2p = newton2pound

def inch2meter(inch: float) -> float:
    return inch / 39.37

def meter2inch(meter: float) -> float:
    return meter * 39.37

i2m = inch2meter
m2i = meter2inch

def degree2radiant(degree: float) -> float:
    return degree * 3.14 / 180

def radiant2degree(radiant: float) -> float:
    return radiant / 3.14 * 180

d2r = degree2radiant
r2d = radiant2degree
