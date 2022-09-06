if not __name__ == "__main__":
	raise ImportError("Do not import the Decrolution front-end as a library!")

import pygame.display
import pygame.time
import pygame.event
import sys
import decrolution

delta_time: float = 0
scale: int = 8

pygame.display.init()
clock = pygame.time.Clock()

pygame.display.set_mode((800, 600))
pygame.display.set_caption("Decrolution")
# pygame.display.set_icon("")

decrolution.Simulation.initialize()

while True:
	frame_start = pygame.time.get_ticks()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	
	decrolution.Simulation.update()
	
	pygame.display.get_surface().fill((0x00, 0x00, 0x00))
	
	for creature in decrolution.Simulation.creatures:
		pygame.draw.rect(
			pygame.display.get_surface(),
			(0xFF, 0xFF, 0xFF),
			(creature.position[0] * scale, creature.position[1] * scale, scale, scale)
		)
	
	pygame.display.flip()
	
	delta_time = clock.tick() / 1000

