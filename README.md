# cs-361-microservice
Random Player/Game Generator
Generates a random player or game

REQUEST data:
HTTP Get Request

RECIEVE data:
HTTP Response Object


# Example Calls
Random Player:<br />
response = requests.get("http://127.0.0.1:5001/player") <br />
player = response.json()[0] <br />
<br />
Random Game:<br />
response = requests.get("http://127.0.0.1:5001/game") <br />
game = response.json()[0] <br />
<br />
![image](https://user-images.githubusercontent.com/102342517/219445973-5ddc2772-c6b6-48fa-8390-9d3dc44ad130.png)
