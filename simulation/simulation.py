import pygame
import random
# from random import randrange, uniform
import time
# from time import delay
from math import atan2, degrees, radians, sin, cos
# from math import sin, cos, radian
from pygame.locals import *

class Boat:
	"""Class for boat"""
	def __init__(self):
		#self.image = pygame.image.load("sprite.png")
		self.color = (0, 0, 0)
		self.weight = 3
		self.pos = [400, 600]
		self.speed = 2
		self.theta = 180  #Trigonometry direction
		
class Tiles:
	"""Class for tiles"""
	def __init__(self):
		self.color = (0, 0, 0)
		self.currentStr = 0.2
		self.currentDir = 0 #random.randrange(0, 360) 
		self.elementType = "water"

class gpsPoint:
	"""Class for gps points"""
	def __init__(self):
		self.color = (0, 0, 0)
		self.pos = [10, 10]
		self.weight = 3

class Map:
	"""Class for the map"""
	def __init__(self):
		self.xTiles = 0
		self.yTiles = 0
		self.ratio = 2
		self.tileSize = 10
		self.xPixels = 0
		self.yPixels = 0

def zoneMap(position, map):
	"""Return tile coordinate where the boat is"""
	return (int(position[0] * map.xTiles / map.xPixels), int(position[1] * map.yTiles / map.yPixels))

def matrix(file):
	"""Return an int matrix of a text file"""
	contents = open(file).read()
	return [list(map(int, el.split())) for el in contents.split('\n')]

def angle2P(point1, point2):
	"""Returns angle between two points"""
	return degrees(atan2(point2[1] - point1[1], point2[0] - point1[0]))

def isInRadius(boat, gps, rad):
	"""Return if gps is in radius of a point"""
	return (((gps[0] - boat[0]) ** 2 + (gps[1] - boat[1]) ** 2) ** 0.5 < rad)

def drawPts(gps, disp):
	"""Drawing the points"""
	for ob in gps:
		pygame.draw.circle(disp, ob.color, ob.pos, ob.weight)	

def drawBoat(boat, disp):
	"""Drawing the boat"""
	tempPos = (int(boat.pos[0]), int(boat.pos[1]))
	pygame.draw.circle(disp, boat.color, tempPos, boat.weight)

def drawTiles(gameMap, map, disp):
	"""Drawing the tiles"""
	for i in range(map.xTiles):
		for j in range(map.yTiles):
			tup = (i * map.xPixels / map.xTiles, j * map.xPixels / map.xTiles, map.xPixels / map.xTiles, map.yPixels / map.yTiles)
			pygame.draw.rect(disp, gameMap[j][i].color, tup)

def drawTarget(target, disp):
	"""Drawing the target"""
	pygame.draw.circle(disp, target.color, target.pos, target.weight)

def calculateNewBoatPos(boat, target):
	"""Calculate the new position of the boat"""
	boat.theta = angle2P(boat.pos, target.pos)
	boat.pos = (boat.pos[0] + boat.speed * cos(radians(boat.theta)), boat.pos[1] + boat.speed * sin(radians(boat.theta)))
	
	#zoneMap(boat.pos, map.xTiles, map.yTiles, width, height)
	#boat.pos = (boat.pos[0] + .currentStr * cos(radians(.currentDir)), boat.pos[1] + .currentStr * sin(radians(.currentDir)))

def checkForQuit():
	"""Quit the simulation"""
	if pygame.event.get(QUIT): # get all the QUIT events
		terminate()
	elif pygame.event.get(KEYUP): # get all the KEYUP events
		if event.key == K_ESCAPE:
			terminate()

def terminate():
	"""Execution to quit"""
	pygame.quit()
	sys.exit()

#--------------------------

def resistance(speed)
	wb = open_workbook('Resistance.xlsx')
	int col = 1
	while sheet.cell((1, col).value) < speed
	col = col + 1

	return  (speed / sheet.cell((1, col).value) * sheet.cell((2, col).value))

def proximitySensor()
	proximitySensorStatus = False

	for dist in range(.22, 7)
		for angle in range(15)
			if gameMap[boat.pos + dist * cos(boat.theta + angle)][boat.pos + dist * sin(boat.theta + angle)].type == "earth"
				proximitySensorStatus = True

	return proximitySensorStatus

#-----------------------------------------------------------------------------------------------	
   
def main():
	# Colors
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	RED = (150, 0, 0)
	GREEN = (0, 82, 33)
	BLUE = (47, 141, 255)
	YELLOW = (250, 250, 0)
	
	# Creation of the map
	matMap = matrix('lake.txt')
	map = Map()
	map.xTiles = len(matMap[0])
	map.yTiles = len(matMap)
	gameMap = [[Tiles() for i in range(map.xTiles)] for j in range(map.yTiles)]
	for i in range(map.yTiles):
		for j in range(map.xTiles):
			if matMap[i][j] == 0:
				gameMap[i][j].type = "earth"
				gameMap[i][j].color = GREEN
			elif matMap[i][j] == 1:
				gameMap[i][j].type = "water"
				gameMap[i][j].color = BLUE

	# Creation of the window
	pygame.init()
	
	map.ratio = 2
	map.tileSize = 20

	map.xPixels = map.xTiles * map.tileSize
	map.yPixels = map.yTiles * map.tileSize
	window = pygame.display.set_mode((map.xPixels, map.yPixels))
	pygame.display.set_caption("Haddock")

	# Creation of the boat
	boat = Boat()
	boat.color = RED

	# Creation of gps objects
	matGPS = matrix("gps.txt")
	gps = [gpsPoint() for i in range(len(matGPS))]
	for index, ob in enumerate(gps):
		ob.pos = matGPS[index]

	# Surface
	DISPLAYSURF = pygame.display.set_mode()

	# Initialize the first target
	target = gps.pop(0)
	target.color = YELLOW

	# Infinite loop recursivly :P
	while True:
		# Draw Tiles
		drawTiles(gameMap, map, DISPLAYSURF)
		
		#Draw GPS Points
		drawPts(gps, DISPLAYSURF)
		
		# Draw Boat
		drawBoat(boat, DISPLAYSURF)

		if target:
			drawTarget(target, DISPLAYSURF)
			calculateNewBoatPos(boat, target)

			if isInRadius(boat.pos, target.pos, 2) and len(gps):
					target = gps.pop(0)
					target.color = YELLOW

			elif isInRadius(boat.pos, target.pos, 2) and not len(gps):
				target = False
		

		# Update the window
		pygame.display.flip()
		
		# Quit event				       
		checkForQuit()

		# Tic toc
		pygame.time.delay(20) 
		
#-----------------------------------------------------------------------------------------------

if __name__ == '__main__':
	main() 