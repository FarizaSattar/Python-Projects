# Flight Deal Finder
''' The code sends the user SMS alerts for flights with prices lower than the specified lowest price for each 
destination. '''

'''
Values to change in code
  1) ORIGIN_CITY_IATA in line 28 to the IATA code for your country
'''

from datetime import datetime, timedelta
from data_manager import DataManager  
from flight_search import FlightSearch  
from notification_manager import NotificationManager  

# Initializing instances of DataManager, FlightSearch, and NotificationManager classes
data_manager = DataManager()

# Retrieving destination data from the data manager
sheet_data = data_manager.get_destination_data()  

# Initializing FlightSearch object
flight_search = FlightSearch()  

# Initializing NotificationManager object
notification_manager = NotificationManager() 

# Setting the IATA code for the origin city (London in this case)
ORIGIN_CITY_IATA = "LON"  

# Checking if the IATA code is missing for the first destination in the sheet data
if sheet_data[0]["iataCode"] == "":
    
    # If the IATA code is missing, obtain and update IATA codes for all destinations
    for row in sheet_data:

        # Getting IATA code for each city
        row["iataCode"] = flight_search.get_destination_code(row["city"])  

    # Updating the destination data with IATA codes
    data_manager.destination_data = sheet_data  

    # Updating the destination codes in the data manager
    data_manager.update_destination_codes()  

# Calculating dates for tomorrow and six months from today
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# Looping through each destination in the sheet data
for destination in sheet_data:
    
    # Checking for flights from the origin city to each destination within the specified date range
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    
    # Sending SMS notification if the flight price is lower than the specified lowest price for the destination
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
