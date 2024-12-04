"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 7
fuel.py
"""
import math

def main():
    print( "Aircraft Fuel Calculator\n" )
    choice = "y"
    while choice.lower() == "y":
        distance = int( input( "Distance in nautical miles: " ) )
        knots_per_hour = 120
        flight_time = distance / knots_per_hour
        hours = distance // knots_per_hour
        distance = distance % knots_per_hour
        knots_per_minute = knots_per_hour / 60
        minutes = int(distance // knots_per_minute)
        gallons_per_hour = 8.4
        reserve_time = 0.5
        fuel = gallons_per_hour * ( flight_time + reserve_time )
        fuel = math.ceil(fuel * 10) / 10
        
        print( f"Flight time:{hours} hour(s) and {minutes} minute(s) " )
        print( f"Required fuel:{fuel} gallons" )
        print()   
        choice = input( "Continue?(y/n): " )
        print()

    print("Ciao!")

if __name__ == "__main__":
    main()