from enum         import IntEnum
from numpy        import empty, array, ndarray, ndindex, min, max, round
from numpy.random import randint
from dataclasses  import dataclass

class Vector2:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
	
	def __repr__(self):
		return f"({self.x}, {self.y})"
	
	def __str__(self):
		return f"Vector2 ({self.x}, {self.y})"
	
	def __add__(self, other):
		return Vector2(
			self.x + other.x,
			self.y + other.y
		)
	
	def __sub__(self, other):
		return Vector2(
			self.x - other.x,
			self.y - other.y
		)
	
	def __mul__(self, other):
		return Vector2(
			self.x * other.x,
			self.y * other.y
		)
	
	def __floordiv__(self, other):
		return Vector2(
			self.x // other.x,
			self.y // other.y
		)
	
	def __mod__(self, other):
		return Vector2(
			self.x % other.x,
			self.y % other.y
		)
	
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y
	
	def __ne__(self, other):
		return self.x != other.x or self.y != other.y
	
	def as_tuple(self):
		return (self.x, self.y)
	
	def coordinates(self) -> ndarray:
		return array([self.x, self.y])
	
	def in_bounds(self, minb, maxb):
		if self.x < minb.x or self.y < minb.y or self.x >= maxb.x or self.y >= maxb.y:
			return False
		
		return True

class Colour:
	def __init__(self, r, g, b):
		colour_clamp = lambda n: max([min([n, 0xFF]), 0x00])
		
		self.r = round(colour_clamp(r))
		self.g = round(colour_clamp(g))
		self.b = round(colour_clamp(b))
	
	def __repr__(self):
		return f"({self.r}, {self.g}, {self.b})"
	
	def __str__(self):
		return f"Colour ({self.r}, {self.g}, {self.b})"
	
	def __eq__(self, other):
		return self.r == other.r and self.g == other.g and self.b == other.b
	
	def __ne__(self, other):
		return self.r != other.r or self.g != other.g or self.b != other.b
	
	def as_tuple(self):
		return (self.r, self.g, self.b)

class Direction(IntEnum):
	Up    = 0
	Left  = 1
	Down  = 2
	Right = 3
	
	Size = 4
	
	def as_Vector2(self) -> Vector2:
		match self:
			case Direction.Up:    return Vector2(0, -1)
			case Direction.Left:  return Vector2(-1, 0)
			case Direction.Down:  return Vector2(0, 1)
			case Direction.Right: return Vector2(1, 0)
			
			case _: return Vector2()

class Sex(IntEnum):
	Male   = 0
	Female = 1

class Sensor(IntEnum):
	CreUp    = 0
	CreLeft  = 1
	CreDown  = 2
	CreRight = 3
	
	FreeUp    = 4
	FreeLeft  = 5
	FreeDown  = 6
	FreeRight = 7
	
	CreUpR    = 8
	CreLeftR  = 9
	CreDownR  = 10
	CreRightR = 11
	
	CreUpRed    = 12
	CreLeftRed  = 13
	CreDownRed  = 14
	CreRightRed = 15
	
	CreUpGreen    = 16
	CreLeftGreen  = 17
	CreDownGreen  = 18
	CreRightGreen = 19
	
	CreUpBlue    = 20
	CreLeftBlue  = 21
	CreDownBlue  = 22
	CreRightBlue = 23
	
	CreUpRedR    = 24
	CreLeftRedR  = 25
	CreDownRedR  = 26
	CreRightRedR = 27
	
	CreUpGreenR    = 28
	CreLeftGreenR  = 29
	CreDownGreenR  = 30
	CreRightGreenR = 31
	
	CreUpBlueR    = 32
	CreLeftBlueR  = 33
	CreDownBlueR  = 34
	CreRightBlueR = 35
	
	FoodUp    = 36
	FoodLeft  = 37
	FoodDown  = 38
	FoodRight = 39
	
	CreUpStr    = 40
	CreLeftStr  = 41
	CreDownStr  = 42
	CreRightStr = 43
	
	CreUpWk    = 44
	CreLeftWk  = 45
	CreDownWk  = 46
	CreRightWk = 47
	
	FoodUpR    = 48
	FoodLeftR  = 49
	FoodDownR  = 50
	FoodRightR = 51
	
	CreUpSmSex    = 52
	CreLeftSmSex  = 53
	CreDownSmSex  = 54
	CreRightSmSex = 55
	
	CreUpDiffSex    = 56
	CreLeftDiffSex  = 57
	CreDownDiffSex  = 58
	CreRightDiffSex = 59
	
	Alive = 60

class Behaviour(IntEnum):
	MvUp    = 0
	MvLeft  = 1
	MvDown  = 2
	MvRight = 3
	
	EatUp    = 4
	EatLeft  = 5
	EatDown  = 6
	EatRight = 7
	
	KillUp    = 8
	KillLeft  = 9
	KillDown  = 10
	KillRight = 11
	
	MateUp    = 12
	MateLeft  = 13
	MateDown  = 14
	MateRight = 15
	
	MvRnd = 16

@dataclass
class Brain:
	data = {
		Sensor.Alive: Behaviour.MvRnd,
		
		Sensor.FoodUp: Behaviour.EatUp,
		Sensor.FoodLeft: Behaviour.EatLeft,
		Sensor.FoodDown: Behaviour.EatDown,
		Sensor.FoodRight: Behaviour.EatRight,
		
		Sensor.CreUpDiffSex: Behaviour.MateUp,
		Sensor.CreLeftDiffSex: Behaviour.MateLeft,
		Sensor.CreDownDiffSex: Behaviour.MateDown,
		Sensor.CreRightDiffSex: Behaviour.MateRight,
		
		Sensor.CreUpSmSex: Behaviour.KillUp,
		Sensor.CreLeftSmSex: Behaviour.KillLeft,
		Sensor.CreDownSmSex: Behaviour.KillDown,
		Sensor.CreRightSmSex: Behaviour.KillRight,
	}

class Creature:
	def __init__(self, colour: Colour, strength: int, sex: Sex, brain: Brain = Brain()):
		self.brain    = brain
		self.colour   = colour
		self.energy   = 300
		self.strength = strength
		self.sex      = sex

SIZE = Vector2(20, 20)
GRID = empty(SIZE.as_tuple(), dtype=object)

def initialize():
	for x, y in ndindex(GRID.shape):
		if not randint(0, 101) <= 10:
			continue
		
		GRID[x, y] = Creature(
			Colour(
				randint(0x50, 0x100),
				randint(0x50, 0x100),
				randint(0x50, 0x100)
			),
			randint(0, 501),
			Sex(randint(0, 2))
		)

def _check_sorroundings(pos: Vector2,            # The position whose sorroundings are to check.
		        dir: Direction,          # Where to check.
		        alive           = True,  # Whether the creature should be dead or alive.
		        onecell         = True,  # Whether to check one cell or more.
		        creature        = True,  # Whether to look for free space or a creature.
		        colour: bytes   = None,  # The colour of the creature (b'r' -> red, b'g' -> green, b'b' -> blue).
		        strength: bytes = None,  # The strength of the creature (b's' -> stronger, b'w' -> weaker).
		        diff_sex: bool  = None   # Whether the creature should have a different sex or not (None -> it doesn't matter).
		) -> bool:
	checkdir = Direction.as_Vector2(dir)
	
	checks = 0
	
	if onecell:
		checks = 1
	
	if not checkdir.x == 0: # horizontal
		checks = SIZE.x - pos.x if not checkdir.x > 0 else pos.x
	else: # vertical
		checks = SIZE.y - pos.y if not checkdir.y > 0 else pos.y
	
	if checks < 0:
		checks = 0
	
	checkpos = pos
	
	for _ in range(checks):
		checkpos += checkdir
		
		if not checkpos.in_bounds(Vector2(), SIZE):
			continue
		
		checked = GRID[checkpos.x, checkpos.y]
		checker = GRID[pos.x, pos.y]
		
		if checked is None:
			continue
		
		if (checked.brain is None) == alive:
			continue
		
		if not colour is None:
			match colour:
				case b'r': return checked.colour.r >= 0xA0
				case b'g': return checked.colour.g >= 0xA0
				case b'b': return checked.colour.b >= 0xA0
				case _:    return False
		
		if not strength is None:
			match strength:
				case b's': return checked.strength > checker.strength
				case b'w': return checked.strength <= checker.strength
				case _:    return False
		
		if not diff_sex is None:
			match diff_sex:
				case True:  return checked.sex != checker.sex
				case False: return checked.sex == checker.sex
				case _:     return False
		
		return True
	
	if creature:
		return False
	else:
		return True
	
def _query(pos: Vector2, sensor: Sensor) -> bool:	
	match sensor:
		case Sensor.CreUp:    return _check_sorroundings(pos, Direction.Up)
		case Sensor.CreLeft:  return _check_sorroundings(pos, Direction.Left)
		case Sensor.CreDown:  return _check_sorroundings(pos, Direction.Down)
		case Sensor.CreRight: return _check_sorroundings(pos, Direction.Right)
		
		case Sensor.FreeUp:    return _check_sorroundings(pos, Direction.Up, creature = False)
		case Sensor.FreeLeft:  return _check_sorroundings(pos, Direction.Left, creature = False)
		case Sensor.FreeDown:  return _check_sorroundings(pos, Direction.Down, creature = False)
		case Sensor.FreeRight: return _check_sorroundings(pos, Direction.Right, creature = False)
		
		case Sensor.CreUpR:    return _check_sorroundings(pos, Direction.Up, onecell = False)
		case Sensor.CreLeftR:  return _check_sorroundings(pos, Direction.Left, onecell = False)
		case Sensor.CreDownR:  return _check_sorroundings(pos, Direction.Down, onecell = False)
		case Sensor.CreRightR: return _check_sorroundings(pos, Direction.Right, onecell = False)
		
		case Sensor.CreUpRed:    return _check_sorroundings(pos, Direction.Right, colour = b'r')
		case Sensor.CreLeftRed:  return _check_sorroundings(pos, Direction.Right, colour = b'r')
		case Sensor.CreDownRed:  return _check_sorroundings(pos, Direction.Right, colour = b'r')
		case Sensor.CreRightRed: return _check_sorroundings(pos, Direction.Right, colour = b'r')
		
		case Sensor.CreUpGreen:    return _check_sorroundings(pos, Direction.Right, colour = b'g')
		case Sensor.CreLeftGreen:  return _check_sorroundings(pos, Direction.Right, colour = b'g')
		case Sensor.CreDownGreen:  return _check_sorroundings(pos, Direction.Right, colour = b'g')
		case Sensor.CreRightGreen: return _check_sorroundings(pos, Direction.Right, colour = b'g')
		
		case Sensor.CreUpBlue:    return _check_sorroundings(pos, Direction.Right, colour = b'b')
		case Sensor.CreLeftBlue:  return _check_sorroundings(pos, Direction.Right, colour = b'b')
		case Sensor.CreDownBlue:  return _check_sorroundings(pos, Direction.Right, colour = b'b')
		case Sensor.CreRightBlue: return _check_sorroundings(pos, Direction.Right, colour = b'b')
		
		case Sensor.CreUpRedR:    return _check_sorroundings(pos, Direction.Right, colour = b'r', onecell = False)
		case Sensor.CreLeftRedR:  return _check_sorroundings(pos, Direction.Right, colour = b'r', onecell = False)
		case Sensor.CreDownRedR:  return _check_sorroundings(pos, Direction.Right, colour = b'r', onecell = False)
		case Sensor.CreRightRedR: return _check_sorroundings(pos, Direction.Right, colour = b'r', onecell = False)
		
		case Sensor.CreUpGreenR:    return _check_sorroundings(pos, Direction.Right, colour = b'g', onecell = False)
		case Sensor.CreLeftGreenR:  return _check_sorroundings(pos, Direction.Right, colour = b'g', onecell = False)
		case Sensor.CreDownGreenR:  return _check_sorroundings(pos, Direction.Right, colour = b'g', onecell = False)
		case Sensor.CreRightGreenR: return _check_sorroundings(pos, Direction.Right, colour = b'g', onecell = False)
		
		case Sensor.CreUpBlueR:    return _check_sorroundings(pos, Direction.Right, colour = b'b', onecell = False)
		case Sensor.CreLeftBlueR:  return _check_sorroundings(pos, Direction.Right, colour = b'b', onecell = False)
		case Sensor.CreDownBlueR:  return _check_sorroundings(pos, Direction.Right, colour = b'b', onecell = False)
		case Sensor.CreRightBlueR: return _check_sorroundings(pos, Direction.Right, colour = b'b', onecell = False)
		
		case Sensor.FoodUp:    return _check_sorroundings(pos, Direction.Up, alive = False)
		case Sensor.FoodLeft:  return _check_sorroundings(pos, Direction.Left, alive = False)
		case Sensor.FoodDown:  return _check_sorroundings(pos, Direction.Down, alive = False)
		case Sensor.FoodRight: return _check_sorroundings(pos, Direction.Right, alive = False)
		
		case Sensor.CreUpStr:    return _check_sorroundings(pos, Direction.Up, strength = b's')
		case Sensor.CreLeftStr:  return _check_sorroundings(pos, Direction.Left, strength = b's')
		case Sensor.CreDownStr:  return _check_sorroundings(pos, Direction.Down, strength = b's')
		case Sensor.CreRightStr: return _check_sorroundings(pos, Direction.Right, strength = b's')
		
		case Sensor.CreUpWk:    return _check_sorroundings(pos, Direction.Up, strength = b'w')
		case Sensor.CreLeftWk:  return _check_sorroundings(pos, Direction.Left, strength = b'w')
		case Sensor.CreDownWk:  return _check_sorroundings(pos, Direction.Down, strength = b'w')
		case Sensor.CreRightWk: return _check_sorroundings(pos, Direction.Right, strength = b'w')
		
		case Sensor.FoodUpR:    return _check_sorroundings(pos, Direction.Up, alive = False, onecell = False)
		case Sensor.FoodLeftR:  return _check_sorroundings(pos, Direction.Left, alive = False, onecell = False)
		case Sensor.FoodDownR:  return _check_sorroundings(pos, Direction.Down, alive = False, onecell = False)
		case Sensor.FoodRightR: return _check_sorroundings(pos, Direction.Right, alive = False, onecell = False)
		
		case Sensor.CreUpSmSex:    return _check_sorroundings(pos, Direction.Up, diff_sex = False)
		case Sensor.CreLeftSmSex:  return _check_sorroundings(pos, Direction.Left, diff_sex = False)
		case Sensor.CreDownSmSex:  return _check_sorroundings(pos, Direction.Down, diff_sex = False)
		case Sensor.CreRightSmSex: return _check_sorroundings(pos, Direction.Right, diff_sex = False)
		
		case Sensor.CreUpDiffSex:    return _check_sorroundings(pos, Direction.Up, diff_sex = True)
		case Sensor.CreLeftDiffSex:  return _check_sorroundings(pos, Direction.Left, diff_sex = True)
		case Sensor.CreDownDiffSex:  return _check_sorroundings(pos, Direction.Down, diff_sex = True)
		case Sensor.CreRightDiffSex: return _check_sorroundings(pos, Direction.Right, diff_sex = True)
		
		case Sensor.Alive: return True
		
		case _: return False

def _move(pos: Vector2, dir: Direction) -> bool:
	checkpos = pos + Direction.as_Vector2(dir)
	
	for n, c in enumerate(checkpos.coordinates()):
		if c < 0 or c >= SIZE.coordinates()[n]:
			return False
	
	if not GRID[checkpos.x, checkpos.y] is None:
		return False
	
	GRID[checkpos.x, checkpos.y] = GRID[pos.x, pos.y]
	GRID[pos.x, pos.y] = None
	
	return True

def _eat(pos: Vector2, dir: Direction) -> bool:
	checkpos = pos + Direction.as_Vector2(dir)
	
	if GRID[checkpos.x, checkpos.y] is None:
		return False
	
	if not GRID[checkpos.x, checkpos.y].brain is None:
		return False
	
	GRID[checkpos.x, checkpos.y] = None
	GRID[pos.x, pos.y].energy += 200
	
	return True

def _turn_to_food(pos: Vector2):
	if GRID[pos.x, pos.y] is None:
		return
	
	GRID[pos.x, pos.y].brain  = None
	GRID[pos.x, pos.y].colour = Colour(0x40, 0x00, 0x00)

def _kill(pos: Vector2, dir: Direction) -> bool:
	checkpos = pos + Direction.as_Vector2(dir)
	
	if GRID[checkpos.x, checkpos.y] is None:
		return False
	
	if not GRID[checkpos.x, checkpos.y].brain is None:
		return False
	
	if GRID[checkpos.x, checkpos.y].strength > GRID[pos.x, pos.y].strength:
		_turn_to_food(pos)
		return True
	else:
		_turn_to_food(checkpos)
		return True

def _mate(pos: Vector2, dir: Direction) -> bool:
	checkpos = pos + Direction.as_Vector2(dir)
	
	# Incel.
	if GRID[checkpos.x, checkpos.y] is None:
		return False
	
	# Sick illegal shit.
	if GRID[checkpos.x, checkpos.y].brain is None:
		return False
	
	# Nothing against it, it just doesn't work.
	if GRID[checkpos.x, checkpos.y].sex == GRID[pos.x, pos.y].sex:
		return False
	
	for d in Direction:
		dirvec = pos + Direction.as_Vector2(d)
		
		if not dirvec.in_bounds(Vector2(), SIZE):
			continue
		
		if GRID[dirvec.x, dirvec.y] is None:
			GRID[dirvec.x, dirvec.y] = Creature(
				Colour(
					randint(
						min([
							GRID[pos.x, pos.y].colour.r,
							GRID[checkpos.x, checkpos.y].colour.r
						]),
						max([
							GRID[pos.x, pos.y].colour.r,
							GRID[checkpos.x, checkpos.y].colour.r
						]) + 1
					),
					randint(
						min([
							GRID[pos.x, pos.y].colour.g,
							GRID[checkpos.x, checkpos.y].colour.g
						]),
						max([
							GRID[pos.x, pos.y].colour.g,
							GRID[checkpos.x, checkpos.y].colour.g
						]) + 1
					),
					randint(
						min([
							GRID[pos.x, pos.y].colour.b,
							GRID[checkpos.x, checkpos.y].colour.b
						]),
						max([
							GRID[pos.x, pos.y].colour.b,
							GRID[checkpos.x, checkpos.y].colour.b
						]) + 1
					)
				),
				randint(
					min([
						GRID[pos.x, pos.y].strength,
						GRID[checkpos.x, checkpos.y].strength
					]),
					max([
						GRID[pos.x, pos.y].strength,
						GRID[checkpos.x, checkpos.y].strength
					]) + 1
				),
				Sex(randint(0, 2))
			)
			
			return True
	
	return False

def _request(pos: Vector2, behaviour: Behaviour) -> bool:
	match behaviour:
		case Behaviour.MvUp:    return _move(pos, Direction.Up)
		case Behaviour.MvLeft:  return _move(pos, Direction.Left)
		case Behaviour.MvDown:  return _move(pos, Direction.Down)
		case Behaviour.MvRight: return _move(pos, Direction.Right)
		
		case Behaviour.EatUp:    return _eat(pos, Direction.Up)
		case Behaviour.EatLeft:  return _eat(pos, Direction.Left)
		case Behaviour.EatDown:  return _eat(pos, Direction.Down)
		case Behaviour.EatRight: return _eat(pos, Direction.Right)
		
		case Behaviour.KillUp:    return _kill(pos, Direction.Up)
		case Behaviour.KillLeft:  return _kill(pos, Direction.Left)
		case Behaviour.KillDown:  return _kill(pos, Direction.Down)
		case Behaviour.KillRight: return _kill(pos, Direction.Right)
		
		case Behaviour.MateUp:    return _mate(pos, Direction.Up)
		case Behaviour.MateLeft:  return _mate(pos, Direction.Left)
		case Behaviour.MateDown:  return _mate(pos, Direction.Down)
		case Behaviour.MateRight: return _mate(pos, Direction.Right)
		
		case Behaviour.MvRnd: return _move(pos, randint(0, Direction.Size))

def update():
	for x, y in ndindex(GRID.shape):
		creature = GRID[x, y]
		
		if creature == None:
			continue
		
		if creature.brain == None:
			continue
		
		for sensor, behaviour in creature.brain.data.items():
			creature.energy -= 1
			
			if creature.energy == 0:
				_turn_to_food(Vector2(x, y))
			
			if _query(Vector2(x, y), sensor):
				if _request(Vector2(x, y), behaviour):
					break

