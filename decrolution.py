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
	
	CreUp2 = 8
	CreLeft2 = 9
	CreDown2 = 10
	CreRight2 = 11
	
	CreUpRed = 12
	CreLeftRed = 13
	CreDownRed = 14
	CreRightRed = 15
	
	CreUpGreen = 16
	CreLeftGreen = 17
	CreDownGreen = 18
	CreRightGreen = 19
	
	CreUpBlue = 20
	CreLeftBlue = 21
	CreDownBlue = 22
	CreRightBlue = 23
	
	CreUpRed2 = 24
	CreLeftRed2 = 25
	CreDownRed2 = 26
	CreRightRed2 = 27
	
	CreUpGreen2 = 28
	CreLeftGreen2 = 29
	CreDownGreen2 = 30
	CreRightGreen2 = 31
	
	CreUpBlue2 = 32
	CreLeftBlue2 = 33
	CreDownBlue2 = 34
	CreRightBlue2 = 35

class Behaviour(enum.Enum):
	MvUp = 0
	MvLeft = 1
	MvDown = 2
	MvRight = 3

class Brain:
	def __init__(self):
		self.data: dict[Sensor, Behaviour] = {
			Sensor.CreUpRed2: Behaviour.MvUp,
			Sensor.CreLeftRed2: Behaviour.MvLeft,
			Sensor.CreDownRed2: Behaviour.MvDown,
			Sensor.CreRightRed2: Behaviour.MvRight
		}

class Creature:
	def __init__(self, position: (int, int), colour: (int, int, int), brain: Brain = Brain()):
		self.position: (int, int) = position
		self.brain: Brain = brain
		self.request: Behaviour = None
		self.colour: (int, int, int) = colour
	
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
					Simulation.creatures.append(Creature(
						(i, j),
						(
							random.randrange(50, 256),
							random.randrange(50, 256),
							random.randrange(50, 256)
						)
					))
	
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
			
			case Sensor.CreUp2:
				checkpos = (creature.position[0], creature.position[1] - 2)
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						return True
				
				return False
			
			case Sensor.CreLeft2:
				checkpos = (creature.position[0] - 2, creature.position[1])
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						return True
				
				return False
			
			case Sensor.CreDown2:
				checkpos = (creature.position[0], creature.position[1] + 2)
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						return True
				
				return False
			
			case Sensor.CreRight2:
				checkpos = (creature.position[0] + 2, creature.position[1])
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						return True
				
				return False
			
			case Sensor.CreUpRed:
				checkpos = (creature.position[0], creature.position[1] - 1)
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[0] > 100:
							return True
				
				return False
			
			case Sensor.CreLeftRed:
				checkpos = (creature.position[0] - 1, creature.position[1])
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[0] > 100:
							return True
				
				return False
			
			case Sensor.CreDownRed:
				checkpos = (creature.position[0], creature.position[1] + 1)
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[0] > 100:
							return True
				
				return False
			
			case Sensor.CreRightRed:
				checkpos = (creature.position[0] + 1, creature.position[1])
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[0] > 100:
							return True
				
				return False
			
			case Sensor.CreUpGreen:
				checkpos = (creature.position[0], creature.position[1] - 1)
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[1] > 100:
							return True
				
				return False
			
			case Sensor.CreLeftGreen:
				checkpos = (creature.position[0] - 1, creature.position[1])
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[1] > 100:
							return True
				
				return False
			
			case Sensor.CreDownGreen:
				checkpos = (creature.position[0], creature.position[1] + 1)
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[1] > 100:
							return True
				
				return False
			
			case Sensor.CreRightGreen:
				checkpos = (creature.position[0] + 1, creature.position[1])
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[1] > 100:
							return True
				
				return False
			
			case Sensor.CreUpBlue:
				checkpos = (creature.position[0], creature.position[1] - 1)
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[2] > 100:
							return True
				
				return False
			
			case Sensor.CreLeftBlue:
				checkpos = (creature.position[0] - 1, creature.position[1])
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[2] > 100:
							return True
				
				return False
			
			case Sensor.CreDownBlue:
				checkpos = (creature.position[0], creature.position[1] + 1)
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[2] > 100:
							return True
				
				return False
			
			case Sensor.CreRightBlue:
				checkpos = (creature.position[0] + 1, creature.position[1])
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[2] > 100:
							return True
				
				return False
			
			case Sensor.CreUpRed2:
				checkpos = (creature.position[0], creature.position[1] - 2)
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[0] > 100:
							return True
				
				return False
			
			case Sensor.CreLeftRed2:
				checkpos = (creature.position[0] - 2, creature.position[1])
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[0] > 100:
							return True
				
				return False
			
			case Sensor.CreDownRed2:
				checkpos = (creature.position[0], creature.position[1] + 2)
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[0] > 100:
							return True
				
				return False
			
			case Sensor.CreRightRed2:
				checkpos = (creature.position[0] + 2, creature.position[1])
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[0] > 100:
							return True
				
				return False
			
			case Sensor.CreUpGreen2:
				checkpos = (creature.position[0], creature.position[1] - 2)
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[1] > 100:
							return True
				
				return False
			
			case Sensor.CreLeftGreen2:
				checkpos = (creature.position[0] - 2, creature.position[1])
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[1] > 100:
							return True
				
				return False
			
			case Sensor.CreDownGreen2:
				checkpos = (creature.position[0], creature.position[1] + 2)
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[1] > 100:
							return True
				
				return False
			
			case Sensor.CreRightGreen2:
				checkpos = (creature.position[0] + 2, creature.position[1])
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[1] > 100:
							return True
				
				return False
			
			case Sensor.CreUpBlue2:
				checkpos = (creature.position[0], creature.position[1] - 2)
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[2] > 100:
							return True
				
				return False
			
			case Sensor.CreLeftBlue2:
				checkpos = (creature.position[0] - 2, creature.position[1])
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[2] > 100:
							return True
				
				return False
			
			case Sensor.CreDownBlue2:
				checkpos = (creature.position[0], creature.position[1] + 2)
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[2] > 100:
							return True
				
				return False
			
			case Sensor.CreRightBlue2:
				checkpos = (creature.position[0] + 2, creature.position[1])
				
				for c in Simulation.creatures:
					if c.position == checkpos:
						if c.colour[2] > 100:
							return True
				
				return False
	
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

