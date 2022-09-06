if not __name__ == "__main__":
	raise ImportError("Do not import the Decrolution front-end as a library!")

import pygame.display
import pygame.time
import pygame.event
import sys
import decrolution

scale: int = 8

pygame.display.init()

pygame.display.set_mode((800, 600))
pygame.display.set_caption("Decrolution")
# pygame.display.set_icon("")

decrolution.Simulation.initialize()

counter = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	
	if counter == 3000:
		counter = 0
		decrolution.Simulation.update()
	
	counter += 1
	
	pygame.display.get_surface().fill((0x00, 0x00, 0x00))
	
	for creature in decrolution.Simulation.creatures:
		pygame.draw.rect(
			pygame.display.get_surface(),
			creature.colour,
			(creature.position[0] * scale, creature.position[1] * scale, scale, scale)
		)
	
	pygame.display.flip()

