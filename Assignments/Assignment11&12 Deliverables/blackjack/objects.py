"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 11&blackjack.py
This is a library for the main application.
"""

import random
from dataclasses import dataclass

@dataclass
class Card:
    rank: str
    suit: str
    value: int

def __str__( self ):
    return f"{self.rank} of {self.suit}"

@dataclass
class Deck:

    def __init__( self ):
        self.__deck = []
        ranks = ( "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "Jack", "Queen", "King" )
        suits = ( "Clubs", "Diamonds", "Hearts", "Spades" )

        for suit in suits:
            for rank in ranks:
                if rank == "Ace":
                    value = 11
                elif rank == "Jack" or rank == "Queen" or rank == "King":
                    value = 10
                else:
                    value = int( rank )

                self.__deck.append( Card ( rank, suit, value ) )

    @property
    def count( self ):
        return len( self.__deck )

    def shuffle( self ):
        random.shuffle( self.__deck )

    def dealCard( self ):
        return self.__deck.pop()

    def __iter__( self ):
        for card in self.__deck:
            yield card

@dataclass
class Hand:
    def __init__( self ):
        self.__cards = []

    def addCard( self, card ):
        self.__cards.append( card )

    @property
    def count( self ):
        return len( self.__cards )
    
    @property
    def points( self ):
        points = 0
        for card in self.__cards:
            points += card.value
    
        if points > 21:
            ace_count = 0
            for card in self.__cards:
                if card.rank == "Ace":
                    ace_count += 1
            points = points - (ace_count * 10)
        return points

    @property
    def isBlackjack( self ):
        return self.count==2 and self.points == 21
    
    @property
    def isBusted( self ):
        return self.points > 21
    
    def __iter__( self ):
        for card in self.__cards:
            yield card
    
def main():
    print( "Cards Tester\n" )
    print( "Deck" )
    deck = Deck()
    for card in deck:
        print( card )
    deck.shuffle()
    print( "Deck count:", deck.count, "\n" )
    print( "Hand" )
    hand = Hand()
    for i in range( 4 ):
        hand.addCard( deck.dealCard() )
    for card in hand:
        print( card )
    print( "Hand points:", hand.points )
    print( "Hand count:", hand.count )
    print( "Deck count:", deck.count, "\n")

if __name__ == "__main__":
    main()