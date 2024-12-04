#!/usr/bin/env python3

def display_title():
    print("Hike Calculator")
    print()

def to_feet(miles):
    feet = miles * 5280
    feet = int(round(feet))
    return feet

def main():
    display_title()
    miles = float(input("How many miles did you walk?: "))
    feet = to_feet(miles)
    print("You walked", feet, "feet.")

if __name__ == "__main__":
    main()
