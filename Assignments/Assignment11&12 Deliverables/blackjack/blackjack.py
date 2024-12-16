"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 11&12
blackjack.py
"""

import random
from objects import Card, Deck, Hand

deck = Deck()
deck.shuffle()
dealer_hand = Hand()
player_hand = Hand()

def play (deck, player_hand):
    while True:
        choice = input( "Hit or stand? (h/s): " ).lower()
        print()
        if choice == "h":
            player_hand.addCard( deck.dealCard() )
            display_cards( player_hand, "Your Hand: " )
            if player_hand.points >= 21:
                break
        elif choice == "s":
                break
        else:
            print( "Not a valid choice. Try again." )
        return player_hand
        
def display_cards( hand, title ):
        print( title.upper() )
        for card in hand:
            print( f"\t{card}" )
        print()

def display_card( card, title ):
        print( title.upper() )
        print( f"\t{card}\n" )

def main():
    print( "Blackjack" )
    print()
    deck = Deck()
    deck.shuffle()

    dealer_hand = Hand()
    player_hand = Hand()
    
    again = "y"
    while again.lower() == "y":
    # get player and dealer hands
        player_hand.addCard( deck.dealCard() )
        player_hand.addCard( deck.dealCard() )
        dealer_hand.addCard (deck.dealCard() )
        show_card = deck.dealCard()
        display_card( show_card, "Dealer's show card: " )
        display_cards( player_hand, "Your Hand: " )
        
        if dealer_hand.isBlackjack or player_hand.isBlackjack:
            display_cards( dealer_hand, "Dealer's Hand: " )
        else:
            player_hand = play( deck, player_hand )
            if not player_hand.isBusted:
                while dealer_hand.points < 17:
                    dealer_hand.addCard( deck.dealCard() )
                    display_cards( dealer_hand, "Dealer's Hand: " )
                print( f"Your Points:{player_hand.points}" )
                print( f"Dealer's Points: {dealer_hand.points}\n" )

        if player_hand.isBusted:
            print( "You busted. You lose." )
        elif dealer_hand.isBusted:
            print( "The dealer busted. You win." )
        else:
            if player_hand.isBlackjack:
                if dealer_hand.isBlackjack:
                    print( "Dealer has blackjack also. Push." )
                else:
                    print( "Blackjack. You win." )
            elif player_hand.points > dealer_hand.points:
                print( "You win." )
            elif player_hand.points == dealer_hand.points:
                print( "You push." )
            elif player_hand.points < dealer_hand.points:
                print( "You lose." )
            else:
                print( "Application error. Contact your developer.\n" )
        
        again = input( "Play again? (y/n): " ).lower()
        print()
        print( "Ciao.\n" )
        
if __name__ == "__main__":
    main()
