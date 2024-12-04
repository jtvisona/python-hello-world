"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 8
birthday_calc.py
"""

from datetime import datetime as DT_DATETIME
from sys import exit as SYS_EXIT

def get_name_and_bday() -> dict:
    profile = { "name": None, "bday": None }
    profile[ 'name' ] = input( "Enter a name: " )
    profile[ 'bday' ] = input( "Enter a birth date (YYYY-MM-DD): " )
    return profile

def get_bday_info( profile: dict ) -> dict:
    profile[ 'birth_date' ] = birth_date = DT_DATETIME.strptime( profile[ 'bday' ], "%Y-%m-%d" )
    profile[ 'today'] = today = DT_DATETIME.today()
    profile[ 'age' ] = age = today.year - birth_date.year - ( (today.month, today.day) < ( birth_date.month, birth_date.day ) )
    profile[ 'next_birthday' ] = next_birthday = birth_date.replace( year=today.year )
    if today > next_birthday:
        profile[ 'next_birthday' ] = next_birthday = next_birthday.replace( year = today.year + 1 )
    profile[ 'days_until' ] = days_until = ( next_birthday - today ).days
    return profile

def print_profile( profile: dict ) -> None:
    final_msg = f"""{profile[ 'name' ]}'s birthday is {profile[ 'birth_date' ].strftime('%Y-%m-%d')}! John's next birthday is in {profile[ 'days_until' ]} days."""

    print( f"Name: {profile[ 'name' ]}" )
    print( f"Birthday: {profile[ 'birth_date' ].strftime('%Y-%m-%d')}" )
    print( f"Today's Date: {profile[ 'today' ].strftime('%Y-%m-%d')}" )
    print( f"Age: {profile[ 'age' ]}" )
    print( f"Days until next birthday: {profile[ 'days_until' ]}" )
    print( final_msg )
    print()

def main():
    print( "Birthday Application" )
    print_profile( get_bday_info( get_name_and_bday() ) )


if __name__ == "__main__":
    main()