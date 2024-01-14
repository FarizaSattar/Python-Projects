from pprint import pprint  
import requests  

# Endpoint for prices data in Sheety (replace with your actual endpoint)
SHEETY_PRICES_ENDPOINT = 'YOUR SHEETY PRICES ENDPOINT'  

# Endpoint for users data in Sheety (replace with your actual endpoint)
SHEETY_USERS_ENDPOINT = 'YOUR SHEETY USERS ENDPOINT'  

class DataManager:
    def __init__(self):
        
        # Initializing an empty dictionary to store destination data
        self.destination_data = {}  

    def get_destination_data(self):
        # Fetching destination data from Sheety's prices endpoint
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        
        # Parsing the response as JSON
        data = response.json()  

        # Storing the retrieved data in destination_data
        self.destination_data = data["prices"]  

        # Returning the destination data
        return self.destination_data  

    def update_destination_codes(self):
        # Updating destination codes in Sheety's prices endpoint
        for city in self.destination_data:
            new_data = {
                "price": {

                    # Setting the IATA code for the city
                    "iataCode": city["iataCode"]  
                }
            }
            response = requests.put(

                # URL for updating specific city's data
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", 

                # Sending updated data in JSON format
                json=new_data  
            )

            # Printing the response text after the update
            print(response.text)  

    def get_customer_emails(self):

        # Endpoint for fetching customer data
        customers_endpoint = SHEETY_USERS_ENDPOINT  

        # Sending GET request to retrieve customer data
        response = requests.get(url=customers_endpoint)  
        # Parsing the response as JSON
        data = response.json()  
        # Storing the retrieved customer data
        self.customer_data = data["users"] 
        # Returning the customer data
        return self.customer_data  
