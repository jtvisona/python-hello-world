"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 9
deck-o-cards.py
"""

import random as RND

def create_deck():
    suits = [ 'hearts', 'diamonds', 'clubs', 'spades' ]
    faces = [ '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A' ]

    deck = [ f"{face} of {suit}" for suit in suits for face in faces ]
    RND.shuffle( deck )
    return deck

def deal_cards( deck, num_cards ):
    hand = deck[ :num_cards ]
    del deck[ :num_cards ]
    return hand

def card_dealer():
    deck = create_deck()
    print( "I have shuffled a deck of 52 cards." )
    
    while True:
        num_cards = int( input( "How many cards would you like?: " ) )
        if num_cards > len( deck ):
            print( f"Sorry, there are only {len(deck)} cards left in the deck." )
            continue
        
        hand = deal_cards(deck, num_cards)
        print( "\nHere are your cards:" )
        for card in hand:
            print( card )
        
        print( f"\nThere are {len(deck)} cards left in the deck." )
        
        cont = input("\nGood luck! Would you like to deal more cards? (y/n): ")
        if cont.lower() != 'y':
            break
    
def main():
    card_dealer()
    print( "Go home, buddy! The casino is closed." )

if __name__ == "__main__":
    main()