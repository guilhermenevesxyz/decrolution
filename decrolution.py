import enum
import random

random.seed()

class Sensor(enum.Enum):
	pass

class Behaviour(enum.Enum):
	pass

class Brain:
	def __init__(self):
		self.data: dict[Sensor, Behaviour] = {}

class Creature:
	def __init__(self, position: (int, int), brain: Brain = Brain()):
		self.position: (int, int) = position
		self.brain: Brain = brain
		self.request: Behaviour = None
	
	def update(self):
		pass

class Simulation:
	creatures: list[Creature] = []
	size: int = 20
	
	def initialize():
		for i in range(Simulation.size):
			for j in range(Simulation.size):
				if random.randrange(0, 101) <= 10:
					Simulation.creatures.append(Creature((i, j)))
	
	def update():
		for creature in Simulation.creatures:
			if not creature == None:
				creature.update()

