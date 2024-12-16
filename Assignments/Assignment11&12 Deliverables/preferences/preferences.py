"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 11&12
preferences.py
"""

from dataclasses import dataclass
import csv
import tkinter as tk

@dataclass
class Preferences():

    def __int__( self ):
        name = ""
        language = ""
        autosave = 0

    @property
    def name( self ):
        return self.name
    @name.setter
    def name( self, value ):
        self.name = value

    @property
    def language( self ):
        return self.language
    @language.setter
    def language( self, value ):
        if not isinstance( value, int ):
            raise ValueError("Name must be an integer")
        self._name = value
    
    @property
    def autosave( self ):
        return self.autosave
    @autosave.setter
    def autosave( self, value ):
        self.autosave = value
    
    def save( self ):
        with open('preferences.csv', mode='w', newline='') as file:
            writer = csv.writer( "preferences.csv" )
            writer.writerows( [ self.name, self.language, self.autosave ] )

def main():
    preferences = Preferences()

    root = tk.Tk()
    root.title( "User Preferences" )

    tk.Label( root, text="Name" ).grid( row=0, column=0 )
    field1 = tk.Entry( root )
    field1.grid( row=0, column=1 )

    tk.Label( root, text="Language" ).grid( row=1, column=0 )
    field2 = tk.Entry( root )
    field2.grid( row=1, column=1 )

    tk.Label( root, text="Autosave" ).grid( row=2, column=0 )
    field3 = tk.Entry( root )
    field3.grid( row=2, column=1 )

    # Define button actions
    def button_action():
        print( "Saving!" )
        preferences.name = field1.get()
        preferences.language = field2.get()
        preferences.autosave = int( field3.get() )
        preferences.save()

    button = tk.Button( root, text="Save", command=button_action)
    button.grid( row=3, column=0 )
    root.mainloop()

if __name__ == "__main__":
    main()