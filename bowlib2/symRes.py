import numpy

class _Jsonizer:
	def asJson(self):
		import json
		return json.dumps(self, default = self._serialize, indent = 2)
		
	@staticmethod
	def _serialize(obj):
		res = {}
		for key in obj.__dict__.keys():
			if key[0] == '_':
					res[key[1:]] = obj.__dict__[key]
			else:
				res[key] = obj.__dict__[key]
		return res
	
	@staticmethod
	def jsonStrToObject(jsonStr: str):
		import json
		from types import SimpleNamespace
		return json.loads(jsonStr, object_hook=lambda d: SimpleNamespace(**d))

	@staticmethod
	def jsonStrToDict(jsonStr: str):
		import json
		return json.loads(jsonStr)

	@classmethod
	def fromJson(cls, jsonStr: str):
		# pylint: disable=no-member 
		return cls.initFromDict(cls.jsonStrToDict(jsonStr))

from typing import List

class States(_Jsonizer):
	def __init__(self, acc_arrow: list, angle_limb: list, draw_force: list, draw_length: list, e_kin_arrow: list, e_kin_limbs: list, e_kin_string: list, e_pot_limbs: list, e_pot_string: list, epsilon: list, grip_force: list, kappa: list, pos_arrow: list, strand_force: list, string_force: list, time: list, vel_arrow: list, x_pos_limb: list, x_pos_string: list, y_pos_limb: list, y_pos_string: list):
		self.acc_arrow = acc_arrow
		self.angle_limb = angle_limb
		self.draw_force = draw_force
		self.draw_length = draw_length
		self.e_kin_arrow = e_kin_arrow
		self.e_kin_limbs = e_kin_limbs
		self.e_kin_string = e_kin_string
		self.e_pot_limbs = e_pot_limbs
		self.e_pot_string = e_pot_string
		self.epsilon = epsilon
		self.grip_force = grip_force
		self.kappa = kappa
		self.pos_arrow = pos_arrow
		self.strand_force = strand_force
		self.string_force = string_force
		self.time = time
		self.vel_arrow = vel_arrow
		self.x_pos_limb = x_pos_limb
		self.x_pos_string = x_pos_string
		self.y_pos_limb = y_pos_limb
		self.y_pos_string = y_pos_string

	@classmethod
	def initFromDict(cls, data):
		return States(
			acc_arrow = data['acc_arrow'],
			angle_limb = data['angle_limb'],
			draw_force = data['draw_force'],
			draw_length = data['draw_length'],
			e_kin_arrow = data['e_kin_arrow'],
			e_kin_limbs = data['e_kin_limbs'],
			e_kin_string = data['e_kin_string'],
			e_pot_limbs = data['e_pot_limbs'],
			e_pot_string = data['e_pot_string'],
			epsilon = data['epsilon'],
			grip_force = data['grip_force'],
			kappa = data['kappa'],
			pos_arrow = data['pos_arrow'],
			strand_force = data['strand_force'],
			string_force = data['string_force'],
			time = data['time'],
			vel_arrow = data['vel_arrow'],
			x_pos_limb = data['x_pos_limb'],
			x_pos_string = data['x_pos_string'],
			y_pos_limb = data['y_pos_limb'],
			y_pos_string = data['y_pos_string'],
			)

	@property
	def acc_arrow(self) -> list:
		return self._acc_arrow

	@acc_arrow.setter
	def acc_arrow(self, acc_arrow: list):
		self._acc_arrow = acc_arrow

	@property
	def angle_limb(self) -> list:
		return self._angle_limb

	@angle_limb.setter
	def angle_limb(self, angle_limb: list):
		self._angle_limb = angle_limb

	@property
	def draw_force(self) -> list:
		return self._draw_force

	@draw_force.setter
	def draw_force(self, draw_force: list):
		self._draw_force = draw_force

	@property
	def draw_length(self) -> list:
		return self._draw_length

	@draw_length.setter
	def draw_length(self, draw_length: list):
		self._draw_length = draw_length

	@property
	def e_kin_arrow(self) -> list:
		return self._e_kin_arrow

	@e_kin_arrow.setter
	def e_kin_arrow(self, e_kin_arrow: list):
		self._e_kin_arrow = e_kin_arrow

	@property
	def e_kin_limbs(self) -> list:
		return self._e_kin_limbs

	@e_kin_limbs.setter
	def e_kin_limbs(self, e_kin_limbs: list):
		self._e_kin_limbs = e_kin_limbs

	@property
	def e_kin_string(self) -> list:
		return self._e_kin_string

	@e_kin_string.setter
	def e_kin_string(self, e_kin_string: list):
		self._e_kin_string = e_kin_string

	@property
	def e_pot_limbs(self) -> list:
		return self._e_pot_limbs

	@e_pot_limbs.setter
	def e_pot_limbs(self, e_pot_limbs: list):
		self._e_pot_limbs = e_pot_limbs

	@property
	def e_pot_string(self) -> list:
		return self._e_pot_string

	@e_pot_string.setter
	def e_pot_string(self, e_pot_string: list):
		self._e_pot_string = e_pot_string

	@property
	def epsilon(self) -> list:
		return self._epsilon

	@epsilon.setter
	def epsilon(self, epsilon: list):
		self._epsilon = epsilon

	@property
	def grip_force(self) -> list:
		return self._grip_force

	@grip_force.setter
	def grip_force(self, grip_force: list):
		self._grip_force = grip_force

	@property
	def kappa(self) -> list:
		return self._kappa

	@kappa.setter
	def kappa(self, kappa: list):
		self._kappa = kappa

	@property
	def pos_arrow(self) -> list:
		return self._pos_arrow

	@pos_arrow.setter
	def pos_arrow(self, pos_arrow: list):
		self._pos_arrow = pos_arrow

	@property
	def strand_force(self) -> list:
		return self._strand_force

	@strand_force.setter
	def strand_force(self, strand_force: list):
		self._strand_force = strand_force

	@property
	def string_force(self) -> list:
		return self._string_force

	@string_force.setter
	def string_force(self, string_force: list):
		self._string_force = string_force

	@property
	def time(self) -> list:
		return self._time

	@time.setter
	def time(self, time: list):
		self._time = time

	@property
	def vel_arrow(self) -> list:
		return self._vel_arrow

	@vel_arrow.setter
	def vel_arrow(self, vel_arrow: list):
		self._vel_arrow = vel_arrow

	@property
	def x_pos_limb(self) -> list:
		return self._x_pos_limb

	@x_pos_limb.setter
	def x_pos_limb(self, x_pos_limb: list):
		self._x_pos_limb = x_pos_limb

	@property
	def x_pos_string(self) -> list:
		return self._x_pos_string

	@x_pos_string.setter
	def x_pos_string(self, x_pos_string: list):
		self._x_pos_string = x_pos_string

	@property
	def y_pos_limb(self) -> list:
		return self._y_pos_limb

	@y_pos_limb.setter
	def y_pos_limb(self, y_pos_limb: list):
		self._y_pos_limb = y_pos_limb

	@property
	def y_pos_string(self) -> list:
		return self._y_pos_string

	@y_pos_string.setter
	def y_pos_string(self, y_pos_string: list):
		self._y_pos_string = y_pos_string

class Dynamics(_Jsonizer):
	def __init__(self, efficiency: float, final_e_kin_arrow: float, final_e_kin_limbs: float, final_e_kin_string: float, final_e_pot_limbs: float, final_e_pot_string: float, final_pos_arrow: float, final_vel_arrow: float, max_grip_force_index: int, max_stress_index: list, max_stress_value: list, max_string_force_index: int, states: States):
		self.efficiency = efficiency
		self.final_e_kin_arrow = final_e_kin_arrow
		self.final_e_kin_limbs = final_e_kin_limbs
		self.final_e_kin_string = final_e_kin_string
		self.final_e_pot_limbs = final_e_pot_limbs
		self.final_e_pot_string = final_e_pot_string
		self.final_pos_arrow = final_pos_arrow
		self.final_vel_arrow = final_vel_arrow
		self.max_grip_force_index = max_grip_force_index
		self.max_stress_index = max_stress_index
		self.max_stress_value = max_stress_value
		self.max_string_force_index = max_string_force_index
		self.states = states

	@classmethod
	def initFromDict(cls, data):
		return Dynamics(
			efficiency = data['efficiency'],
			final_e_kin_arrow = data['final_e_kin_arrow'],
			final_e_kin_limbs = data['final_e_kin_limbs'],
			final_e_kin_string = data['final_e_kin_string'],
			final_e_pot_limbs = data['final_e_pot_limbs'],
			final_e_pot_string = data['final_e_pot_string'],
			final_pos_arrow = data['final_pos_arrow'],
			final_vel_arrow = data['final_vel_arrow'],
			max_grip_force_index = data['max_grip_force_index'],
			max_stress_index = data['max_stress_index'],
			max_stress_value = data['max_stress_value'],
			max_string_force_index = data['max_string_force_index'],
			states = States.initFromDict(data['states']),
			)

	@property
	def efficiency(self) -> float:
		return self._efficiency

	@efficiency.setter
	def efficiency(self, efficiency: float):
		self._efficiency = efficiency

	@property
	def final_e_kin_arrow(self) -> float:
		return self._final_e_kin_arrow

	@final_e_kin_arrow.setter
	def final_e_kin_arrow(self, final_e_kin_arrow: float):
		self._final_e_kin_arrow = final_e_kin_arrow

	@property
	def final_e_kin_limbs(self) -> float:
		return self._final_e_kin_limbs

	@final_e_kin_limbs.setter
	def final_e_kin_limbs(self, final_e_kin_limbs: float):
		self._final_e_kin_limbs = final_e_kin_limbs

	@property
	def final_e_kin_string(self) -> float:
		return self._final_e_kin_string

	@final_e_kin_string.setter
	def final_e_kin_string(self, final_e_kin_string: float):
		self._final_e_kin_string = final_e_kin_string

	@property
	def final_e_pot_limbs(self) -> float:
		return self._final_e_pot_limbs

	@final_e_pot_limbs.setter
	def final_e_pot_limbs(self, final_e_pot_limbs: float):
		self._final_e_pot_limbs = final_e_pot_limbs

	@property
	def final_e_pot_string(self) -> float:
		return self._final_e_pot_string

	@final_e_pot_string.setter
	def final_e_pot_string(self, final_e_pot_string: float):
		self._final_e_pot_string = final_e_pot_string

	@property
	def final_pos_arrow(self) -> float:
		return self._final_pos_arrow

	@final_pos_arrow.setter
	def final_pos_arrow(self, final_pos_arrow: float):
		self._final_pos_arrow = final_pos_arrow

	@property
	def final_vel_arrow(self) -> float:
		return self._final_vel_arrow

	@final_vel_arrow.setter
	def final_vel_arrow(self, final_vel_arrow: float):
		self._final_vel_arrow = final_vel_arrow

	@property
	def max_grip_force_index(self) -> int:
		return self._max_grip_force_index

	@max_grip_force_index.setter
	def max_grip_force_index(self, max_grip_force_index: int):
		self._max_grip_force_index = max_grip_force_index

	@property
	def max_stress_index(self) -> list:
		return self._max_stress_index

	@max_stress_index.setter
	def max_stress_index(self, max_stress_index: list):
		self._max_stress_index = max_stress_index

	@property
	def max_stress_value(self) -> list:
		return self._max_stress_value

	@max_stress_value.setter
	def max_stress_value(self, max_stress_value: list):
		self._max_stress_value = max_stress_value

	@property
	def max_string_force_index(self) -> int:
		return self._max_string_force_index

	@max_string_force_index.setter
	def max_string_force_index(self, max_string_force_index: int):
		self._max_string_force_index = max_string_force_index

	@property
	def states(self) -> States:
		return self._states

	@states.setter
	def states(self, states: States):
		self._states = states

class Layer(_Jsonizer):
	def __init__(self, E: float, He_back: list, He_belly: list, Hk_back: list, Hk_belly: list, length: list, name: str, rho: float):
		self.E = E
		self.He_back = He_back
		self.He_belly = He_belly
		self.Hk_back = Hk_back
		self.Hk_belly = Hk_belly
		self.length = length
		self.name = name
		self.rho = rho

	@classmethod
	def initFromDict(cls, data):
		return Layer(
			E = data['E'],
			He_back = data['He_back'],
			He_belly = data['He_belly'],
			Hk_back = data['Hk_back'],
			Hk_belly = data['Hk_belly'],
			length = data['length'],
			name = data['name'],
			rho = data['rho'],
			)

	@property
	def E(self) -> float:
		return self._E

	@E.setter
	def E(self, E: float):
		self._E = E

	@property
	def He_back(self) -> list:
		return self._He_back

	@He_back.setter
	def He_back(self, He_back: list):
		self._He_back = He_back

	@property
	def He_belly(self) -> list:
		return self._He_belly

	@He_belly.setter
	def He_belly(self, He_belly: list):
		self._He_belly = He_belly

	@property
	def Hk_back(self) -> list:
		return self._Hk_back

	@Hk_back.setter
	def Hk_back(self, Hk_back: list):
		self._Hk_back = Hk_back

	@property
	def Hk_belly(self) -> list:
		return self._Hk_belly

	@Hk_belly.setter
	def Hk_belly(self, Hk_belly: list):
		self._Hk_belly = Hk_belly

	@property
	def length(self) -> list:
		return self._length

	@length.setter
	def length(self, length: list):
		self._length = length

	@property
	def name(self) -> str:
		return self._name

	@name.setter
	def name(self, name: str):
		self._name = name

	@property
	def rho(self) -> float:
		return self._rho

	@rho.setter
	def rho(self, rho: float):
		self._rho = rho

class Limb_properties(_Jsonizer):
	def __init__(self, Cee: list, Cek: list, Ckk: list, angle: list, height: list, layers: List[Layer], length: list, rhoA: list, width: list, x_pos: list, y_pos: list):
		self.Cee = Cee
		self.Cek = Cek
		self.Ckk = Ckk
		self.angle = angle
		self.height = height
		self.layers = layers
		self.length = length
		self.rhoA = rhoA
		self.width = width
		self.x_pos = x_pos
		self.y_pos = y_pos

	@classmethod
	def initFromDict(cls, data):
		return Limb_properties(
			Cee = data['Cee'],
			Cek = data['Cek'],
			Ckk = data['Ckk'],
			angle = data['angle'],
			height = data['height'],
			layers = [Layer.initFromDict(x) for x in data['layers']],
			length = data['length'],
			rhoA = data['rhoA'],
			width = data['width'],
			x_pos = data['x_pos'],
			y_pos = data['y_pos'],
			)

	@property
	def Cee(self) -> list:
		return self._Cee

	@Cee.setter
	def Cee(self, Cee: list):
		self._Cee = Cee

	@property
	def Cek(self) -> list:
		return self._Cek

	@Cek.setter
	def Cek(self, Cek: list):
		self._Cek = Cek

	@property
	def Ckk(self) -> list:
		return self._Ckk

	@Ckk.setter
	def Ckk(self, Ckk: list):
		self._Ckk = Ckk

	@property
	def angle(self) -> list:
		return self._angle

	@angle.setter
	def angle(self, angle: list):
		self._angle = angle

	@property
	def height(self) -> list:
		return self._height

	@height.setter
	def height(self, height: list):
		self._height = height

	@property
	def layers(self) -> List[Layer]:
		return self._layers

	@layers.setter
	def layers(self, layers: List[Layer]):
		self._layers = layers

	@property
	def length(self) -> list:
		return self._length

	@length.setter
	def length(self, length: list):
		self._length = length

	@property
	def rhoA(self) -> list:
		return self._rhoA

	@rhoA.setter
	def rhoA(self, rhoA: list):
		self._rhoA = rhoA

	@property
	def width(self) -> list:
		return self._width

	@width.setter
	def width(self, width: list):
		self._width = width

	@property
	def x_pos(self) -> list:
		return self._x_pos

	@x_pos.setter
	def x_pos(self, x_pos: list):
		self._x_pos = x_pos

	@property
	def y_pos(self) -> list:
		return self._y_pos

	@y_pos.setter
	def y_pos(self, y_pos: list):
		self._y_pos = y_pos

class Setup(_Jsonizer):
	def __init__(self, limb_mass: float, limb_properties: Limb_properties, string_length: float, string_mass: float):
		self.limb_mass = limb_mass
		self.limb_properties = limb_properties
		self.string_length = string_length
		self.string_mass = string_mass

	@classmethod
	def initFromDict(cls, data):
		return Setup(
			limb_mass = data['limb_mass'],
			limb_properties = Limb_properties.initFromDict(data['limb_properties']),
			string_length = data['string_length'],
			string_mass = data['string_mass'],
			)

	@property
	def limb_mass(self) -> float:
		return self._limb_mass

	@limb_mass.setter
	def limb_mass(self, limb_mass: float):
		self._limb_mass = limb_mass

	@property
	def limb_properties(self) -> Limb_properties:
		return self._limb_properties

	@limb_properties.setter
	def limb_properties(self, limb_properties: Limb_properties):
		self._limb_properties = limb_properties

	@property
	def string_length(self) -> float:
		return self._string_length

	@string_length.setter
	def string_length(self, string_length: float):
		self._string_length = string_length

	@property
	def string_mass(self) -> float:
		return self._string_mass

	@string_mass.setter
	def string_mass(self, string_mass: float):
		self._string_mass = string_mass

class Statics(_Jsonizer):
	def __init__(self, drawing_work: float, final_draw_force: float, max_draw_force_index: int, max_grip_force_index: int, max_stress_index: list, max_stress_value: list, max_string_force_index: int, states: States):
		self.drawing_work = drawing_work
		self.final_draw_force = final_draw_force
		self.max_draw_force_index = max_draw_force_index
		self.max_grip_force_index = max_grip_force_index
		self.max_stress_index = max_stress_index
		self.max_stress_value = max_stress_value
		self.max_string_force_index = max_string_force_index
		self.states = states

	@classmethod
	def initFromDict(cls, data):
		return Statics(
			drawing_work = data['drawing_work'],
			final_draw_force = data['final_draw_force'],
			max_draw_force_index = data['max_draw_force_index'],
			max_grip_force_index = data['max_grip_force_index'],
			max_stress_index = data['max_stress_index'],
			max_stress_value = data['max_stress_value'],
			max_string_force_index = data['max_string_force_index'],
			states = States.initFromDict(data['states'])
			)

	@property
	def drawing_work(self) -> float:
		return self._drawing_work

	@drawing_work.setter
	def drawing_work(self, drawing_work: float):
		self._drawing_work = drawing_work

	@property
	def final_draw_force(self) -> float:
		return self._final_draw_force

	@final_draw_force.setter
	def final_draw_force(self, final_draw_force: float):
		self._final_draw_force = final_draw_force

	@property
	def max_draw_force_index(self) -> int:
		return self._max_draw_force_index

	@max_draw_force_index.setter
	def max_draw_force_index(self, max_draw_force_index: int):
		self._max_draw_force_index = max_draw_force_index

	@property
	def max_grip_force_index(self) -> int:
		return self._max_grip_force_index

	@max_grip_force_index.setter
	def max_grip_force_index(self, max_grip_force_index: int):
		self._max_grip_force_index = max_grip_force_index

	@property
	def max_stress_index(self) -> list:
		return self._max_stress_index

	@max_stress_index.setter
	def max_stress_index(self, max_stress_index: list):
		self._max_stress_index = max_stress_index

	@property
	def max_stress_value(self) -> list:
		return self._max_stress_value

	@max_stress_value.setter
	def max_stress_value(self, max_stress_value: list):
		self._max_stress_value = max_stress_value

	@property
	def max_string_force_index(self) -> int:
		return self._max_string_force_index

	@max_string_force_index.setter
	def max_string_force_index(self, max_string_force_index: int):
		self._max_string_force_index = max_string_force_index

	@property
	def states(self) -> States:
		return self._states

	@states.setter
	def states(self, states: States):
		self._states = states

class SymRes(_Jsonizer):
	def __init__(self, dynamics: Dynamics, setup: Setup, statics: Statics, version: str):
		self.dynamics = dynamics
		self.setup = setup
		self.statics = statics
		self.version = version

	def calculateCurvatureError(self, start: float, end: float) -> float:
		""" Calculate the curvature error for a given limb span as area below the curvature.\n
            Smaller is better.
        """
		nbrOfSymSteps = len(self.setup.limb_properties.length)
		kappa = self.statics.states.kappa[-1][int(start*nbrOfSymSteps):int(end*nbrOfSymSteps)]
		res = 0
		min = numpy.min(kappa)
		for i in range(len(kappa)):
			res += kappa[i] - min
		# return res
		# Sacle the error for different lengths
		return res / len(kappa)

	@classmethod
	def initFromDict(cls, data):
		return SymRes(
			dynamics = Dynamics.initFromDict(data['dynamics']),
			setup = Setup.initFromDict(data['setup']),
			statics = Statics.initFromDict(data['statics']),
			version = data['version'],
			)

	@property
	def dynamics(self) -> Dynamics:
		return self._dynamics

	@dynamics.setter
	def dynamics(self, dynamics: Dynamics):
		self._dynamics = dynamics

	@property
	def setup(self) -> Setup:
		return self._setup

	@setup.setter
	def setup(self, setup: Setup):
		self._setup = setup

	@property
	def statics(self) -> Statics:
		return self._statics

	@statics.setter
	def statics(self, statics: Statics):
		self._statics = statics

	@property
	def version(self) -> str:
		return self._version

	@version.setter
	def version(self, version: str):
		self._version = version

