class Matrix():
	def __init__(self,rows,columns,default_character = '@'):
		self.rows = rows
		self.columns = columns
	def grid(self):
		self.grid = [[default_character] * columns for _ in xrange(rows)]

box = Matrix(4,5)
print box.grid