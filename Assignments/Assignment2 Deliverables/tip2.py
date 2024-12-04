#!/usr/bin/env python3

# Tip Calculator

print("Tip Calculator")
print()

meal_cost = float(input("Cost of meal: "))
tip_percent = int(input("Tip percent: "))

for tip_percent in range(15, 30, 5):
    print()
    # calculate tip and total
    tip_amount = meal_cost * tip_percent / 100
    total = round(meal_cost + tip_amount, 2)
    
    # display the results:
    print(f"Tip amount: ", tip_amount)
    print(f"Total amount: ", total)
