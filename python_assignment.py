class Flight:

    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

    def __str__(self):
        return f"Flight ID: {self.flight_id}, Source: {self.source}, Destination: {self.destination}, Price: {self.price}"
    
    def __repr__(self):
        return f"Flight ID: {self.flight_id}, Source: {self.source}, Destination: {self.destination}, Price: {self.price}"
    
if __name__ == "__main__":

    flights = [
        Flight("AI161E90", "BLR", "BOM", 5600),
        Flight("BR161F91", "BOM", "BBI", 6750),
        Flight("AI161F99", "BBI", "BLR", 8210),
        Flight("VS171E20", "JLR", "BBI", 5500),
        Flight("AS171G30", "HYD", "JLR", 4400),
        Flight("AI131F49", "HYD", "BOM", 3499)
    ]

    print("Name: Divesh Saini")
    print("Roll no: E22CSEU1471")

    while(True):

        print("1. Flights for a particular City")
        print("2. Flights From a city")
        print("3. Flights between two given cities")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice < 1 or choice > 4:
            print("Invalid choice")
            continue

        if choice == 4:
            print("-" * 50)
            break

        found = False
        if choice == 1:
            city = input("Enter city: ")
            found = False

            for flight in flights:
                if flight.source == city.upper() or flight.destination == city.upper():
                    found = True
                    print(flight)

        if choice == 2:
            city = input("Enter city: ")
            for flight in flights:
                if flight.source == city.upper():
                    found = True
                    print(flight)

        if choice == 3:
            source = input("Enter source: ")
            destination = input("Enter destination: ")
            for flight in flights:
                if flight.source == source.upper() and flight.destination == destination.upper():
                    found = True
                    print(flight)

        if not found:
            print("No flights found")

        print("-" * 50)