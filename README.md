# cs-361-microservice
Random User Generator
Generates a random username (email) and password

REQUEST data:
HTTP Get Request

RECIEVE data:
HTTP Response Object


Example -

async function getRandomUser() {
	// send get request to http://127.0.0.1:600/
	const response = await fetch('http://127.0.0.1:6000/')

	// access and return contents of response
	const data = await response.json()
  return data
}

getRandomUser()

returns: { username: 'user41974854@email.com', password: 'W6Z1X8P2G6C5!' } 


![UMLDiagram](https://user-images.githubusercontent.com/102342517/218203242-1318ca36-0305-42ff-837c-7ebe99f3638f.png)
