# Define a class named Car
class Car:
    # Constructor to initialize the attributes of the Car class
    def __init__(self, make, name, year):
        self.make = make  # Brand of the car (e.g., Toyota, BMW)
        self.name = name  # Model name of the car (e.g., Camry, Series 5)
        self.year = year  # Year of manufacture

    # Method to simulate starting the car's engine
    def start_engine(self):
        print(f"Starting {self.make} {self.name}'s engine!")

# Example of creating Car objects and calling the start_engine method
# toyota_camry = Car("Toyota", "Camry", 2007)  # Create a Toyota Camry car object
# toyota_camry.start_engine()  # Call the start_engine method for Toyota Camry

# BMW_series5 = Car("BMW", "Series 5", 2007)  # Create a BMW Series 5 car object
# BMW_series5.start_engine()  # Call the start_engine method for BMW Series 5
