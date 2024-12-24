# Import the Car class from the classes_and_objects module
from classes_and_objects import Car

# Entry point for the script
if __name__ == "__main__":
    # Create an instance of the Car class with the specified make, name, and year
    honda_crv = Car("Honda", "CRV", 2024)

    # Call the start_engine method to simulate starting the car's engine
    honda_crv.start_engine()
