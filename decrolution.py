import enum
import random

random.seed()

class Vector2i:
	def __init__(self, x: int = 0, y: int = 0):
		self.x: int = x
		self.y: int = y
	
	def __str__(self):
		return f"({self.x}, {self.y})"
	
	def __add__(self, other):
		return Vector2i(self.x + other.x, self.y + other.y)
	
	def __sub__(self, other):
		return Vector2i(self.x - other.x, self.y - other.y)
	
	def __mul__(self, other):
		return Vector2i(self.x * other.x, self.y * other.y)
	
	def __floordiv__(self, other):
		return Vector2i(self.x // other.x, self.y // other.y)
	
	def __mod__(self, other):
		return Vector2i(self.x % other.x, self.y % other.y)
	
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y
	
	def __ne__(self, other):
		return self.x != other.x or self.y != other.y
	
	def coordinates(self):
		return [self.x, self.y]

class Colour:
	def __init__(self, r: int = 0x00, g: int = 0x00, b: int = 0x00):
		colour_clamp = lambda n: max([min([n, 0xFF]), 0x00])
		
		self.r: int = colour_clamp(r)
		self.g: int = colour_clamp(g)
		self.b: int = colour_clamp(b)
	
	def __str__(self):
		return f"({self.r}, {self.g}, {self.b})"
	
	def __eq__(self, other):
		return self.r == other.r and self.g == other.g and self.b == other.b
	
	def __ne__(self, other):
		return self.r != other.r or self.g != other.g or self.b != other.b
	
	def as_tuple(self):
		return (self.r, self.g, self.b)

class Direction(enum.Enum):
	Up = 0
	Left = 1
	Down = 2
	Right = 3
	
	def to_Vector2i(dir) -> Vector2i:
		match dir:
			case Direction.Up: return Vector2i(0, -1)
			case Direction.Left: return Vector2i(-1, 0)
			case Direction.Down: return Vector2i(0, 1)
			case Direction.Right: return Vector2i(1, 0)

class Sensor(enum.Enum):
	CreUp = 0
	CreLeft = 1
	CreDown = 2
	CreRight = 3
	
	FreeUp = 4
	FreeLeft = 5
	FreeDown = 6
	FreeRight = 7
	
	CreUpR = 8
	CreLeftR = 9
	CreDownR = 10
	CreRightR = 11
	
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
	
	CreUpRedR = 24
	CreLeftRedR = 25
	CreDownRedR = 26
	CreRightRedR = 27
	
	CreUpGreenR = 28
	CreLeftGreenR = 29
	CreDownGreenR = 30
	CreRightGreenR = 31
	
	CreUpBlueR = 32
	CreLeftBlueR = 33
	CreDownBlueR = 34
	CreRightBlueR = 35
	
	FoodUp = 36
	FoodLeft = 37
	FoodDown = 38
	FoodRight = 39
	
	CreUpStr = 40
	CreLeftStr = 41
	CreDownStr = 42
	CreRightStr = 43
	
	CreUpWk = 44
	CreLeftWk = 45
	CreDownWk = 46
	CreRightWk = 47
	
	FoodUpR = 48
	FoodLeftR = 49
	FoodDownR = 50
	FoodRightR = 51

class Behaviour(enum.Enum):
	MvUp = 0
	MvLeft = 1
	MvDown = 2
	MvRight = 3
	
	EatUp = 4
	EatLeft = 5
	EatDown = 6
	EatRight = 7
	
	KillUp = 8
	KillLeft = 9
	KillDown = 10
	KillRight = 11

class Brain:
	def __init__(self):
		self.data: dict[Sensor, Behaviour] = {
			Sensor.CreUpR: Behaviour.MvUp,
			Sensor.CreLeftR: Behaviour.MvLeft,
			Sensor.CreDownR: Behaviour.MvDown,
			Sensor.CreRightR: Behaviour.MvRight,
			
			Sensor.FoodUpR: Behaviour.MvUp,
			Sensor.FoodLeftR: Behaviour.MvLeft,
			Sensor.FoodDownR: Behaviour.MvDown,
			Sensor.FoodRightR: Behaviour.MvRight,
			
			Sensor.FoodUp: Behaviour.EatUp,
			Sensor.FoodLeft: Behaviour.EatLeft,
			Sensor.FoodDown: Behaviour.EatDown,
			Sensor.FoodRight: Behaviour.EatRight,
			
			Sensor.CreUpWk: Behaviour.KillUp,
			Sensor.CreLeftWk: Behaviour.KillLeft,
			Sensor.CreDownWk: Behaviour.KillDown,
			Sensor.CreRightWk: Behaviour.KillRight,
		}

class Creature:
	def __init__(self, position: Vector2i, colour: Colour, strength: int,
			brain: Brain = Brain()):
		self.position: Vector2i = position
		self.brain: Brain = brain
		self.request: Behaviour = None
		self.colour: Colour = colour
		self.energy: int = 300
		self.strength: int = strength
	
	def update(self):
		if self.brain == None:
			return
		
		for sensor, behaviour in self.brain.data.items():
			self.energy -= 1
			
			if self.energy == 0:
				self.die()
				
			if Simulation.query(self, sensor):
				if Simulation.request(self, behaviour):
					break
	
	def die(self):
		self.brain = None
		self.request = None
		self.colour = Colour(0x40, 0x00, 0x00)

class Simulation:
	creatures: list[Creature] = []
	size: int = 20
	
	def initialize():
		for i in range(Simulation.size):
			for j in range(Simulation.size):
				if random.randrange(0, 101) <= 10:
					Simulation.creatures.append(Creature(
						Vector2i(i, j),
						Colour(
							random.randrange(0x50, 0x100),
							random.randrange(0x50, 0x100),
							random.randrange(0x50, 0x100)
						),
						random.randrange(0, 501)
					))
	
	def update():
		for creature in Simulation.creatures:
			creature.update()
	
	def query(creature: Creature, sensor: Sensor) -> bool:
		def check_sorroundings(direction: Direction, alive: bool = True,
				       recursive = False, free_space: bool = False,
				       colour: bytes = None, strength: bytes = None) -> bool:
			checkdir: Vector2i = Direction.to_Vector2i(direction)
			
			def get_number_of_checks() -> int:
				if not recursive:
					return 1
				
				if not checkdir.x == 0: # horizontal
					if checkdir.x > 0:
						return Simulation.size - creature.position.x
					else:
						return creature.position.x
				else: # vertical
					if checkdir.y > 0:
						return Simulation.size - creature.position.y
					else:
						return creature.position.y
			
			checks = get_number_of_checks()
			del get_number_of_checks
			
			checkpos: Vector2i = creature.position
			
			for _ in range(checks):
				checkpos += checkdir
			
				for c in Simulation.creatures:
					if not c.position == checkpos: continue
					if free_space: return False
					if (c.brain is None) == alive: continue
					
					if not colour is None:
						match colour:
							case b'r': return c.colour.r >= 0xA0
							case b'g': return c.colour.g >= 0xA0
							case b'b': return c.colour.b >= 0xA0
					
					if not strength is None:
						match strength:
							case b's': return c.strength > creature.strength
							case b'w': return c.strength <= creature.strength
					
					return True
			
			if free_space:
				return True
			else:
				return False
	
		match sensor:
			case Sensor.CreUp: return check_sorroundings(Direction.Up)
			case Sensor.CreLeft: return check_sorroundings(Direction.Left)
			case Sensor.CreDown: return check_sorroundings(Direction.Down)
			case Sensor.CreRight: return check_sorroundings(Direction.Right)
			
			case Sensor.FreeUp: return check_sorroundings(Direction.Up, free_space = True)
			case Sensor.FreeLeft: return check_sorroundings(Direction.Left, free_space = True)
			case Sensor.FreeDown: return check_sorroundings(Direction.Down, free_space = True)
			case Sensor.FreeRight: return check_sorroundings(Direction.Right, free_space = True)
			
			case Sensor.CreUpR: return check_sorroundings(Direction.Up, recursive = True)
			case Sensor.CreLeftR: return check_sorroundings(Direction.Left, recursive = True)
			case Sensor.CreDownR: return check_sorroundings(Direction.Down, recursive = True)
			case Sensor.CreRightR: return check_sorroundings(Direction.Right, recursive = True)
			
			case Sensor.CreUpRed: return check_sorroundings(Direction.Right, colour = b'r')
			case Sensor.CreLeftRed: return check_sorroundings(Direction.Right, colour = b'r')
			case Sensor.CreDownRed: return check_sorroundings(Direction.Right, colour = b'r')
			case Sensor.CreRightRed: return check_sorroundings(Direction.Right, colour = b'r')
			
			case Sensor.CreUpGreen: return check_sorroundings(Direction.Right, colour = b'g')
			case Sensor.CreLeftGreen: return check_sorroundings(Direction.Right, colour = b'g')
			case Sensor.CreDownGreen: return check_sorroundings(Direction.Right, colour = b'g')
			case Sensor.CreRightGreen: return check_sorroundings(Direction.Right, colour = b'g')
			
			case Sensor.CreUpBlue: return check_sorroundings(Direction.Right, colour = b'b')
			case Sensor.CreLeftBlue: return check_sorroundings(Direction.Right, colour = b'b')
			case Sensor.CreDownBlue: return check_sorroundings(Direction.Right, colour = b'b')
			case Sensor.CreRightBlue: return check_sorroundings(Direction.Right, colour = b'b')
			
			case Sensor.CreUpRedR: return check_sorroundings(Direction.Right, colour = b'r', recursive = True)
			case Sensor.CreLeftRedR: return check_sorroundings(Direction.Right, colour = b'r', recursive = True)
			case Sensor.CreDownRedR: return check_sorroundings(Direction.Right, colour = b'r', recursive = True)
			case Sensor.CreRightRedR: return check_sorroundings(Direction.Right, colour = b'r', recursive = True)
			
			case Sensor.CreUpGreenR: return check_sorroundings(Direction.Right, colour = b'g', recursive = True)
			case Sensor.CreLeftGreenR: return check_sorroundings(Direction.Right, colour = b'g', recursive = True)
			case Sensor.CreDownGreenR: return check_sorroundings(Direction.Right, colour = b'g', recursive = True)
			case Sensor.CreRightGreenR: return check_sorroundings(Direction.Right, colour = b'g', recursive = True)
			
			case Sensor.CreUpBlueR: return check_sorroundings(Direction.Right, colour = b'b', recursive = True)
			case Sensor.CreLeftBlueR: return check_sorroundings(Direction.Right, colour = b'b', recursive = True)
			case Sensor.CreDownBlueR: return check_sorroundings(Direction.Right, colour = b'b', recursive = True)
			case Sensor.CreRightBlueR: return check_sorroundings(Direction.Right, colour = b'b', recursive = True)
			
			case Sensor.FoodUp: return check_sorroundings(Direction.Up, alive = False)
			case Sensor.FoodLeft: return check_sorroundings(Direction.Left, alive = False)
			case Sensor.FoodDown: return check_sorroundings(Direction.Down, alive = False)
			case Sensor.FoodRight: return check_sorroundings(Direction.Right, alive = False)
			
			case Sensor.CreUpStr: return check_sorroundings(Direction.Up, strength = b's')
			case Sensor.CreLeftStr: return check_sorroundings(Direction.Left, strength = b's')
			case Sensor.CreDownStr: return check_sorroundings(Direction.Down, strength = b's')
			case Sensor.CreRightStr: return check_sorroundings(Direction.Right, strength = b's')
			
			case Sensor.CreUpWk: return check_sorroundings(Direction.Up, strength = b'w')
			case Sensor.CreLeftWk: return check_sorroundings(Direction.Left, strength = b'w')
			case Sensor.CreDownWk: return check_sorroundings(Direction.Down, strength = b'w')
			case Sensor.CreRightWk: return check_sorroundings(Direction.Right, strength = b'w')
			
			case Sensor.FoodUpR: return check_sorroundings(Direction.Up, alive = False, recursive = True)
			case Sensor.FoodLeftR: return check_sorroundings(Direction.Left, alive = False, recursive = True)
			case Sensor.FoodDownR: return check_sorroundings(Direction.Down, alive = False, recursive = True)
			case Sensor.FoodRightR: return check_sorroundings(Direction.Right, alive = False, recursive = True)
	
	def request(creature: Creature, behaviour: Behaviour) -> bool:
		def move(dir: Direction) -> bool:
			checkpos = creature.position + Direction.to_Vector2i(dir)
			
			for c in checkpos.coordinates():
				if c < 0 or c > Simulation.size:
					return False
			
			for c in Simulation.creatures:
				if c.position == checkpos:
					return False
			
			creature.position = checkpos
			
			return True
		
		def eat(dir: Direction) -> bool:
			checkpos = creature.position + Direction.to_Vector2i(dir)
			
			for c in Simulation.creatures:
				if c.position == checkpos and c.brain is None:
					Simulation.creatures.remove(c)
					creature.energy += 200
					return True
			
			return False
		
		def kill(dir: Direction) -> bool:
			checkpos = creature.position + Direction.to_Vector2i(dir)
			
			for c in Simulation.creatures:
				if c.position == checkpos and not c.brain is None:
					if c.strength > creature.strength:
						creature.die()
						return True
					else:
						c.die()
						return True
			
			return False
	
		match behaviour:
			case Behaviour.MvUp: return move(Direction.Up)
			case Behaviour.MvLeft: return move(Direction.Left)
			case Behaviour.MvDown: return move(Direction.Down)
			case Behaviour.MvRight: return move(Direction.Right)
			
			case Behaviour.EatUp: return eat(Direction.Up)
			case Behaviour.EatLeft: return eat(Direction.Left)
			case Behaviour.EatDown: return eat(Direction.Down)
			case Behaviour.EatRight: return eat(Direction.Right)
			
			case Behaviour.KillUp: return kill(Direction.Up)
			case Behaviour.KillLeft: return kill(Direction.Left)
			case Behaviour.KillDown: return kill(Direction.Down)
			case Behaviour.KillRight: return kill(Direction.Right)

