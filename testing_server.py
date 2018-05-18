import requests


text = "I am looking for a mexican resturant in my area"
response = requests.get("http://localhost:5000/parse",params={"q":text})
response = response.json()
intent = response["intent"]

print(response)
