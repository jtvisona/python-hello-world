"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 8
future_value.py
"""

from datetime import datetime as DT_datetime

def calculate_future_value( monthly_investment: float, yearly_interest_rate: float, years: int ) -> float:
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12
    future_value = 0
    # my first use of a dummy variable in python! :D Yay, me.
    for _ in range( months ):
        future_value = (future_value + monthly_investment) * (1 + monthly_interest_rate)
    #debug print( f"{type(future_value)}") # just to be sure get float

    return future_value

def log( monthly_investment: float, yearly_interest_rate: float, years: int, future_value:float ) -> None:
    current_datetime = DT_datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{current_datetime} - {monthly_investment}|{yearly_interest_rate}|{years}|{future_value:.2f}\n"    
    try:
        with open("future_value_log.txt", "a") as file:
            file.write( entry )
    except Exception as e:
        print( f"log(): {e}" )

def main():
    while True:
        monthly_investment = float( input( "Enter monthly investment: "  ))
        yearly_interest_rate = float( input( "Enter yearly interest rate: "  ))
        years = int( input( "Enter number of years: " ) )

        future_value = calculate_future_value( monthly_investment, yearly_interest_rate, years )
        print( f"Future value: ${future_value:,.2f}" )
        log( monthly_investment, yearly_interest_rate, years, future_value )
        
        choice = input( "Continue? (y/n): " ).lower()
        if choice != 'y':
            break

    print("Ciao!")

if __name__ == "__main__":
    main()