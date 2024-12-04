"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 5&6
monthly_salary.py
"""

import csv
import sys

MONTH_SELECTED = 0
AMOUNT = 1
INPUT_NAME = "Assignments\\Assignment5&6 Deliverables\\monthly_sales.csv"
MONTHS = [ "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ]

def write_sales( sales: list ) -> None:
    try:
        with open( INPUT_NAME, "w", newline="" ) as input_file:
            writer = csv.writer( input_file )
            writer.writerows( sales )
    except Exception as e:
        print( f"Exception: {e}")

def read_sales() -> list:
    try:
        sales = []
        with open( INPUT_NAME, newline="" ) as output_file:
            reader = csv.reader( output_file )
            for each_row in reader:
                print( ".", end="" )
                sales.append( each_row )
            print()
    except Exception as e:
        print( f"Exception: {e}")
    finally:
        return sales

def view_monthly_sales( sales ) -> None:
    for each_row in sales:
        print( each_row[0], " - ", each_row[1] ) 
    print()

def view_yearly_summary( sales: list ) -> None:
    total = 0
    average = 0
    for each_row in sales:
        total += int( each_row[1] )
    try: 
        average = round( total / len( sales ), 2 )
    except Exception as e:
        print( f"Exception: {e}")
    finally:     
        print( f"Yearly: {total}\nMonthly: {average}\n" )

def edit( sales: list ) -> None:
    month_selection = input( "Three-letter month code: " ).title()

    if month_selection in MONTHS:
        index = MONTHS.index( month_selection )
        month = []
        list( month.append( month_selection )).append( str( int( input( "Sales amount: " ) ) ) )
        sales[ index ] = month
        write_sales( sales )
        print( f"Sales for {month[MONTH_SELECTED]} modifed.\n" )
    else:
        print( f"'{month_selection}' is invalid.\n" )

def display_menu() -> None:
    menu = """
    COMMANDS
    monthly - View monthly sales
    yearly  - View yearly summary
    edit    - Edit sales figure for month
    exit    - Exit application

    """
    print( menu )

def main() -> None:
    print( "Montly Salary Application" )
    sales = []
    sales = read_sales()
    #print( f"{sales=}" )
    display_menu()
    while True:
        command = input( "> " )
        if command == "monthly":
            view_monthly_sales( sales )
        elif command == "yearly":
            view_yearly_summary( sales )
        elif command == "edit":
            edit( sales )
        elif command == "exit":
            write_sales( sales )
            print( "Exiting" )
            sys.exit()
        else:
            print( "Invalid command" )


if __name__ == "__main__":
    main()

