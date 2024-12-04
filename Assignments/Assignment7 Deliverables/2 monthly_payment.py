"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 7
monthly_payment
"""

from decimal import Decimal
import locale as lc

def calculate_monthly_payment( loan_amount, yearly_interest_rate, years ):
    monthly_interest_rate= yearly_interest_rate / 12 / 100
    months = years * 12
    monthly_payment = loan_amount * monthly_interest_rate / \
       (1-1 /(1 + monthly_interest_rate) ** months)
    return monthly_payment

def main():
    print( "monthly_payment Calculator" )
    print()
    choice = "y"

    while choice.lower() == "y":
        print( "Data entry" )
        loan_amount = Decimal( input( "Loan amount: " ) )
        interest_rate = Decimal( input( "Yearly interest_rate: " ) )
        years = int( input( "Years: " ) )
        print()
        loan_amount = loan_amount.quantize( Decimal( "1.12" ) )
        interest_rate = interest_rate.quantize( Decimal( "1.1" ) )
        # calculate and quantize the results
        monthly_payment = calculate_monthly_payment(loan_amount, interest_rate, years)
        monthly_payment = monthly_payment.quantize(Decimal( "1.12" ))
        print( "FORMATTED RESULTS" )
        lc.setlocale( lc.LC_ALL, "en_US" )
        loan_amount= lc.currency(loan_amount, grouping=True)
        monthly_payment = lc.currency(monthly_payment, grouping=True)
        w1 = 22
        w2 = 16
        print( f"Loan amount: \t\t{loan_amount:>{w2}}" )
        print( f"Yearly interest_rate: \t{interest_rate:> {w2-1}}%" )
        print( f"Number of years:\t {years:>{w2}}" )
        print( f"monthly_payment:\t {monthly_payment:>{w2}}" )
        print()
        
        choice = input( "Continue?(y/n): " )
        print()

    print( "Ciao!" )

if __name__ == "__main__":
    main()