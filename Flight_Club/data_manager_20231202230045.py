from pprint import pprint  # Importing pprint for pretty printing
import requests  # Importing requests for making HTTP requests

SHEETY_PRICES_ENDPOINT = 'YOUR SHEETY PRICES ENDPOINT'  # Endpoint for prices data in Sheety (replace with your actual endpoint)
SHEETY_USERS_ENDPOINT = 'YOUR SHEETY USERS ENDPOINT'  # Endpoint for users data in Sheety (replace with your actual endpoint)

class DataManager:
    def __init__(self):
        self.destination_data = {}  # Initializing an empty dictionary to store destination data

    def get_destination_data(self):
        # Fetching destination data from Sheety's prices endpoint
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()  # Parsing the response as JSON
        self.destination_data = data["prices"]  # Storing the retrieved data in destination_data
        return self.destination_data  # Returning the destination data

    def update_destination_codes(self):
        # Updating destination codes in Sheety's prices endpoint
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]  # Setting the IATA code for the city
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",  # URL for updating specific city's data
                json=new_data  # Sending updated data in JSON format
            )
            print(response.text)  # Printing the response text after the update

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT  # Endpoint for fetching customer data
        response = requests.get(url=customers_endpoint)  # Sending GET request to retrieve customer data
        data = response.json()  # Parsing the response as JSON
        self.customer_data = data["users"]  # Storing the retrieved customer data
        return self.customer_data  # Returning the customer data
