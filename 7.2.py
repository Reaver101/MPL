class Vehicle: 
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.available = True

class RentalAgency: 
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(vehicle.name, "Added to agency")

    def display_vehicles(self):
        print("\nAvailable vehicles: ")

        for vehicle in self.vehicles:
            if vehicle.available:
                print(vehicle.name, "-", vehicle.price, "Per day")

    def rent_vehicle(self, vehicle, customer, days):
        if vehicle.available:
            vehicle.available = False

            total = vehicle.price * days

            print("\nRental Successful")
            print("Customer: ", customer)
            print("Vehicle: ", vehicle.name)
            print("Rental period:", days, " days")
            print("Total Price =", total)
        else: 
            print(vehicle.name, "is not available")

car1 = Vehicle("F1 Redbull", 1000000)
car2 = Vehicle("Ferrari carrera", 200000)
car3 = Vehicle("Porsche 911", 400000)
car4 = Vehicle("Lamborghini", 25)

agency = RentalAgency()

agency.add_vehicle(car1)
agency.add_vehicle(car2)
agency.add_vehicle(car3)
agency.add_vehicle(car4)

agency.display_vehicles()
