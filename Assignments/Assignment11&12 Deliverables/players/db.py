"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 11&12
db.py for players
"""

import sqlite3
from contextlib import closing

from objects import Player

conn = None

def connect():
    global conn
    if not conn:
        DB_FILE = "Assignments\\Assignment11&12 Deliverables\\players\\player_db.sqlite"
        print( "Connectioning!" )
        try:
            #conn = sqlite3.connect( DB_FILE, uri=True, flags=sqlite3.OPEN_READWRITE )
            conn = sqlite3.connect( DB_FILE )
            conn.row_factory = sqlite3.Row
            print("Connection successful!")
        except sqlite3.Error as e:
            print(f"Connection error: {e}")


def close():
    if conn:
        conn.close()

def get_players():
    query = '''SELECT playerID, name, wins, losses, ties
               FROM Player ORDER BY wins DESC'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    players = []
    for row in results:
        player = Player(row["name"], row["wins"],
                        row["losses"], row["ties"], row["playerID"])
        players.append(player)
    return players

def get_player(name):
    query = '''SELECT playerID, name, wins, losses, ties
               FROM Player WHERE name = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (name,))
        row = c.fetchone()
        if row:
            player = Player(row["name"], row["wins"],
                            row["losses"], row["ties"], row["playerID"])
            return player
        else:
            return None

def add_player(player):
    sql = '''INSERT INTO Player (name, wins, losses, ties) 
             VALUES (?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (player.name, player.wins, player.losses, player.ties))
        conn.commit()

def delete_player(name):
    sql = '''DELETE FROM Player WHERE name = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (name,))
        conn.commit()

def main():
    connect()
    players = get_players()
    for player in players:
        print(player.name, player.id, player.wins,
              player.losses, player.ties, player.getGames())
    print()
    
    player = get_player("Mike")
    print(player.name, player.id, player.wins,
          player.losses, player.ties, player.getGames())

if __name__ == "__main__":
    main()
