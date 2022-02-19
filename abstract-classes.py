"""
An abstract class allows one to create a set of methods that must be created within any child classes built from the abstract class.
It is a method that has a declaration but does not have an implementation.

"""

'''
How Abstract Base classes work : 
By default, Python does not provide abstract classes. Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that module name is ABC. ABC works by decorating methods of the base class as abstract and then registering concrete classes as implementations of the abstract base. A method becomes abstract when decorated with the keyword @abstractmethod.
'''

# Implementation

from abc import ABC, abstractmethod

class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass

class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")

class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")

class Hexagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")

class Quadrilateral(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")

# Driver code

R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

P = Pentagon()
P.noofsides()

H = Hexagon()
H.noofsides()


# Example 2
# Python progrom showing abstract base class work

from abc import ABC, abstractmethod
class Animal(ABC):

    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Dog(Animal):

    def move(self):
        print("I can bark")

class Snake(Animal):

    def move(self):
        print("I can crawl")

class Lion(Animal):
     
    def move(self):
        print("I can roar")

# Driver code
Hu = Human()
Hu.move()
 
S = Snake()
S.move()
 
D = Dog()
D.move()
 
L = Lion()
L.move()