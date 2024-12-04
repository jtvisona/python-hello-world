"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 5&6
mailing_list.py
"""

import csv
import sys
import os

print( "Welcome the the Email List Cleaner\n\n" )
#print( f"{os.getcwd()}"); sys.exit()

input_name = "Assignments\\Assignment5&6 Deliverables\\prospects.csv"
output_name = "Assignments\\Assignment5&6 Deliverables\\prospects_clean.csv"

print( f"Source list: {input_name} Cleaned list: {output_name}" )

with open( input_name, "r", newline="" ) as input_file,\
    open( output_name, "w", newline="" ) as output_file:
    
    #print( f"{type(input_file)=} {type(output_file)=}"); sys.exit()
    # don't scramble the file's name with the file!
    reader = csv.reader( input_file )
    writer = csv.writer( output_file, quoting=csv.QUOTE_ALL )

    print( "Cleaning rows" )
    for each_row in reader:
        tmp_row = []
        print( f"Cleaning *shububub*: '{each_row}'" )
        tmp_row.append( each_row[0].strip().title() )
        tmp_row.append( each_row[1].strip().title() )
        tmp_row.append( each_row[2].strip().lower() )
        print( f"Cleaned! '{tmp_row}'" )
        writer.writerow( tmp_row )
    print( "Rows have been cleaned" )