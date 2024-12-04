"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 8
champion_counter.py
"""

import csv
import sys

YEAR = 0
COUNTRY = 1

FILENAME = r"C:\Users\17082\Documents\github-repos\python-hello-world\Assignments\Assignment8 Deliverables\world_cup_champions.txt"

def read_champions( champions: dict ) -> dict:
    try:
        with open( FILENAME, newline="" ) as file:
            reader = csv.reader( file )
            print( "reading rows: " )
            for row in reader:
                year = row[ YEAR ]
                country = row[ COUNTRY ]
                print( ".", end="" )
                if country in champions:
                    data = champions[ country ]
                    data[ YEAR ] += 1
                    data[ COUNTRY ].append( year )
                else:
                    if country.lower() == "country":
                        pass
                    else:
                        count = 1
                        years = []
                        years.append( year )
                        data = [ count, years ]
                        champions[ country ] = data
        print()
    except Exception as e:
        #debug print( f"read_champions error: {e}" )
        sys.exit()
    return champions

def main():
    champions = read_champions( champions = {} )

    print( "FIFA World Cup Winners\n" )

    w1 = 15; w2 = 5
    print( f"{'Country':{w1}} {'Wins':{w2}} {'Years':{w1}}" )
    print( f"{'='*7:{w1}} {'='*4:{w2}} {'='*5:{w1}}" )

    countries = list( champions.keys() )
    countries.sort()
    print( countries )

    for country in countries:
        data = champions[ country ]
        count = data[ YEAR ]
        years = data[ COUNTRY ]
        years_str = ""
        for year in years:
            years_str += year + ", "
        years_str = years_str[ :-2 ]
        print( f"{country:{w1}} {count:<{w2}d} {years_str:{w1}}" )

if __name__ == "__main__":
    main()