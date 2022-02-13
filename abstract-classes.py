"""
An abstract class allows one to create a set of methods that must be created within any child classes built from the abstract class.
It is a method that has a declaration but does not have an implementation.

"""

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