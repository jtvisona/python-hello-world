import locale

# set the locale for use in currency formatting
locale.setlocale(locale.LC_ALL, 'en_US')

# No splash screen yet!
print("This is a application that does a financial calculation")
print()

user_input = "y"
while user_input.lower() == "y":
    # get input from the user
    savings_amount = float(input("Enter a monthly savings amount:\t$"))

    # show sum for next 12 months
    for i in range(1,13):
        # format and display the result
        print(f"Savings at {i} month(s):",end="")
        print( "\t" + locale.currency(i * savings_amount, grouping=True) )

    # see if the user wants to continue
    user_input = input("Show differenat amount? (y/n): ")
    print()

print("Thanks!")
