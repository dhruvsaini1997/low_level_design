# A class is a blueprint for creating objects.
# It defines the attributes (properties) and methods (functions) of objects.
# An object is an instance of a class, representing a specific entity with its own data.

# Define a class named Car (PascalCase)
class Car:
    # Constructor to initialize the attributes of the Car class
    def __init__(self, make, name, year):
        self.make = make  # Brand of the car (e.g., Toyota, BMW)
        self.name = name  # Model name of the car (e.g., Camry, Series 5)
        self.year = year  # Year of manufacture

    # Method to simulate starting the car's engine (snake_case for method name)
    def start_engine(self):
        return f"Starting {self.make} {self.name}'s engine!"
