list_of_floats = [1.2, 2.1, 3.5, 1.2]
print( list_of_floats)
value_to_locate = 1.2

# find first incident of value
if value_to_locate in list_of_floats:
    print( list_of_floats.index(value_to_locate) )

# find all incidents of value using a comprehension
indices = [index for index, search_value in enumerate(list_of_floats) if search_value == value_to_locate]
print( indices )

# Is there a way to do this with the index function and additional arguments?