import pygame 

pygame.init()

window = pygame.display.set_mode((600,400)) #tuples are immutable arrays


class Sprite:
	def __init__(self, x=100, y=100): #constructor automatically called if it is present when you create a new instance.
		self.x = x #self is the current instance of the class.  Setting the x property of the instance, not the class.  
		self.y = y

	def draw(self, window):
		raise Exception("not implemented")


class Paddle1(Sprite):  # Paddle1 inherits from Sprite. It overrides Sprite's `draw` method
	def __init__(self, height, width, *args, **kwargs):
		Sprite.__init__(self, *args, **kwargs) # It will use the Sprite's `__init__` method. 
		self.height = height
		self.width = width
		self.color = (0, 0, 255) # RGB value. (0 - 255, 0 - 255, 0 - 255)

	def draw(self, screen): #draws the rectangle onto the screen
		pygame.draw.rect(screen, self.color, pygame.Rect((self.x, self.y), (self.width,self.height)), 0)


class Paddle2(Sprite):  # Paddle1 inherits from Sprite. It overrides Sprite's `draw` method
	def __init__(self, height, width, *args, **kwargs):
		Sprite.__init__(self, *args, **kwargs) # It will use the Sprite's `__init__` method. 
		self.height = height
		self.width = width
		self.color = (0, 0, 255) # RGB value. (0 - 255, 0 - 255, 0 - 255)

	def draw(self, screen): #draws the rectangle onto the screen
		pygame.draw.rect(screen, self.color, pygame.Rect((self.x, self.y), (self.width,self.height)), 0)


class Line(Paddle1):	# Line inherits from Paddle1. It will use the Paddle1's `draw` method.
	def __init__(self, height, *args, **kwargs): #args would be a list that would contain the X and Y coordinates
		Sprite.__init__(self, *args, **kwargs) # Uses sprites's `__init__` method
		self.height = height
		self.width = 4
		self.color = (0, 255, 255)


class Text(Sprite):
	def __init__(self,font,*args,**kwargs):
		Sprite.__init__(self, *args, **kwargs)
		self.font = font.render("Your Score",1,(255,255,0))

	def draw(self, screen):
		screen.blit(self.font, (self.x, self.y))	

class Ball(Sprite):  # Ball inherits from Sprite. It overrides Sprite's `draw` method
	def __init__(self, height, width, *args, **kwargs):
		Sprite.__init__(self, *args, **kwargs) # It will use the Sprite's `__init__` method. 
		self.height = height
		self.width = width
		self.color = (0, 0, 255) # RGB value. (0 - 255, 0 - 255, 0 - 255)

	def draw(self, screen): #draws the rectangle onto the screen
		pygame.draw.rect(screen, self.color, pygame.Rect((self.x, self.y), (self.width,self.height)), 0)


# Create two paddles using the Paddle1 class. Set the height/width appropriately, and set the x/y for both so they are opposite sides of the screen
# Create a pong ball by using the Paddle1 class. you can put it anywhere on the screen for now.
# Updating the Text class so we can change the text that actually gets rendered to the screen (so it isnt only "You Score" everytime).

# Next time we can look at animating these objects so they move on the screen.



while True : 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit() #cleans up all the resources
			exit()

	paddle1 = Paddle1(30, 20, 0, 0) #height,width,x-pos,y-pos

	paddle2 = Paddle2(30, 20, 580, 0)

	# s = Paddle1()
	# s.__init__(100, 100, 0, 0)
	# Paddle1.__init__(s, 100, 100, 0, 0)

	paddle1.draw(window)
	paddle2.draw(window)

	# s.draw(window) ---> Paddle1.draw(s, window)  ---> Paddle1.draw(s, screen=window)

	line = Line(400, 300, 0) # Create a line with a height of 400 (matches the window height), at x = 300 (halfway point on the window) and y = 0 (start at top of window)
	line.draw(window)  # in pygame x and y coordinates are from the top left

	t = Text(pygame.font.SysFont("monospace", 24), 200, 50) # "pygame.font.SysFont("times new roman")" would be passed in as the font attrbiute in Class Text; 200 is x and 50 is y, x and y overwrites the Sprites's init's x and y
	t.draw(window)

	ball = Ball(5, 5, 40, 50)
	ball.draw(window)

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