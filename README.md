# cs-361-microservice
Random Player/Game Generator
Generates a random player or game

REQUEST data:
HTTP Get Request

RECIEVE data:
HTTP Response Object


# Example Calls
Random Player:
\nresponse = requests.get("http://127.0.0.1:5001/player")
\nplayer = response.json()[0]
\n
\nRandom Game:
\nresponse = requests.get("http://127.0.0.1:5001/game")
\ngame = response.json()[0]
\n
![image](https://user-images.githubusercontent.com/102342517/219445973-5ddc2772-c6b6-48fa-8390-9d3dc44ad130.png)
