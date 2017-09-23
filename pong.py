import pygame 

pygame.init()

window = pygame.display.set_mode((600,400)) #tuples are immutable arrays


class Sprite:
	def __init__(self, x=200, y=200): #constructor automatically called if it is present when you create a new instance.
		self.x = x #self is the current instance of the class.  Setting the x property of the instance, not the class.  
		self.y = y

	def draw(self, window):
		raise Exception("not implemented")


class Square(Sprite):  # Square inherits from Sprite. It will use the Sprite's `__init__` method. It overrides Sprite's `draw` method
	def __init__(self, height, width, *args, **kwargs):
		Sprite.__init__(self, *args, **kwargs)
		self.height = height
		self.width = width
		self.color = (0, 0, 255)

	def draw(self, screen): #draws the rectangle onto the screen
		pygame.draw.rect(screen, self.color, pygame.Rect((self.x, self.y), (self.width,self.height)), 0)


class Line(Square):	# Line inherits from Square. It will use the Square's `draw` method, and its `__init__` method
	def __init__(self, height, *args, **kwargs):
		Square.__init__(self, *args, **kwargs)
		self.height = height
		self.width = 1
		self.color = (0, 255, 255)


#Display Text 
# Create a new class called Text, which inherits from Sprite.
# Have it use a draw method which will write text to the screen. Check the pygame docs for how to display check.
# For example, it should print the number "0" on the window. Or any other text will work.
# You may want to have the number/text that it writes to the screen be dictated by an internal property, like `self.score` or `self.text`


while True : 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit() #cleans up all the resources
			exit()

	s = Square(100, 100, 0, 0)
	s.draw(window)

	l = Line(400, 100, 0)
	l.draw(window)
	pygame.display.flip()




"""
class Test:
	def __init__(self, *args, **kwargs):
		print(args, kwargs)


t = Test(1, 2, five=5, three=3, four=4)
"""



# this is a comment

"""
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def favorite_food(self):
		raise Exception("not implemented")


class Curtis(Person):
	def __init__(self):
		Person.__init__(self, "Curtis", 24)

	def favorite_food(self):
		print("I love pizza!")


class Magic:
	
	def __str__(self):
		return "this is what is printed"
	



print(Magic())

class (shihan < curtis)
"""