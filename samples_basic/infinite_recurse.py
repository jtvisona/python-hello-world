# This results in infinte recursion.
def call_self():
    print( "Ctrl+C to halt execution of infinite recursion!" )
    call_self()

call_self()
