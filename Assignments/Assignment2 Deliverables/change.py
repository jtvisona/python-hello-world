#!/usr/bin/env python3

print("Change Calculator")
print("Enter a value in cents")
# display welcome message

choice = "y"
while choice.lower() == "y":
    # get input from the user
    cents = int(input("Enter number of cents (0-99): "))
    print()

    # calculate the number of quarters
    quarters = cents // 25
    # assigns the remainder to the cents variable
    cents = cents % 25

    # calculate the number of dimes
    dimes = cents // 10
    # assigns the remainder to the cents variable
    cents = cents % 10

    # calculate the number of nickels and pennies
    nickels = cents // 5 
    pennies = cents % 5

    # display results:
    print("Quarters: " + str(quarters))
    print("Dimes: " + str(dimes))
    print("Nickels: " + str(nickels))
    print("Pennies: " + str(pennies))

    # see if the user wants to continue 
    choice = input("Continue? (y/n): ")
    print()
