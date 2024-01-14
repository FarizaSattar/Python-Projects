class FlightData:
    def __init__(

        # Initializing FlightData object with specific attributes
        self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date, stop_overs=0, via_city=""):

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
        
        # Number of stopovers for the flight (defaulted to 0)
        self.stop_overs = stop_overs
        
        # City where the flight stops over (if applicable, defaulted to an empty string)
        self.via_city = via_city
