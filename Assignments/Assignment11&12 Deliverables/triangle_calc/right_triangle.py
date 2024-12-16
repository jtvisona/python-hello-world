"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment n
right_triangle.py
"""

import math
from dataclasses import dataclass
import tkinter as tk

@dataclass
class RightTriangle():
    a: int = 0
    b: int = 0

    @property
    def c( self ):
        c_sq = self.a ** 2 + self.b ** 2
        return math.sqrt( c_sq )
    
def main():
    triangle = RightTriangle()

    root = tk.Tk()
    root.title( "Right Triangle Calculator" )

    tk.Label( root, text="a" ).grid( row=0, column=0 )
    field1 = tk.Entry( root )
    field1.grid( row=0, column=1 )

    tk.Label( root, text="b" ).grid( row=1, column=0 )
    field2 = tk.Entry( root )
    field2.grid( row=1, column=1 )

    tk.Label( root, text="c" ).grid( row=2, column=0 )
    field3 = tk.Entry( root )
    field3.grid( row=2, column=1 )

    # Define button actions
    def button_action():
        triangle.a = int( field1.get() )
        triangle.b = int( field1.get() )
        field3.insert( 0, str( triangle.c ) )

    button = tk.Button( root, text="Calculate", command=button_action)
    button.grid( row=3, column=0 )
    root.mainloop()

if __name__ == "__main__":
    main()