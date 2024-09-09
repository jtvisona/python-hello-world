# Four ways to iterate through lists

list_of_foods = [ "apples", "carrots", "eggplants", "bananas" ]
print( "Unsorted: ", end=" " )
for each_food in list_of_foods:
    print( each_food, end=" " )
print()

list_of_foods.sort()
print( "Sorted: ", end=" " )
for index, each_food in enumerate(list_of_foods,start=1): # Enumerate creates KVPs of type <int,type>
    print( f"{index}:{each_food}", end=" " )
print()

list_of_digits = [ "one", "two", "three", "four", "five" ]
index = 0
print( "Indexed:", end=" " )
while index < len( list_of_digits ):
    print( index+1, ":", list_of_digits[index], end=" " ) # Note that enumerate is not used and index must be manually created
    index += 1
print()

list_of_ints = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
print( "Printed list:", end=" " )
perfect_squares = [ integer**2 for integer in list_of_ints ] # Uses a comprehension
print( perfect_squares )







