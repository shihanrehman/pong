class className:
	def createName(self,name): #self is a temporary placeholder for the object, if you have an object name as apples, whenever you call the object, it's gonna throw apples in place of self
		self.newName=name
		print name
	def displayName(self):
		return self.newName
	def saying(self):
		print 'hello %s' % self.newName  

first=className()
second=className()
first.createName("bucky") #self refers to first
second.createName("tony")
print first.displayName()
print first.saying()
print first.newName

#self is a placeholder for the ojbect

class parentClass:
	var1="i am var1"
	var2="i am var2"

class childClass(parentClass):
	pass #dont' do anything

parentObject=parentClass()
print parentObject.var1
childObject=childClass()
print childObject.var1
print childObject.var2

class Line:	# Line inherits from Square. It will use the Square's `draw` method, and its `__init__` method
	def __init__(self, height, *args, **kwargs):
		self.height = height
		self.width = 1
		self.color = (args,kwargs)

printLine = Line(0,255,255)
print printLine.color













class parent:
	var1="bacon"
	var2="sausage"

class child(parent):
	var2="toast"

child=child()
print child.var1
print child.var2

class Mom:
	var1="hey i'm mom"

class Dad:
	var2="hey i'm dad"

class child(Mom,Dad):
	var3="im a kid"

childObject=child()
print childObject.var1
print childObject.var2

class swine:
	def apples(self):
		print "beef pie"

obj=swine()
obj.apples()
#beef pie
class new:
	def __init__(self):
		print "this is a constructor"
		print "this also prints out"

newobj=new()
print newobj
#prints out the methods in construcor method


class Human():
	def __init__(self,name,gender):
		self.name = name
		self.gender = gender
	def speak_name(self):
		print "my name is %s" % self.name
	def speak(self,text):
		print text

will = Human("william","male")

print will.name

print will.speak_name()

will.speak("I love Python")

class Rectange():
	def __init__(self,width, lenght):		
		self.width = width
		self.length = length

	def area(self):
		self.area = area
		return self.area * self.length

	def perimter(self):
		return self.length * 2 + self.width * 2

my_rect = Rectange(5,6)
another_rect = Rectange(2,10)

print my_rect.area()
print another_rect.area()
print my_rect.perimter()

class Character():
	total_number_of_chracters = 0 # static
	MAX_HEALTH = 150
	def __init__(self,name):
		self.name = name
		self.health = Character.MAX_HEALTH
		Character.total_number_of_chracters += 1

bob = Character("Bon")
ryan = Character("Ryan Stevens")

print Character.total_number_of_chracters
print Character.MAX_HEALTH


class Matrix():
	def __init__(self, rows, columns, default_character = '@'):
		self.rows = rows
		self.columns = columns
		
    def grid(self):
		self.grid = [ [default_character] * columns for _ in xrange(rows)]

box = Matrix(4,5)
print box.grid





		