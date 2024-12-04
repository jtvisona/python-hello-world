"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 12
bird_counter.py
"""

import pickle
import sys

FILENAME = r"C:\Users\17082\Documents\github-repos\python-hello-world\Assignments\Assignment8 Deliverables\birds.bin"

def write_birds( birds ):
    try:
        with open( FILENAME, "wb" ) as file:
            pickle.dump( birds, file )
    except Exception as e:
        print( f"Error: write_birds(): {e}" )


def read_birds():
    birds = {}
    try:
        with open( FILENAME, "rb" ) as file:
            birds = pickle.load(file)
        return birds
    except FileNotFoundError as e:
        print( f"Error: read_birds(): {e}" )
        sys.exit(1)
    
def main():
    print( "Bird Counter\n" )
    print( "Enter 'x' to exit\n" )

    birds = read_birds()
    while True:
        name = input( "Enter name of bird: " ).title()
        if name.lower() == "x":
            break
    
        if name in birds:
            birds[ name ] += 1
        else:
            birds[ name ] = 1
    print ()
    
    names = list( birds.keys() )
    names.sort()

    w1 = 25; w2 = 5; count = 0
    print( f"{'Name':{w1}} {'Count':{w2}}" )
    print( f"{'='*w1} {'='*w2}" )
    for name in names:
        count = birds[ name ]
        print( f"{name:{w1}} {count:<{w2}d}" )

if __name__ == "__main__":
    main()


