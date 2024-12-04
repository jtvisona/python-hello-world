"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 5&6
tip.py
"""

def get_cost() -> float:
    while True:
        try:
            meal_cost = float( input( "Meal's cost: " ) )
        except ValueError:
            print( "Use decimal value." )
            continue

        if meal_cost < 0.00:
            meal_cost *= -1
        return meal_cost

def get_tip_percent() -> int:
    while True:
        try:
            tip_percent = int( input ( "Tip %: " ) )
        except ValueError:
            print( "Use integer." )
            continue

        if tip_percent < 0:
            tip_percent *= -1

        return tip_percent

def main() -> None:
    print( "Tip Calculator\n" )
    print( "INPUT" )
    meal_cost = get_cost()
    tip_percent = get_tip_percent()
    tip = round( meal_cost * (tip_percent/100), 2 )
    total = round( meal_cost + tip_percent, 2 )

    message = f"""OUTPUT
    Cost of meal: {meal_cost}
    Tip percent: {tip_percent}
    Tip: {tip}
    Total: {total}
    """
    print( message )
    
if __name__ == "__main__":
    main()