"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 7
NAME
"""

import sys
from decimal import Decimal
import locale as lc

loan_amount = 0

def main():
    print ("Interest Calculator")
    print()
    choice = "y"

    while choice.lower () == "y":
        # get user input and future value
        loan_amount = Decimal( input( "Enter loan amount: " ) )
        interest_rate = Decimal( input( "Enter interest rate: " ) )
        print()
        # quantize the entries
        loan_amount = loan_amount.quantize( Decimal( "1.12" ) )
        interest_rate = interest_rate.quantize( Decimal( "1.123" ) )
        # calculate and quantize the interest amount interest_amount loan_amount (interest rate / 100) interest_amount= interest_amount.quantize (Decimal("1.12"))

        # format and display the results
        lc.setlocale( lc.LC_ALL, "en_US" )
        loan_amount = lc.currency( loan_amount, grouping=True )
        interest_amount = lc.currency( interest_rate, grouping=True )

        width = 16
        print ( f"Loan amount:\t{loan_amount:>{width}}" )
        print ( f"Interest rate:\t{interest_rate:>{width-1}}%" )
        print ( f"Interest amount:{interest_amount:>{width}}" )
        # subtract 1 from second width formatting to accommodate '%' char print (f"{'Interest rate:': {width}} {interest_rate:>{width - 1}}%") print (f"{'Interest amount:':{width}} {interest_amount:>{width}}") print()
        choice = input( "Continue? (y/n): " )
        print()

    print( "Ciao!" )

if __name__ == "__main__":
    main()