"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 9
rectangle.py
"""

def draw_rectangle( height, width ):
    print( '*' + ' *' * width )
    # use anon variable since just creating ASCII graphics
    for _ in range( height - 2 ):
        print( '*' + ' ' * ( 2 * width - 1 ) + '*' )
    print( '*' + ' *' * width )

def rectangle_calculator():
    height = int( input( "Height: " ) )
    width = int( input( "Width: " ) )
    perimeter = 2 * ( height + width )
    area = height * width
    print( f"Perimeter: {perimeter}" )
    print( f"Area: {area}" )
    draw_rectangle( height, width )

def main():
    # continue to loop until user finished
    choice = "y"
    while choice.lower() == "y":
        rectangle_calculator()
        choice = input( "Again? (y/n): ")

if __name__ == "__main__":
    main()