# welcome message function
def welcome():
    print("Welcome to conversion converter")

# feet to meters function
def feet_to_meters(feet):
    return feet * 0.3048

# meters to feet function
def meters_to_feet(meters):
    return meters / 0.3048

# main() function
def main():
    print("\nConvert: ")
    print("a. Meters to Feet")
    print("b. Feet to Meters")
    
    while True:
        choice = input("Select conversion (a/b): ")
        if choice == "a":
            meters = float(input("Enter meters: "))
            feet = meters_to_feet(meters)
            print(f"Result: {feet} feet")
        elif choice == "b":
            feet = float(input("Enter feet: "))
            meters = feet_to_meters(feet)
            print(f"Result: {meters} meters")
        else:
            print("You did not pick a valid selection.")
        
        again = input("Would you like to perform another conversion? (y/n): ")
        if again.lower() != "y":
            break
    
    print("\nThanks, bye!")

if __name__ == "__main__":
    welcome()
    main()
