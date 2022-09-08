if not __name__ == "__main__":
	raise ImportError("Do not import the Decrolution front-end as a library!")

from pygame      import display, event, draw, locals
from sys         import exit
from decrolution import initialize, update, GRID
from numpy       import ndindex

scale: int = 8

display.init()

display.set_mode((800, 600))
display.set_caption("Decrolution")
#display.set_icon("")

initialize()

counter = 0

while True:
	for e in event.get():
		if e.type == locals.QUIT:
			exit()
	
	if counter == 100:
		counter = 0
		update()
	
	counter += 1
	
	display.get_surface().fill((0x00, 0x00, 0x00))
	
	for x, y in ndindex(GRID.shape):
		cell = GRID[x, y]
		
		if cell is None:
			continue
		
		draw.rect(
			display.get_surface(),
			cell.colour.as_tuple(),
			(x * scale, y * scale, scale, scale)
		)
	
	display.flip()

