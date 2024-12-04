"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 5&6
wizard_inventory.py
"""

import random
import sys

ITEMS_FILE = "Assignments\\Assignment5&6 Deliverables\\wizard_all_items.txt"
INVENTORY_FILE = "Assignments\\Assignment5&6 Deliverables\\wizard_inventory.txt"

def read_file( file: str ) -> list:
    lines = []
    try:
        with open( file, "r", newline="" ) as input_file:
            print( f"Reading '{file}'", end="" )
            for each_line in input_file:
                print( ".", end="" )
                lines.append( each_line.strip() )
            print()
    except Exception as e:
        print( f"Exception: {e}")
    finally:
        return lines

def write_file( file: str, lines: list ) -> None:
    try:
        with open( file, "w" ) as output_file:
            print( f"Writing '{file}'", end="" )
            for each_line in lines:
                output_file.write( each_line )
    except Exception as e:
        print( f"Exception: {e}")

def display_title():
    print("The Wizard Inventory program")
    print()

def display_menu():
    menu = """
    COMMAND MENU
    show - Show all items
    grab - Grab an item
    edit - Edit an item
    drop - Drop an item
    walk - Take a stroll
    exit - Exit program
    """
    print( menu )

def show( inventory ):
    for i in range(len( inventory )):
        item = inventory[i]
        number = i + 1
        print(str(number) + ". " + item + " ", end="")
    print()

def grab_item( inventory ):
    if len( inventory ) >= 4:
        print("You can't carry any more items. Drop something first.\n")
    else:
        item = input("Name: ")
        inventory.append(item)
        print(item + " was added.\n")

def edit_item( inventory ):
    number = int( input("Number: "))
    if number < 1 or number > len( inventory ):
        print( "Invalid item number.\n" )
    else:
        item = input("Updated name: ")
        inventory[number - 1] = item
        print( "Item number " + str( number ) + " was updated.\n" )

def drop_item( inventory ):
    number = int( input("Number: ") )
    if number < 1 or number > len( inventory ):
        print( "Invalid item number.\n") 
    else:
        item = inventory.pop(number - 1)
        print( item + " was dropped.\n" )

def walk( inventory, items ):
    new_item = random.choice( items )
    print( f"While walking down the path you see a {new_item}" )
    yn_choice = input( "Do you want to grab it? (y/n) " )
    if yn_choice.lower() == "y":
        grab_item( inventory )

def main():
    display_title()
    items  = read_file( ITEMS_FILE )
    inventory = read_file( INVENTORY_FILE )

    display_menu()
    # all players start with these 3 items
    
    while True:
        command = input("Command: ")
        if command == "show":
            show( inventory )
        elif command == "grab":
            grab_item( inventory )
        elif command == "edit":
            edit_item( inventory )
        elif command == "drop":
            drop_item( inventory )
        elif command == "walk":
            walk( inventory, items )
        elif command == "exit":
            write_file( INVENTORY_FILE, inventory )
            sys.exit()
            print("Bye!")
        else:
            print("Not a valid command. Please try again.\n")
    

if __name__ == "__main__":
    main()
