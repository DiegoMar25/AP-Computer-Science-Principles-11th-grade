#Printing commands
x = 5
y = "John"
a = 4
A = "Bob"
print(x, y)
print(a, A)
# A will not overwrite a
#  "=" in programming means "Assigned to" Ex. 5 is assigned to variable x
#                 Legal Variable Names
# Variables can’t begin with capital
# no spaces (can be replaced with underscores, dashes, etc.)
# Can’t begin with a number
# It is case sensitive and CANNOT contain alpha-numeric characters [A-z or 0-9]
# the "#" can also mean "not equal to"
# in programming, it's often more about being efficient rather than effective
#Python allows you to assign many values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(x, y, z)
#Python allows you to assign one value to multiple variables
c = 1
d = 1
e = 1
print(c, d, e)
x = y = z = "Orange"
# RANDOM NUMBER
import os
import random

os.system('clear')
print(random.randrange(1, 10))

#Concatenation
#To concatenate or combine 2 strings you can use the + operator
#Add " " between the variables
a, b = "hola", "Juan"
c = a + " " + b
print(c)
# String format
age = "36"
text = "My name is patricia, I am " + age
print(text)

#Functions
''' A function is a block of code which only runs when it is called. You can pass data, known as parameter, into a function. A function can get data as a result '''
# Creating a Function
# In python a function is created using the def keyword
def my_function():
  print("Hello from a function") 

# Calling a Function
# To call a function, use the function name by parenthesis
my_function()
#Example
def my_Function(fname):
 print(fname + "Joaquin")
 my_Function("Pizza")
  #Parameters or Arguments
# The terms parameter and argument can be used for the same thing : informationthat arre passed into a function/ executed 
# A parameter is the variable listed inside the parenthes is in the function definition.
# an argument is the value sent to the function when it's called 
def my_function(fname,lname):
 print(fname + "" + lname)
my_function("Carlos", "Campuzano")
#Pyhton Class
# To Create a class, Use Keyboard class 
# create a class named MyClass, with a property named x:
class MyClass:
  x=5 
  
#Create an Object
#Now we can use the class name MyClass to create an object 
#Create an object named G1, and print the value of x:
g1 = MyClass ()
print (g1.x)
#The _init_ () function to assign values for name and age:
#Example  Create a class named Person, use the _init_ () function to assign values for name and age
class Person:
  def __init__(self,name,age):
    self.name= name
    self.age= age
    
g1 = Person("John", 36)

print(g1.name)
print(g1.age)

#Note the _init_() function is called automatically every time the class is being used to create a new object.
#Python Inheritance 
#Inheritance allows us to deinfe a class that inherits all the methods and properties from another class
#Parent class is the class being inherited from, also called base class
#Child Class is: is the class that inherits from another class, also called derived class
# any class can be a parent, so syntax is the same as creating other class
# EX. create a class named Person, with firstname and lastname properties, and a printname method: 
class Person: 
  def _init_ (self, fname, lname):
    self.fname=fname
    self.lname=lname 
def printname (self):
  print (self.firstname, self.lastname)
#Use Person class to create an object, and then execute the printname method
x=person ("John", "Doe")
x.printname()
#Child Class 
#To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class
#Ex: Assign: Create a class named student, which will inherit the properties and methods from the Person class
class Student(Person):
  pass
  #Example: Use the student class to create and object, and then execute the printname method
  x=Student ("Mike", "Olsen")
x.printname()
