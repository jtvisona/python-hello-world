"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 10
creator.py
"""

from dataclasses import dataclass

@dataclass
class Person:
    f_name: str
    l_name: str
    email_add: str

    @property
    def full_name( self ):
        return f"{self.f_name.title()} {self.l_name.title()}"

@dataclass
class Customer( Person ):
    number: str

@dataclass
class Employee( Person ):
    ssn: str

def main():
    print( "Customer/Employee data entry\n" )

    choice = "y"
    while choice.lower() == "y":
        selection = input( "Customer or employee (c/e): " )
        print()

        if selection == "c" or selection == "e":
            person = get_input( selection )
            print()
            display( person )
        else:
            print( "Bad choice, boss!" )
            continue

        choice = input( "Again? (y/n): " )
        print()

def get_input( choice ):
    print( "DATA ENTRY" )
    first_name = input( "First name: " )
    last_name = input( "Last name: " )
    email = input( "Email: " )
    if choice == "c":
        number = input( "Number: " )
        return Customer( first_name, last_name, email, number)
    elif choice == "e":
        ssn = input( "SSN: " )
        return Employee (first_name, last_name, email, ssn)
    
def display( person ):
    if isinstance( person, Customer ):
        print( "CUSTOMER" )
    elif isinstance( person, Employee ):
        print( "EMPLOYEE" )
    else:
        print( "PERSON" )

    print( "Person:\t", person.full_name )
    print( "Email:\t", person.email_add )
    if isinstance( person, Customer ):
        print( "Number:\t", person.number )
    elif isinstance( person, Employee ):
        print ( "SSN:\t", person.ssn )
    print()

if __name__ == "__main__":
    main()