"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 7
loan2.py
"""

from decimal import Decimal
import locale as lc

def main():
    print( "Interest Calculator\n" )
    choice = "y"
    while choice.lower() == "y":
        loan_amount = Decimal( 0 )
        input_str = input ( "Enter loan amount:" ).strip()
        if "," in input_str:
            input_str = input_str.replace( ",", "" )
        if input_str.startswith( "" ):
            input_str = input_str[1:]
        if input_str.endswith ( "K" ) or input_str.endswith( "k" ):
            input_str = input_str [0:-1]
            k_multiplier = Decimal( 1000 )
        else:
            k_multiplier = Decimal( 1 )
        loan_amount = Decimal( input_str ) * k_multiplier

        input_str = input ( "Enter interest rate: " ).strip()
        if "%" in input_str:
            input_str = input_str.replace( "%", "" )
        interest_rate = Decimal( input_str )
        print()
        
        loan_amount = loan_amount.quantize( Decimal( "1.12" ) )
        interest_rate.quantize( Decimal( "1.123" ) )
        
        interest_amount = loan_amount * (interest_rate / 100)
        interest_amount = interest_amount.quantize (Decimal ( "1.12" ))
        
        lc.setlocale (lc.LC_ALL, "en_US" )
        loan_amount = lc.currency (loan_amount, grouping=True)
        interest_amount= lc.currency (interest_amount, grouping=True)
        
        width = 16
        print( f"{'Loan amount:':{width}} {loan_amount:>{width}}" )
        print( f"{'Interest rate:':{width}} {interest_rate:>{width-1}}%" )
        print( f"{'Interest amount:':{width}} {interest_amount:>{width}}\n" )
                
        choice = input ( "Continue? (y/n): " )
        print()

print ( "Ciao!" )

if __name__ == "__main__":
    main()