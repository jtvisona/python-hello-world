#!/usr/bin/env python3

"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 3
order_floats.py
"""
# for keeping track of float values
float_lists = [[ 3.0, 2.0, 1.0 ],
                [ 3.0, 1.0, 2.0 ],
                [ 2.0, 3.0, 1.0 ],
                [ 2.0, 1.0, 3.0 ],
                [ 1.0, 3.0, 2.0 ],
                [ 1.0, 2.0, 3.0 ]]

def sort_two_floats( list_of_floats: float ):
    if list_of_floats[1] < list_of_floats[0]:
        print( "Swapping 1st and 2nd", end="; " )
        temp = list_of_floats[0]
        list_of_floats[0] = list_of_floats[1]
        list_of_floats[1] = temp

def sort_three_floats( list_of_floats: float ):
    # sort first two first; then figure out below where the third belongs
    print( "Inspecting", list_of_floats, end="; " )
    sort_two_floats( list_of_floats )
    print( "Sorted", list_of_floats, end="; " )

    # 3rd is smallest
    if list_of_floats[2] <= list_of_floats[0]:
        print( f"Sorting bc {list_of_floats[2]} <= {list_of_floats[0]}", end="; " )
        temp = list_of_floats[0]
        list_of_floats[0] = list_of_floats[2]
        list_of_floats[2] = list_of_floats[1]
        list_of_floats[1] = temp
        print( f"Postsort: {list_of_floats[0]} {list_of_floats[1]} {list_of_floats[2]};" )
    # 3rd is middle
    elif list_of_floats[2] <= list_of_floats[1]:
        print( f"Sorting bc {list_of_floats[2]} <= {list_of_floats[1]}", end="; " )
        temp = list_of_floats[1]
        list_of_floats[1] = list_of_floats[2]
        list_of_floats[2] = temp
        print( f"Postsort: {list_of_floats[0]} {list_of_floats[1]} {list_of_floats[2]};" )
    # 3rd is 3rd
    else:
        print( f"Postsort: {list_of_floats[0]} {list_of_floats[1]} {list_of_floats[2]};" )

def main():
    # cycle through all of the sublists, sort, and then print the results
    print( "Initial set: ", float_lists )
    for each_sublist in float_lists:
        sort_three_floats( each_sublist )
    print( "Final set: ", float_lists )

if __name__ == "__main__":
    main()
