if not __name__ == "__main__":
	raise ImportError("Do not import Decrolution as a library!")

import pygame.display
import pygame.time
import pygame.event
import sys

delta_time: float = 0

pygame.display.init()
clock = pygame.time.Clock()

pygame.display.set_mode((800, 600))
pygame.display.set_caption("Decrolution")
# pygame.display.set_icon("")

while True:
	frame_start = pygame.time.get_ticks()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	
	print(delta_time)
	
	pygame.display.get_surface().fill((0x00, 0x00, 0x00))
	
	pygame.display.flip()
	
	delta_time = clock.tick() / 1000

