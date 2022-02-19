class Carrier: # Define your class here
    all_carriers = [] # Class variable: list that will hold your carriers
    overseer = "Federal Aviation Administration" # Class variable

    def __init__(self, year, name, city):
        self.year = year
        self.name = name
        self.city = city
        self.flights = [] # List of flights
        self.total_workers = 0 # Workforce for this carrier
        Carrier.all_carriers.append(self) # Add this carrier

class Flight:
    def __init__(self, number, starting_city, ending_city):
        self.number = number
        self.starting_city = starting_city
        self.ending_city = ending_city


