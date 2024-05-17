import requests
import json

#This URL is online and used for testing REST API queries.
URL = "https://jsonplaceholder.typicode.com/users"

#This will print out all of the data.
response = requests.get(URL)

print(response.text)

#Now lets prompt the user for a particular user name in the database and print it to the screen.

print("Search by Username:")
user = input("> ")
queryURL = URL + f"?username={user}"
response = requests.get(queryURL)

print(response.text)

#Now lets create a python dictionary that contains the specified user and parse the data and provide some nicely formatted output.

userdata = json.loads(response.text)[0]

name = userdata["name"]
email = userdata["email"]
phone = userdata["phone"]

print(f"{name} can be reached via the following methods: ")
print(f"Email: {email}")
print(f"Phone: {phone}")


