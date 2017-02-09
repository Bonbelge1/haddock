import pygame
import random
# from random import randrange, uniform
import time
# from time import delay
from math import atan2, degrees, radians, sin, cos
# from math import sin, cos, radian
from pygame.locals import *

# Class for boat
class Boat:
	def __init__(self):
		self.image = pygame.image.load("sprite.png")
		self.color = (255, 0, 0)
		self.weight = 3
		self.pos = [400, 600]
		self.speed = 2
		self.theta = 180  #Trigonometry direction
		
# Class for tiles
class Tiles:
	def __init__(self):
		self.color = (0, 0, 255)
		self.currentStr = 0.2
		self.currentDir = random.randrange(0, 360) 
		self.elementType = "water"

# Class for gps points
class gpsPoint:
	def __init__(self):
		self.color = (0, 0, 0)
		self.pos = [10, 10]

# Function returning tile coordinate where the boat is 
def zoneMap(position, map_x, map_y, s_width, s_height):
	return (int(position[0] * map_x / s_width), int(position[1] * map_y / s_height))

# Function that makes an int matrix of a text file
def matrix(file):
	contents = open(file).read()
	return [list(map(int, el.split())) for el in contents.split('\n')]

# Function that calculate angle between two points
def autoAngle(point1, point2):
	print(degrees(atan2(point2[1] - point1[1], point2[0] - point1[0])))
	return degrees(atan2(point2[1] - point1[1], point2[0] - point1[0]))



#-----------------------------------------------------------------------------------------------	
   
def main():
	
	# Colors
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	BLUE = (0, 0, 255)
	
	# Creation of the map
	matMap = matrix('lake.txt')
	map_x = len(matMap[0])
	map_y = len(matMap)
	gameMap = [[Tiles() for i in range(map_x)] for j in range(map_y)]
	for j in range(map_y):
		for i in range(map_x):
			gameMap[j][i].color = (0, 255 * matMap[j][i], 255)

	# Creation of the window
	pygame.init()
	tileSize = 20
	s_width = map_x * tileSize
	s_height = map_y * tileSize
	window = pygame.display.set_mode((s_width, s_height))
	pygame.display.set_caption("Haddock")

	# Creation of the boat
	boat = Boat()

	# Creation of gps objects
	matGPS = matrix("gps.txt")
	gps = [gpsPoint() for i in range(len(matGPS))]
	for index, ob in enumerate(gps):
		ob.pos = matGPS[index]


	# Surface
	DISPLAYSURF = pygame.display.set_mode()

	# Infinite loop recursivly
	while True:
		
		# Draw Tiles
		for i in range(map_x):
			for j in range(map_y):
				tup = (i * s_width / map_x, j * s_width / map_x, s_width / map_x - 0, s_height / map_y - 0)
				pygame.draw.rect(DISPLAYSURF, gameMap[j][i].color, tup)
		
		#Draw GPS Points
		for ob in gps:
			pygame.draw.circle(DISPLAYSURF, ob.color, ob.pos, 2)


		# Draw Boat
		posTemp = (int(boat.pos[0]), int(boat.pos[1]))
		#pygame.sprite.Group.draw(DISPLAYSURF, boat.image, posTemp)
		pygame.draw.circle(DISPLAYSURF, boat.color, posTemp, int(boat.weight))
	
		# Horizontal border verification (not up to date)
		#if not (boat.weight <= int(boat.pos[0] + boat.speed * cos(radians(boat.theta))) <= s_width - boat.weight):
		#	boat.theta = 180 - boat.theta
		
		# Vertical border verification (not up to date)
		#if not (boat.weight <= int(boat.pos[1] + boat.speed * sin(radians(boat.theta))) <= s_height - boat.weight):
		#	boat.theta = 360 - boat.theta

		# Calculate new position
		boat.theta = autoAngle(boat.pos, gps[0].pos)
		boat.pos = (boat.pos[0] + boat.speed * cos(radians(boat.theta)), boat.pos[1] + boat.speed * sin(radians(boat.theta)))
		# gps = zoneMap(boat.pos, map_x, map_y, s_width, s_height)
			

		# Update the window
		pygame.display.flip()
		DISPLAYSURF.fill(BLACK)
		
		# Tic toc
		pygame.time.delay(30) 
	
#-----------------------------------------------------------------------------------------------

	# Not working quit event				       
	for event in pygame.event.get():
		if (event.type == QUIT):
			pygame.quit()
			sys.exit()

if __name__ == '__main__':
	main() 