# simple shipping calculator program

print("------------------------------------------------")
print("Welcome to Shipping Calculator!")
print("------------------------------------------------")

while True:
    # get input from the user
    cost_of_items = float(input("Cost of items ordered: $"))

    # make sure input is a positive number
    if cost_of_items < 0:
        print("Please try again. Must enter a positive number.")
        continue

    # calculate shipping cost
    if cost_of_items == 0:
        shipping_cost = 0
    elif cost_of_items <= 50:
        shipping_cost = 10
    elif cost_of_items <= 75:
        shipping_cost = 5
    elif cost_of_items <= 100:
        shipping_cost = 3
    else:
        shipping_cost = 0

    # calculate total cost
    total_cost = round(cost_of_items + shipping_cost, 2)

    # display costs
    print("Shipping Cost: $", shipping_cost)
    print("Total Cost: $", total_cost)

    # ask if the user wants to continue using calculator 
    choice = input("Continue? (y/n): ").lower()
    if choice == 'n':
        break

# end program 
print("\nThank you for using Shipping Calculator!")
