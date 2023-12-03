# Flight Deal Finder

''' The code retrieves destination data, checks for available flights within a specific date range, compares 
the flight prices with the lowest prices for each destination, and sends email alerts to customers if a 
lower-priced flight is found, considering potential stopovers and associated details. '''

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Define the IATA code for the origin city
ORIGIN_CITY_IATA = "LON"

# Initializing DataManager, FlightSearch, and NotificationManager objects
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Fetching destination data from the data manager
sheet_data = data_manager.get_destination_data()

# Check if the IATA code is missing for the first destination in the sheet data
if sheet_data[0]["iataCode"] == "":
    # Get city names from the sheet data
    city_names = [row["city"] for row in sheet_data]
    
    # Obtain city codes from FlightSearch and update destination codes in DataManager
    data_manager.city_codes = flight_search.get_destination_codes(city_names)
    data_manager.update_destination_codes()
    
    # Update sheet_data with the latest destination data
    sheet_data = data_manager.get_destination_data()

# Create a dictionary of destinations with their respective details
destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data
}

# Define time for searching flights (tomorrow and six months from today)
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)

# Loop through each destination for flight search and comparison
for destination_code in destinations:
    # Check for available flights from the origin city to the current destination within the specified date range
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    
    print(flight.price)  # Print the flight price for debugging
    
    # Continue if no flight is found
    if flight is None:
        continue

    # Compare the flight price with the lowest price for the current destination
    if flight.price < destinations[destination_code]["price"]:
        # Retrieve customer emails from DataManager
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]  # Extract email addresses from user data
        names = [row["firstName"] for row in users]  # Extract first names from user data

        # Compose the email message for the low-price flight alert
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        
        # Add information about stopovers if there are any
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stopover(s), via {flight.via_city}."
        
        # Send email notifications to users via NotificationManager
        notification_manager.send_emails(emails, message)
