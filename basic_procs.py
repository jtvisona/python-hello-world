# Note the implicit type declarations
def sum1(addened,adder):
    return addened+adder

# Note this has explicit type declarations
def sum2( addened:int, adder:int ) -> int:
    return addened + adder

# Note the return of a pair
def swap(value1,value2):
    return value2,value1

def main():
    value1 = 1
    value2 = 100
    print( f"{value1}, {value2} = ", sum1( value1, value2 ) )
    print( f"{value1}, {value2} = ", sum2( value1, value2 ) )
    value1,value2 = swap( value1, value2 ) # written to make return explicit
    print( f"{value1}, {value2} = ", value1, value2 )

# if this module is called first, call the main function
if __name__ == "__main__":
    main()
