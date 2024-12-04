#!/usr/bin/env python3

"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 3
sales_tax.py
"""

def get_items_total():
    print("ENTER ITEMS (ENTER 0 TO END)")
    total = 0
    while True:
        item_cost = float(input("Cost of item: "))
        if item_cost == 0:
            break
        total += item_cost
    return round(total, 2)

def get_tax(total):
    total *= 0.06
    return total

def get_total_after_tax(total, total_tax):
    return total + total_tax

def main():
    print("Sales Tax Calculator\n")
    while True:
        total = get_items_total()
        #print( f"{total=}")
        print("Total:", total)
        total_tax = get_tax(total)
        #print( f"{total=} {total_tax=}")
        print("Sales tax:", total_tax)
        print("Total after tax:", get_total_after_tax(total, total_tax))
        print()
        again = input("Again? (y/n): ")
        print()
        if again.lower() != "y":
            break
    print("Thanks, bye!")

if __name__ == "__main__":
    main()
