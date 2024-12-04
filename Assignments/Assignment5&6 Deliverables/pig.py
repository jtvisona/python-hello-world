"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 5&6
pig.py
"""
import sys
import os

def main():
    file_name = "Assignments\Assignment5&6 Deliverables\pig_dice_rules.txt"

    try:
        with open( file_name ) as file:
            file_contents = file.read()
    except:
        print( f"Error opening file named '{file_name}'" )
        sys.exit()
    
    print( f"File Contents\n-------------\n{file_contents}" )

if __name__ == "__main__":
    main()
