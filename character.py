class Direction():
	
	SOUTH = 's'
	WEST = 'a'
	EAST = 'd'
	NORTH = 'w'

class MainSymbol():
	def __init__(self, symbol, startX = 0, startY =0, velx = 1, vely = 1, trace = 'x'):
		self.symbol = symbol
		
		self.x = startX
		self.y = startY

		self.velx = velx
		self.vely = vely

	def move(self, direction):

		#Y
		if direction == Direction.SOUTH:
			self.y += self.vely
		elif direction == Direction.NORTH:
			self.y -= self.vely
		#X
		elif direction == Direction.EAST:
			self.x += self.velx
		elif direction == Direction.WEST:
			self.x -= self.velx