from .symRes import SymRes

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

class Damping(_Jsonizer):
	def __init__(self, damping_ratio_limbs: float, damping_ratio_string: float):
		self.damping_ratio_limbs = damping_ratio_limbs
		self.damping_ratio_string = damping_ratio_string

	@classmethod
	def initFromDict(cls, data):
		return Damping(
			damping_ratio_limbs = data['damping_ratio_limbs'],
			damping_ratio_string = data['damping_ratio_string'],
			)

	@property
	def damping_ratio_limbs(self) -> float:
		return self._damping_ratio_limbs

	@damping_ratio_limbs.setter
	def damping_ratio_limbs(self, damping_ratio_limbs: float):
		self._damping_ratio_limbs = damping_ratio_limbs

	@property
	def damping_ratio_string(self) -> float:
		return self._damping_ratio_string

	@damping_ratio_string.setter
	def damping_ratio_string(self, damping_ratio_string: float):
		self._damping_ratio_string = damping_ratio_string

class Dimensions(_Jsonizer):
	def __init__(self, brace_height: float, draw_length: float, handle_angle: float, handle_length: float, handle_setback: float):
		self.brace_height = brace_height
		self.draw_length = draw_length
		self.handle_angle = handle_angle
		self.handle_length = handle_length
		self.handle_setback = handle_setback

	@classmethod
	def initFromDict(cls, data):
		return Dimensions(
			brace_height = data['brace_height'],
			draw_length = data['draw_length'],
			handle_angle = data['handle_angle'],
			handle_length = data['handle_length'],
			handle_setback = data['handle_setback'],
			)

	@property
	def brace_height(self) -> float:
		return self._brace_height

	@brace_height.setter
	def brace_height(self, brace_height: float):
		self._brace_height = brace_height

	@property
	def draw_length(self) -> float:
		return self._draw_length

	@draw_length.setter
	def draw_length(self, draw_length: float):
		self._draw_length = draw_length

	@property
	def handle_angle(self) -> float:
		return self._handle_angle

	@handle_angle.setter
	def handle_angle(self, handle_angle: float):
		self._handle_angle = handle_angle

	@property
	def handle_length(self) -> float:
		return self._handle_length

	@handle_length.setter
	def handle_length(self, handle_length: float):
		self._handle_length = handle_length

	@property
	def handle_setback(self) -> float:
		return self._handle_setback

	@handle_setback.setter
	def handle_setback(self, handle_setback: float):
		self._handle_setback = handle_setback

class Material:
	def __init__(self, E: float, name: str, rho: float):
		self.E = E
		self.name = name
		self.rho = rho

class Layer(_Jsonizer):
	def __init__(self, E: float, height: list, name: str, rho: float):
		self.E = E
		self.height = height
		self.name = name
		self.rho = rho

	@classmethod
	def initFromMaterial(cls, data: Material, height):
		if type(height) is float:
			height = [[0.00, height], [1.00, height]]
		return Layer(
			E = data.E,
			name = data.name,
			rho = data.rho,
			height = height
		)

	@classmethod
	def initFromDict(cls, data):
		return Layer(
			E = data['E'],
			height = data['height'],
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
	def height(self) -> list:
		return self._height

	@height.setter
	def height(self, height: list):
		self._height = height

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

class Masses(_Jsonizer):
	def __init__(self, arrow: float, limb_tip: float, string_center: float, string_tip: float):
		self.arrow = arrow
		self.limb_tip = limb_tip
		self.string_center = string_center
		self.string_tip = string_tip

	@classmethod
	def initFromDict(cls, data):
		return Masses(
			arrow = data['arrow'],
			limb_tip = data['limb_tip'],
			string_center = data['string_center'],
			string_tip = data['string_tip'],
			)

	@property
	def arrow(self) -> float:
		return self._arrow

	@arrow.setter
	def arrow(self, arrow: float):
		self._arrow = arrow

	@property
	def limb_tip(self) -> float:
		return self._limb_tip

	@limb_tip.setter
	def limb_tip(self, limb_tip: float):
		self._limb_tip = limb_tip

	@property
	def string_center(self) -> float:
		return self._string_center

	@string_center.setter
	def string_center(self, string_center: float):
		self._string_center = string_center

	@property
	def string_tip(self) -> float:
		return self._string_tip

	@string_tip.setter
	def string_tip(self, string_tip: float):
		self._string_tip = string_tip

class Settings(_Jsonizer):
	def __init__(self, n_draw_steps: int, n_limb_elements: int, n_string_elements: int, sampling_rate: float, time_span_factor: float, time_step_factor: float):
		self.n_draw_steps = n_draw_steps
		self.n_limb_elements = n_limb_elements
		self.n_string_elements = n_string_elements
		self.sampling_rate = sampling_rate
		self.time_span_factor = time_span_factor
		self.time_step_factor = time_step_factor

	@classmethod
	def initFromDict(cls, data):
		return Settings(
			n_draw_steps = data['n_draw_steps'],
			n_limb_elements = data['n_limb_elements'],
			n_string_elements = data['n_string_elements'],
			sampling_rate = data['sampling_rate'],
			time_span_factor = data['time_span_factor'],
			time_step_factor = data['time_step_factor'],
			)

	@property
	def n_draw_steps(self) -> int:
		return self._n_draw_steps

	@n_draw_steps.setter
	def n_draw_steps(self, n_draw_steps: int):
		self._n_draw_steps = n_draw_steps

	@property
	def n_limb_elements(self) -> int:
		return self._n_limb_elements

	@n_limb_elements.setter
	def n_limb_elements(self, n_limb_elements: int):
		self._n_limb_elements = n_limb_elements

	@property
	def n_string_elements(self) -> int:
		return self._n_string_elements

	@n_string_elements.setter
	def n_string_elements(self, n_string_elements: int):
		self._n_string_elements = n_string_elements

	@property
	def sampling_rate(self) -> float:
		return self._sampling_rate

	@sampling_rate.setter
	def sampling_rate(self, sampling_rate: float):
		self._sampling_rate = sampling_rate

	@property
	def time_span_factor(self) -> float:
		return self._time_span_factor

	@time_span_factor.setter
	def time_span_factor(self, time_span_factor: float):
		self._time_span_factor = time_span_factor

	@property
	def time_step_factor(self) -> float:
		return self._time_step_factor

	@time_step_factor.setter
	def time_step_factor(self, time_step_factor: float):
		self._time_step_factor = time_step_factor

class String(_Jsonizer):
	def __init__(self, n_strands: int, strand_density: float, strand_stiffness: float):
		self.n_strands = n_strands
		self.strand_density = strand_density
		self.strand_stiffness = strand_stiffness

	@classmethod
	def initFromDict(cls, data):
		return String(
			n_strands = data['n_strands'],
			strand_density = data['strand_density'],
			strand_stiffness = data['strand_stiffness'],
			)

	@property
	def n_strands(self) -> int:
		return self._n_strands

	@n_strands.setter
	def n_strands(self, n_strands: int):
		self._n_strands = n_strands

	@property
	def strand_density(self) -> float:
		return self._strand_density

	@strand_density.setter
	def strand_density(self, strand_density: float):
		self._strand_density = strand_density

	@property
	def strand_stiffness(self) -> float:
		return self._strand_stiffness

	@strand_stiffness.setter
	def strand_stiffness(self, strand_stiffness: float):
		self._strand_stiffness = strand_stiffness

class Bow(_Jsonizer):
	def __init__(self, damping: Damping, dimensions: Dimensions, layers: List[Layer], masses: Masses, profile: list, settings: Settings, string: String, width: list, comment: str = '', version: str = "0.7.1"):
		self.comment = comment
		self.damping = damping
		self.dimensions = dimensions
		self.layers = layers
		self.masses = masses
		self.profile = profile
		self.settings = settings
		self.string = string
		self.version = version
		self.width = width
		self._symRes = None

	@classmethod
	def initFromDict(cls, data):
		return Bow(
			comment = data['comment'],
			damping = Damping.initFromDict(data['damping']),
			dimensions = Dimensions.initFromDict(data['dimensions']),
			layers = [Layer.initFromDict(x) for x in data['layers']],
			masses = Masses.initFromDict(data['masses']),
			profile = data['profile'],
			settings = Settings.initFromDict(data['settings']),
			string = String.initFromDict(data['string']),
			version = data['version'],
			width = data['width'],
			)

	@property
	def comment(self) -> str:
		return self._comment

	@comment.setter
	def comment(self, comment: str):
		self._comment = comment

	@property
	def damping(self) -> Damping:
		return self._damping

	@damping.setter
	def damping(self, damping: Damping):
		self._damping = damping

	@property
	def dimensions(self) -> Dimensions:
		return self._dimensions

	@dimensions.setter
	def dimensions(self, dimensions: Dimensions):
		self._dimensions = dimensions

	@property
	def layers(self) -> List[Layer]:
		return self._layers

	@layers.setter
	def layers(self, layers: List[Layer]):
		self._layers = layers

	@property
	def masses(self) -> Masses:
		return self._masses

	@masses.setter
	def masses(self, masses: Masses):
		self._masses = masses

	@property
	def profile(self) -> list:
		return self._profile

	@profile.setter
	def profile(self, profile: list):
		self._profile = profile

	@property
	def settings(self) -> Settings:
		return self._settings

	@settings.setter
	def settings(self, settings: Settings):
		self._settings = settings

	@property
	def string(self) -> String:
		return self._string

	@string.setter
	def string(self, string: String):
		self._string = string

	@property
	def version(self) -> str:
		return self._version

	@version.setter
	def version(self, version: str):
		self._version = version

	@property
	def width(self) -> list:
		return self._width

	@width.setter
	def width(self, width: list):
		self._width = width

	@property
	def cachedSymRes(self) -> SymRes:
		return self._symRes

	@cachedSymRes.setter
	def cachedSymRes(self, symRes: SymRes):
		self._symRes = symRes