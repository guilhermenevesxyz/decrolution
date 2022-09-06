import enum

class Sensor(enum.Enum):
	pass

class Behaviour(enum.Enum):
	pass

class Brain:
	def __init__(self):
		self.data: dict[Sensor, Behaviour] = {}

class Creature:
	def __init__(self, brain: Brain = Brain()):
		pass
	
	def update(self):
		pass

class Simulation:
	def __init__(self):
		self.creatures = []
	
	def update(self):
		for creature in self.creatures:
			creature.update()

