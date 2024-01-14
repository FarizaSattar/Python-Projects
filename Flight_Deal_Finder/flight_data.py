class FlightData:

    # Initializing FlightData object with specific attributes
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):

        # Price of the flight
        self.price = price
        
        # City of origin for the flight
        self.origin_city = origin_city
        
        # Airport code of the origin city
        self.origin_airport = origin_airport
        
        # City of destination for the flight
        self.destination_city = destination_city
        
        # Airport code of the destination city
        self.destination_airport = destination_airport
        
        # Departure date of the flight
        self.out_date = out_date
        
        # Return date of the flight (if applicable)
        self.return_date = return_date
