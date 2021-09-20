from .bow import Material

cfk = Material(
    E = 90000000000.0,
    name = "cfk",
    rho = 1920.0
)
bamboo = Material(
    E = 13130000000.0,
    name = "core",
    rho = 510.0
)
core = bamboo

ash = Material(
    name='ash',
    E=12000000000.0,
    rho=720.0
)
glass = Material(
    name='glass',
    E=41000000000.0,
    rho=1920.0
)
