#!/usr/bin/env python3

"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 3
dice.py
"""

import random

def roll():
    value = random.randint(1, 6)
    return value

def display_title():
    print("Dice Roller")
    print()

def roll_dice():
    die1 = roll()
    die2 = roll()
    total = die1 + die2
    print("Die 1:", die1)
    print("Die 2:", die2)
    print("Total:", total)
    if total == 2:
        print("Snake eyes!")
    if total == 12:
        print("Boxcars!")
    print()

def main():
    display_title()
    choice = input("Roll the dice? (y/n): ")
    print()
    while choice == "y":
        roll_dice()
        choice = input("Roll again? (y/n): ")
        print()

if __name__ == "__main__":
    main()
