"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 7
Sales Report
"""

import locale as lc

def format_as_currency( value ):
    #print( f"type={type(value)} {value=}" ) # for debugging
    if( type(value) is str ):
        value = float( 0.00 )
    return_value = lc.currency( value, grouping=True )
    return return_value

def main():

    lc.setlocale(lc.LC_ALL, "en_US" )
    sales = [[1540.0, 2010.0, 2450.0, 1845.01],
             [1130.0, 1168.0, 1847.0, 1491.01],
             [1580.0, 2305.0, 2710.0, 1284.01],
             [1105.0, 4102.0, 2391.0, 1576.011]]

    print( "Sales Report" )
    w = 12
    for number, region in enumerate( sales, start=1 ):
        ql = format_as_currency( region[0] )
        q2 = format_as_currency( region[1] )
        q3 = format_as_currency( region[2] )
        q4 = format_as_currency( region[3] )
        print( f"{number:<8d} {ql:>{w}} {q2:>{w}} {q3:>{w}} {q4:>{w}}" )
    print()

    print( "Sales by region:" )
    for number, region in enumerate( sales, start=1 ):
        total = 0.0
        for quarter in region:
            total += float( quarter )
        total = format_as_currency( total )
        print( f"\tRegion{number}:  {total}" )
    print()

    print( "Sales by quarter: " )
    for number, quarter in enumerate( range (4), start=1) :
        total = 0.0
        for region in range( len( sales ) ):
            total += sales[region][quarter]
        total = format_as_currency( total )
        print ( f"\tQ{number}:    {total}" )
    print()

    #total = 0.0 This somehow becomes a string when outside the loop??
    for region in sales:
        total = 0.0
        for quarter in region:
            total += quarter
        total = format_as_currency( total )
    
    print( f"Total annual sales, all regions: {total}" )

if __name__ == "__main__":
    main()