
"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 8
monthly_sales.py
"""

FILENAME = r"C:\Users\17082\Documents\github-repos\python-hello-world\Assignments\Assignment8 Deliverables\monthly_sales.txt"

MONTH = 0
MONTHLY_SALES = 1

def read_sales( sales: dict = {} ) -> dict:
    sales = {}
    try:
        with open( FILENAME, "r" ) as file:
            for line in file:
                line = line.replace( "\n", "" )
                row = line.split( "\t" )
                sales[ row[ MONTH ] ] = int( row[ MONTHLY_SALES ] )
        return sales
    except Exception as e:
        print( f"write_sales(): {e}" )


def write_sales( sales: dict ) -> None:
    try:
        with open( FILENAME, "w" ) as file:
            for month, amount in sales.items():
                file.write( f" {month} \t{amount}\n" )
    except Exception as e:
        print( f"write_sales(): {e}" )

def view_month( sales: dict = {} ) -> None:
    month = input( "Three-letter Month: " )
    month = month.title()
    if month in sales.keys():
        monthly_sales = sales[ month ]
        print( f"Sales amount for {month} is {monthly_sales:,.2f}.\n" )
    else:
        print( "Invalid three-letter month.\n" )

def edit_month( sales: dict ) -> None:
    month = input ( "Three-letter Month: " )
    month = month.title()
    if month in sales.keys():
        amount = float( input( "Sales Amount: " ) )
        sales[ month ] = amount
        write_sales( sales )
        print( f"Sales amount for {month} is {amount:,.2f}.\n" )
    else:
        print( "Invalid three-letter month.\n" )
 
def view_year( sales ):
    total = 0
    for month, amount in sales.items():
            total += int( amount )
    count = len( sales )
    average = total / count
    average = round( average, 2 )

    print( f"Yearly total:\t\t{total:12,.2f}" )
    print( f"Monthly average:\t{average: 12,.2f}\n" )

def display_menu():
    print( "COMMAND MENU" )
    print( "view - View sales for specified month" )
    print( "edit - Edit sales for specified month" )
    print( "totals - View sales summary for year" )
    print( "exit - Exit program\n" )

def main():
    print( "Monthly Sales program\n" )

    sales = read_sales()
    display_menu()
    while True:
        command = input( "Command: " )
        if command ==  "view":
            view_month( sales )
        elif command == "edit":
            edit_month( sales )
        elif command == "totals":
            view_year( sales )
        elif command == "exit":
            break
        else:
            print( "Not a valid command. Please try again. \n" )
    print( "Ciao!" )

if __name__ == "__main__":
    main()
