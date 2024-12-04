"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 12-1
game_stats.py
"""

def sort_dict_by_0( players: dict ) -> dict:
    return dict( sorted( players.items(), key=lambda item: item[0] ) )

def display_names( players: dict ) -> None:
    print( "ALL PLAYERS: " )
    for name in players:
        print( name )
    print()

def display_stats( players: dict ) -> None:
    name = input( "Enter a player name: " ).title()
    if name in players.keys():
        player = players[ name ]
        print("Wins: ", player [ "wins" ] )
        print("Losses: ", player [ "losses" ] )
        print("Ties: ", player [ "ties" ] )
    else:
        print( f"There is no player named {name}." )
    print()

def main():
    print( "Game Statistics\n" )
    players = { "Joel": {"wins": 32, "losses": 14, "ties": 17},
               "Elizabeth": {"wins": 41, "losses": 3, "ties": 22},
               "Mike": {"wins": 8, "losses": 19, "ties": 11}
    }

    display_names( sort_dict_by_0( players ) )
    choice = "y"
    while choice.lower() =="y":
        display_stats( players )
        choice = input( "Continue? (y/n): " )
        print()
    print( "Bye!" )

if __name__ == "__main__":
    main()