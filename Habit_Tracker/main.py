# Habit Tracker

''' The code is an API interaction script using Python's requests library, creating a user on Pixela, setting 
up a graph to track cycling distance, adding data points to the graph, updating the data, and demonstrating 
how to delete a data point if needed within the Pixela platform. '''

import requests
from datetime import datetime

USERNAME = "YOUR USERNAME"
TOKEN = "YOUR SELF GENERATED TOKEN"
GRAPH_ID = "YOUR GRAPH ID"

pixela_endpoint = "https://pixe.la/v1/users"

# Parameters for creating a new user on Pixela
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# POST request to create a new user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Endpoint for the graph configuration
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Configuration for a new graph
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# POST request to create a new graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

# Pixel data to be added for the current date
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

# POST request to add pixel data to the graph for the current date
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# PUT request to update existing pixel data
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# DELETE request to delete specific pixel data
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
