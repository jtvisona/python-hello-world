"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 11&12
objects.py
used by ui.py
"""

from dataclasses import dataclass

@dataclass
class Category:
    id:int = 0
    name:str = ""

@dataclass
class Product:
    id:int = 0
    code:str = ""
    name:str = ""
    price:float = 0.0
    category:Category = None



