"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 9
customer_viewer.py
"""

import csv as CSV

FILE = "Assignments\Assignment9 Deliverables\customers.csv"
CUSTOMERS = {}

class Customer():

    def __init__( self, id, name, company, address ):
        self.id = id
        self.name = name
        self.company = company
        self.address = address

    def get_data( self ):
        id = self.id
        name = self.name
        company = self.company
        address = self.address

        return f"id:{id} name:{name} company:{company} address:{address}"


def read_customer_file( file_name ):
    with open( file_name, mode='r' ) as file: 
        csv_reader = CSV.DictReader( file )
        customer_data = {}
        for row in csv_reader:
            customer_data[ 'name' ] = row[ 'first_name' ] + " " + row[ 'last_name' ]
            customer_data[ 'company' ] = row[ 'company_name' ]
            customer_data[ 'address' ] =  row[ 'city' ] + " " + row[ 'state' ] + " " + row[ 'zip' ]
            obj_address = Customer( row[ 'cust_id' ], customer_data[ 'name' ], customer_data[ 'company' ], customer_data[ 'address' ] )
            customer_data[ 'cust_add' ] = obj_address
            # make sure to use int as primary key of record!
            CUSTOMERS[ int( row[ 'cust_id' ] ) ] = customer_data

def customer_viewer():
    read_customer_file( FILE )

    while True:
        target_id = int( input( "Enter customer ID: " ) )
        if target_id in CUSTOMERS:
            
            #print( f"\n{customer['name']}\n{customer['address']}\n{customer['city']}\n" )
            print( f"ID:{target_id} found. Creating local dictionary and reference to object for access." )
            customer_record = CUSTOMERS[ 101 ]
            customer_obj = customer_record[ 'cust_add' ]
            #print( type( CUSTOMERS[ 101 ] ) )
            #print( CUSTOMERS[ 101 ] )
            #print( customer_record[ 'name' ] )
            print( customer_obj.get_data() )

        else:
            print( "\nNo customer with such an ID.\n" )

        cont = input( "Continue? (y/n): " )
        if cont.lower() != 'y':
            break

def main():
    customer_viewer()
    print( "Ciao!" )

if __name__ == "__main__":
    main()