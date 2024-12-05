"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 10
quad_calc.py
"""

from dataclasses import dataclass
import sys

@dataclass
class Rectangle:
    height: int
    width: int

    def getPerimeter( self ):
        return self.height * 2 + self.width * 2

    def getArea( self ):
        return self.height * self.width

    def __str__( self ):
        quad = ''
        top_bottom = "*" * self.width + "\n"
        quad += top_bottom
        # for "hollow" portions of quadrilateral
        for i in range( self.height - 2 ):
            quad += "*"
            quad += " " * ( self.width - 2 )
            quad += "*\n"
        quad += top_bottom
        return quad

@dataclass
class Square( Rectangle ):
    def __init__( self, length ):
        Rectangle.__init__( self, length, length )

def display( rectangle ):
    print( "Perimeter:", rectangle.getPerimeter() )
    print( "Area:", rectangle.getArea() )
    print( rectangle )

def main():
    print("Rectangle Calculator")
    print()
    choice = "y"

    while choice.lower() == "y":
        shape = input( "Rectangle or square? (r/s): " )
        if shape == "r":
            height = int( input( "Height:" ) )
            width = int( input( "Width:" ) )
            rectangle = Rectangle( height, width )
            display( rectangle )
        elif shape == "s":
            length = int( input( "Length: " ) )
            square = Square( length )
            display( square )
        else:
            print( "Invalid entry. Try again." )
            continue

        choice = input( "Continue? (y/n): ").lower()
        print()
    print( "Ciao!" )

if __name__ == "__main__":
    main()