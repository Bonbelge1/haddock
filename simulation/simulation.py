import pygame
import random
# from random import randrange, uniform
import time
# from time import delay
import math
# from math import sin, cos, radian, e
from pygame.locals import *

# Class for boat
class Boat:
	def __init__(self):
		self.image = pygame.image.load("sprite.png")
		self.color = (255, 0, 0)
		self.weight = 3
		self.pos = [100, 100]
		self.speed = 2
		self.theta = 0
		
# Class for tiles
class Tiles:
	def __init__(self):
		self.color = (0, 0, 255)
		self.currentStr = 0.2
		self.currentDir = random.randrange(0, 360) 
		self.elementType = "water"

# Function returning tile coordinate where the boat is 
def zoneMap(position, map_x, map_y, screen_width, screen_height):
	return [int(position[0] * map_x / screen_width), int(position[1] * map_y / screen_height)]

# Function that makes an int matrix of a text file
def matrix(file):
	contents = open(file).read()
	return [list(map(int, el.split())) for el in contents.split('\n')]


#-----------------------------------------------------------------------------------------------	
   
def main():
	
	# Colors
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	BLUE = (0, 0, 255)
	
	# Creation of the map
	
	mat = matrix('lake.txt')
	
	map_x = len(mat[0])
	map_y = len(mat)
	gameMap = [[Tiles() for i in range(map_x)] for j in range(map_y)]
	for j in range(map_y):
		for i in range(map_x):
			gameMap[j][i].color = (0, 255 * mat[j][i], 255)

	# Creation of the window
	pygame.init()
	tileSize = 20
	screen_width = map_x * tileSize
	screen_height = map_y * tileSize
	window = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption("Haddock")

	# Creation of the boat
	boat = Boat()

	# Surface
	DISPLAYSURF = pygame.display.set_mode()

	# Infinite loop recursivly
	while True:
		
		# Draw Tiles
		for i in range(map_x):
			for j in range(map_y):
				pygame.draw.rect(DISPLAYSURF, gameMap[j][i].color, (i * screen_width / map_x, j * screen_width / map_x, screen_width / map_x - 0, screen_height / map_y - 0))
					
		# Draw Boat
		posTemp = (int(boat.pos[0]), int(boat.pos[1]))
		#pygame.sprite.Group.draw(DISPLAYSURF, boat.image, posTemp)
		pygame.draw.circle(DISPLAYSURF, boat.color, posTemp, int(boat.weight))

			
		# Horizontal border verification 
		if not (boat.weight <= int(boat.pos[0] + boat.speed * math.cos(math.radians(boat.theta))) <= screen_width - boat.weight):
			boat.theta = 180 - boat.theta
		
		# Vertical border verification
		if not (boat.weight <= int(boat.pos[1] + boat.speed * math.sin(math.radians(boat.theta))) <= screen_height - boat.weight):
			boat.theta = 360 - boat.theta

		# Calculate new position
		boat.pos = (boat.pos[0] + boat.speed * math.cos(math.radians(boat.theta)), boat.pos[1] + boat.speed * math.sin(math.radians(boat.theta)))
		gps = zoneMap(boat.pos, map_x, map_y, screen_width, screen_height)
			

		# Update the window
		pygame.display.flip()
		DISPLAYSURF.fill(BLACK)
		
		# Tic toc
		pygame.time.delay(1000) 
	
#-----------------------------------------------------------------------------------------------

	# Not working quit event				       
	for event in pygame.event.get():
		if (event.type == QUIT):
			pygame.quit()
			sys.exit()

if __name__ == '__main__':
	main() 