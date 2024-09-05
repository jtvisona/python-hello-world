# Create a number at random
import random
temp_number = random.randint( 1, 1000 )
print( temp_number,end=" ∈ " )

# Determine which segment of the number line the integer is on
if temp_number >= 10 and temp_number <= 100:
    print( "[10,100]" )
elif temp_number < 10:
    print( "(NegInf,10)" )
else:
    print( "(100,PosInf)" )

