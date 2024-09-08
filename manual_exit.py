import sys

while True:
    exit_input = input( "Do you wish to exit manually? (y/n) " )
    exit_input.lower()

    if( exit_input == "y" ):
        sys.exit() # requires 'import sys'

print( "This string will never print." )

