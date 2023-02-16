# cs-361-microservice
Random Player/Game Generator
Generates a random player or game

REQUEST data:
HTTP Get Request

RECIEVE data:
HTTP Response Object


Example Call -
# Random Player
response = requests.get("http://127.0.0.1:5001/player")
player = response.json()[0]

# Random Game
response = requests.get("http://127.0.0.1:5001/game")
game = response.json()[0]

![image](https://user-images.githubusercontent.com/102342517/219445973-5ddc2772-c6b6-48fa-8390-9d3dc44ad130.png)
