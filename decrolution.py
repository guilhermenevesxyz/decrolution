import enum
import random

random.seed()

class Sensor(enum.Enum):
	CreUp = 0
	CreLeft = 1
	CreDown = 2
	CreRight = 3
	
	FreeUp = 4
	FreeLeft = 5
	FreeDown = 6
	FreeRight = 7

class Behaviour(enum.Enum):
	MvUp = 0
	MvLeft = 1
	MvDown = 2
	MvRight = 3

class Brain:
	def __init__(self):
		self.data: dict[Sensor, Behaviour] = {
			Sensor.FreeDown: Behaviour.MvDown
		}

class Creature:
	def __init__(self, position: (int, int), brain: Brain = Brain()):
		self.position: (int, int) = position
		self.brain: Brain = brain
		self.request: Behaviour = None
	
	def update(self):
		for sensor, behaviour in self.brain.data.items():
			if Simulation.query(self, sensor):
				Simulation.request(self, behaviour)

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
	
	def query(creature: Creature, sensor: Sensor):
		match sensor:
			case Sensor.CreUp:
				checkpos = (creature.position[0], creature.position[1] - 1)
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						return True
				
				return False
			
			case Sensor.CreLeft:
				checkpos = (creature.position[0] - 1, creature.position[1])
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						return True
				
				return False
			
			case Sensor.CreDown:
				checkpos = (creature.position[0], creature.position[1] + 1)
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						return True
				
				return False
			
			case Sensor.CreRight:
				checkpos = (creature.position[0] + 1, creature.position[1])
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						return True
				
				return False
			
			case Sensor.FreeUp:
				checkpos = (creature.position[0], creature.position[1] - 1)
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						return False
				
				return True
			
			case Sensor.FreeLeft:
				checkpos = (creature.position[0] - 1, creature.position[1])
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						return False
				
				return True
			
			case Sensor.FreeDown:
				checkpos = (creature.position[0], creature.position[1] + 1)
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						return False
				
				return True
			
			case Sensor.FreeRight:
				checkpos = (creature.position[0] + 1, creature.position[1])
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						return False
				
				return True
	
	def request(creature: Creature, behaviour: Behaviour):
		match behaviour:
			case Behaviour.MvUp:
				checkpos = (creature.position[0], creature.position[1] - 1)
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						return
				
				if checkpos[1] < 0:
					return
				
				creature.position = checkpos
			
			case Behaviour.MvLeft:
				checkpos = (creature.position[0] - 1, creature.position[1])
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						return
				
				if checkpos[0] < 0:
					return
				
				creature.position = checkpos
			
			case Behaviour.MvDown:
				checkpos = (creature.position[0], creature.position[1] + 1)
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						return
				
				if checkpos[1] > Simulation.size:
					return
				
				creature.position = checkpos

			case Behaviour.MvDown:
				checkpos = (creature.position[0] + 1, creature.position[1])
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						return
				
				if checkpos[0] > Simulation.size:
					return
				
				creature.position = checkpos

