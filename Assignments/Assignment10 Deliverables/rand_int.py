"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 10
rand_int.py
NB the inheritance from the list type and the use of self as an iterable list
"""
import random
from dataclasses import dataclass

MIN = 1; MAX = 100

@dataclass
class RandomIntList( list ):
    def __init__( self, count ):
        for _ in range( count ):
            rnd_int = random.randint( MIN, MAX )
            #print( f"Appending integer {rnd_int}" )
            self.append( rnd_int )

    @property
    def count( self ):
        return len( self )

    @property
    def total( self ):
        total = 0
        for i in self:
            total += i
        return total

    @property
    def average( self ):
        return self.total / self.count

    def __str__( self ):
        str_output = ""
        str_output += "[ "
        for i in self:
            str_output += str( i ) + " " 

        str_output += "]"
        return str_output

def get_int( size ):
    while True:
        try:
            return int( input( size ) )
        except ValueError:
            print( "Invalid whole number. Please try again." )

def main():
    print( "Random Integer List" )
    print()
    again = "y"
    while again.lower () == "y":
        list_size = int( get_int( "How many random integers should the list contain? ") )
        print()
        rnd_list = RandomIntList( list_size )
        print( "Random Integers" )
        print( "======" )
        print( "Integers: ", rnd_list )
        print( "Count: ", rnd_list.count )
        print( "Total: ", rnd_list.total )
        print( "Average: ", round( rnd_list.average, 3 ) )

        again = input( "Continue? (y/n): " ).lower()
        print()

if __name__ == "__main__":
    main()