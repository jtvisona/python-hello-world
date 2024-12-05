"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 10
roshambo.py
"""

from dataclasses import dataclass
import random

ROSHAMBO_LIST = ["rock", "paper", "scissors"]

@dataclass
class Player:
    name: str = ""
    roshambo: str = ROSHAMBO_LIST[ 0 ]
    __wins: int = 0

    def generateRoshambo( self ):
        self.__roshambo = ROSHAMBO_LIST[ 0 ]
    
    def play( self, other_player ):
        if self.roshambo == other_player.roshambo:
            return None
        else:
            if self.roshambo == "rock" and other_player.roshambo == "scissors" \
            or self.roshambo == "paper" and other_player.roshambo == "rock" \
            or self.roshambo == "scissors" and other_player.roshambo == "paper":
                return self
            else:
                return other_player
    
    @property
    def wins( self ):
        return self.__wins

    def addWin( self ):
        self.__wins += 1

    def __str__( self ):
        return f"{self.name}: {self.roshambo}"

@dataclass
class Bart( Player ):
    def __post_init__( self ):
        self.name = "Bart"

@dataclass
class Lisa( Player ):
    def __post_init__( self ):
       self.name = "Lisa"

    def generateRoshambo( self ):
       self.roshambo = random.choice( ROSHAMBO_LIST )


def main():
    print( "Rock, Scissors, Paper\n ")
    name = input( "Enter your name: ")
    print()
    player1 = Player( name )
    opponent = input ( "Would you like to play Bart or Lisa? (b/l): ")
    print()
    if opponent.lower() == "b":
        player2 = Bart()
    elif opponent.lower() == "l":
        player2 = Lisa()

    again = "y"
    while again.lower() == "y":
        selection = input ( "Rock, paper, or scissors? (r/p/s): ").lower()
        print ()
        if selection == "r":
            player1.roshambo = "rock"
        elif selection == "p":
            player1.roshambo = "paper"
        elif selection == "s":
            player1.roshambo = "scissors"
        else:
            print( "Invalid choice. Try again.")
            continue

        player2.generateRoshambo ()
        print( player1 )
        print( player2 )
        winner = player1.play( player2 )
        if winner is None:
            print ( "Draw!\n")
        else:
            print( f" {winner.name} wins!\n")
            winner.addWin()
            print( f"{player1.name}: {player1.wins} total win(s)" )
            print( f"{player2.name}: {player2.wins} total win(s)" )
            print()
            again = input( "Play again? (y/n): ")
            print ()
    print ( "Ciao!" )

if __name__ == "__main__":
    main()