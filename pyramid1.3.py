from bowlib2 import *

def makeBow(bowLength: float, bowWidth: float, drawLength: float) -> pyramidal.PyramidalBow:
    return pyramidal.PyramidalBow(
        bowLength=bowLength,
        handleLength=0.5,
        braceHeight=0.16,
        drawLength=drawLength,
        startWidth=bowWidth,
        endWidth=0.015,
        curvature=1.3,

        topLayer=Layer.initFromMaterial(material.glass, 0.001),
        coreLayer=Layer.initFromMaterial(material.bamboo, 0.0067),
        bottomLayer=Layer.initFromMaterial(material.glass, 0.001),
        masses=masses.arrow30,
        string=string.fastFlight12,
        damping=damping.damping12,
        settings=settings.pyramid
    )

def symBows(drawLength: float, drawWeight: float=222.4, curvature: float=1.3):
    summary = []
    for bowWidth in [0.038, 0.045, 0.050]:
        for bowLength in [1.45, 1.50, 1.55, 1.60, 1.65, 1.70]:
            try:
                pBow = makeBow(bowLength=bowLength, bowWidth=bowWidth, drawLength=drawLength)
                print(str(pBow))
                pBow.optimize(drawWeight=drawWeight, curvature=curvature)
                summary.append('{} {} {}'.format(str(pBow), pBow.summary(), pBow.summary(imperial=True)))
                symutil.saveBowToFile(pBow, './tmp/{}.bow'.format(str(pBow)))
            except:
                print('Oops...')
    return summary

summary = symBows(drawLength=0.71) #0.58)
print()
for element in summary:
    print(element)

# 38/0.58
# pb(1.50-0.50-(0.038-0.015)-1.30)-0.403)[0.16-0.58] arrow velocity: 56.898 m/s, (222.610 N @ 0.580 m) arrow velocity: 186.7 fps, (50.0 lbs @ 22.8")
# pb(1.55-0.50-(0.038-0.015)-1.30)-0.403)[0.16-0.58] arrow velocity: 57.159 m/s, (222.491 N @ 0.580 m) arrow velocity: 187.5 fps, (50.0 lbs @ 22.8")
# pb(1.60-0.50-(0.038-0.015)-1.30)-0.409)[0.16-0.58] arrow velocity: 57.221 m/s, (222.495 N @ 0.580 m) arrow velocity: 187.7 fps, (50.0 lbs @ 22.8")
# pb(1.65-0.50-(0.038-0.015)-1.30)-0.422)[0.16-0.58] arrow velocity: 57.244 m/s, (222.569 N @ 0.580 m) arrow velocity: 187.8 fps, (50.0 lbs @ 22.8") <-- 1)
# pb(1.70-0.50-(0.038-0.015)-1.30)-0.434)[0.16-0.58] arrow velocity: 57.123 m/s, (222.426 N @ 0.580 m) arrow velocity: 187.4 fps, (50.0 lbs @ 22.8")

# 45/0.58
# pb(1.50-0.50-(0.045-0.015)-1.30)-0.403)[0.16-0.58] arrow velocity: 56.780 m/s, (222.681 N @ 0.580 m) arrow velocity: 186.3 fps, (50.1 lbs @ 22.8")
# pb(1.55-0.50-(0.045-0.015)-1.30)-0.403)[0.16-0.58] arrow velocity: 56.994 m/s, (222.511 N @ 0.580 m) arrow velocity: 187.0 fps, (50.0 lbs @ 22.8")
# pb(1.60-0.50-(0.045-0.015)-1.30)-0.416)[0.16-0.58] arrow velocity: 57.214 m/s, (222.599 N @ 0.580 m) arrow velocity: 187.7 fps, (50.0 lbs @ 22.8") <-- 2)
# pb(1.65-0.50-(0.045-0.015)-1.30)-0.416)[0.16-0.58] arrow velocity: 57.153 m/s, (222.540 N @ 0.580 m) arrow velocity: 187.5 fps, (50.0 lbs @ 22.8")
# pb(1.70-0.50-(0.045-0.015)-1.30)-0.472)[0.16-0.58] arrow velocity: 57.081 m/s, (222.559 N @ 0.580 m) arrow velocity: 187.3 fps, (50.0 lbs @ 22.8")

#  50/0.58
# pb(1.50-0.50-(0.050-0.015)-1.30)-0.403)[0.16-0.58] arrow velocity: 56.735 m/s, (222.577 N @ 0.580 m) arrow velocity: 186.1 fps, (50.0 lbs @ 22.8")
# pb(1.55-0.50-(0.050-0.015)-1.30)-0.409)[0.16-0.58] arrow velocity: 56.987 m/s, (222.738 N @ 0.580 m) arrow velocity: 187.0 fps, (50.1 lbs @ 22.8")
# pb(1.60-0.50-(0.050-0.015)-1.30)-0.409)[0.16-0.58] arrow velocity: 57.126 m/s, (222.658 N @ 0.580 m) arrow velocity: 187.4 fps, (50.1 lbs @ 22.8")
# pb(1.65-0.50-(0.050-0.015)-1.30)-0.434)[0.16-0.58] arrow velocity: 57.135 m/s, (222.667 N @ 0.580 m) arrow velocity: 187.5 fps, (50.1 lbs @ 22.8") <-- 3)
# pb(1.70-0.50-(0.050-0.015)-1.30)-0.472)[0.16-0.58] arrow velocity: 57.070 m/s, (222.710 N @ 0.580 m) arrow velocity: 187.2 fps, (50.1 lbs @ 22.8")

# And the winner 23" is:
# pb(1.65-0.50-(0.038-0.015)-1.30)-0.422)[0.16-0.58] arrow velocity: 57.244 m/s, (222.569 N @ 0.580 m) arrow velocity: 187.8 fps, (50.0 lbs @ 22.8")

# pb(1.50-0.50-(0.038-0.015)-1.30)-0.403)[0.16-0.71] arrow velocity: 61.904 m/s, (222.866 N @ 0.710 m) arrow velocity: 203.1 fps, (50.1 lbs @ 28.0")
# pb(1.55-0.50-(0.038-0.015)-1.30)-0.403)[0.16-0.71] arrow velocity: 62.635 m/s, (222.465 N @ 0.710 m) arrow velocity: 205.5 fps, (50.0 lbs @ 28.0")
# pb(1.60-0.50-(0.038-0.015)-1.30)-0.403)[0.16-0.71] arrow velocity: 63.297 m/s, (222.778 N @ 0.710 m) arrow velocity: 207.7 fps, (50.1 lbs @ 28.0")
# pb(1.65-0.50-(0.038-0.015)-1.30)-0.434)[0.16-0.71] arrow velocity: 63.775 m/s, (222.620 N @ 0.710 m) arrow velocity: 209.2 fps, (50.0 lbs @ 28.0")
# pb(1.70-0.50-(0.038-0.015)-1.30)-0.472)[0.16-0.71] arrow velocity: 64.094 m/s, (222.190 N @ 0.710 m) arrow velocity: 210.3 fps, (50.0 lbs @ 28.0") <-- 1)

# pb(1.50-0.50-(0.045-0.015)-1.30)-0.403)[0.16-0.71] arrow velocity: 61.941 m/s, (223.189 N @ 0.710 m) arrow velocity: 203.2 fps, (50.2 lbs @ 28.0")
# pb(1.55-0.50-(0.045-0.015)-1.30)-0.403)[0.16-0.71] arrow velocity: 62.669 m/s, (222.924 N @ 0.710 m) arrow velocity: 205.6 fps, (50.1 lbs @ 28.0")
# pb(1.60-0.50-(0.045-0.015)-1.30)-0.416)[0.16-0.71] arrow velocity: 63.175 m/s, (222.486 N @ 0.710 m) arrow velocity: 207.3 fps, (50.0 lbs @ 28.0")
# pb(1.65-0.50-(0.045-0.015)-1.30)-0.434)[0.16-0.71] arrow velocity: 63.645 m/s, (222.730 N @ 0.710 m) arrow velocity: 208.8 fps, (50.1 lbs @ 28.0")
# pb(1.70-0.50-(0.045-0.015)-1.30)-0.478)[0.16-0.71] arrow velocity: 64.053 m/s, (222.635 N @ 0.710 m) arrow velocity: 210.2 fps, (50.1 lbs @ 28.0") <-- 2)

# pb(1.50-0.50-(0.050-0.015)-1.30)-0.403)[0.16-0.71] arrow velocity: 61.919 m/s, (223.292 N @ 0.710 m) arrow velocity: 203.2 fps, (50.2 lbs @ 28.0")
# pb(1.55-0.50-(0.050-0.015)-1.30)-0.403)[0.16-0.71] arrow velocity: 62.637 m/s, (223.001 N @ 0.710 m) arrow velocity: 205.5 fps, (50.1 lbs @ 28.0")
# pb(1.60-0.50-(0.050-0.015)-1.30)-0.416)[0.16-0.71] arrow velocity: 63.125 m/s, (222.616 N @ 0.710 m) arrow velocity: 207.1 fps, (50.0 lbs @ 28.0")
# pb(1.65-0.50-(0.050-0.015)-1.30)-0.497)[0.16-0.71] arrow velocity: 56.874 m/s, (176.195 N @ 0.710 m) arrow velocity: 186.6 fps, (39.6 lbs @ 28.0")
# pb(1.70-0.50-(0.050-0.015)-1.30)-0.478)[0.16-0.71] arrow velocity: 63.891 m/s, (222.645 N @ 0.710 m) arrow velocity: 209.6 fps, (50.1 lbs @ 28.0") <-- 3)

# And the winner 28" is:
# pb(1.70-0.50-(0.038-0.015)-1.30)-0.472)[0.16-0.71] arrow velocity: 64.094 m/s, (222.190 N @ 0.710 m) arrow velocity: 210.3 fps, (50.0 lbs @ 28.0")