from flask import Flask
import random
import csv

app = Flask(__name__)

@app.route("/player")
def random_player():
    with open('players.csv', 'r') as infile:
        players = list(csv.reader(infile, delimiter=","))

    return players[random.randint(0, len(players)-1)]

@app.route("/game")
def random_game():
    with open('games.csv', 'r') as infile:
        games = list(csv.reader(infile, delimiter=","))

    return games[random.randint(0, len(games)-1)]

if __name__ == "__main__":
    app.run(debug=True, port=5001)
