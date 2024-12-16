"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 11&12
customers.py
"""

import sys
import os
from pathlib import Path
import csv
import sqlite3
from contextlib import closing

csv_file = Path( "Assignments\\Assignment11&12 Deliverables\\customers\\customers.csv" )
print( csv_file.exists() )
db_file = Path( "Assignments\\Assignment11&12 Deliverables\\customers\\customers.sqlite" )
print( db_file.exists() )
table_name = "Customer"

print( "Customer Data Importer\n" )
print( "CSV file:   ", csv_file )
print( "DB file:    ", db_file )
print( "Table name: ", table_name, "\n" )

print( "Connectioning!" )
try:
    conn = sqlite3.connect( db_file ) # remember this autogens a file if none exists!
    conn.row_factory = sqlite3.Row
    print("Connection successful!")
except sqlite3.Error as e:
    print(f"Connection error: {e}")

""" DEBUG
# Generate list of database tables
cursor = conn.cursor()
cursor.execute( "SELECT name FROM sqlite_master WHERE type='table';" )
tables = cursor.fetchall()
print( "Tables:", end="" )
for table in tables:
    print( table[0], "," )
cursor.close()
conn.close()
sys.exit()
"""

# delete old rows in database
with closing( conn.cursor() ) as c:
    sql =  '''DELETE FROM Customer'''
    c.execute( sql )
    conn.commit()
print( f"All rows deleted from {table_name} table." )

sql = '''INSERT INTO Customer
            (firstName, lastName, companyName, address, city, state, zip)
         VALUES
             (?, ?, ?, ?, ?, ?, ?)'''

print( "Opening CSV and reading for insertion" )
with open( csv_file, "r", newline='' ) as infile:
    reader = csv.reader(infile)
    count = 0
    for row in reader:
        if count == 0:
            pass
        else:
            first =    row[ 0 ].strip()
            last =     row[ 1 ].strip()
            company =  row[ 2 ].strip()
            address =  row[ 3 ].strip()
            city =     row[ 4 ].strip()
            state =    row[ 5 ].strip()
            zip =      row[ 6 ].strip()
    
            with closing( conn.cursor() ) as c:            
                c.execute(sql, (first, last, company, address, city, state, zip))
        
        count += 1
        # print( "Count:", count) # for debugging

conn.commit()
conn.close()

print( f"{count-1} row(s) inserted into Customer table." )
