from pprint import pprint
import requests

# Replace 'YOUR SHEETY PRICES ENDPOINT' with your actual Sheety prices endpoint
SHEETY_PRICES_ENDPOINT = 'YOUR SHEETY PRICES ENDPOINT'

class DataManager:

    def __init__(self):
        self.destination_data = {}  # Initializing an empty dictionary to store destination data

    def get_destination_data(self):
        # Sending a GET request to retrieve destination data from the Sheety endpoint
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()  # Parsing the response as JSON
        self.destination_data = data["prices"]  # Storing the retrieved data in the destination_data dictionary
        return self.destination_data  # Returning the destination data

    def update_destination_codes(self):
        # Iterating through each city in the destination data
        for city in self.destination_data:
            # Creating a new dictionary with 'iataCode' key-value pair
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            # Sending a PUT request to update the 'iataCode' for the city
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)  # Printing the response after updating the 'iataCode'
