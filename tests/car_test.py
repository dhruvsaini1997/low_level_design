import unittest
from src.classes_and_objects import Car

class CarTest(unittest.TestCase):
    def setUp(self):
        self.dummy_car = Car("Brand","Model",1999)

    def test_check_car_constructor(self):
        self.assertEqual(self.dummy_car.make,"Brand" )
        self.assertEqual(self.dummy_car.name, "Model")
        self.assertEqual(self.dummy_car.year, 1999)

    def test_start_engine_method(self):
        self.assertEqual(self.dummy_car.start_engine(),"Starting Brand Model's engine!")


if __name__ == "__main__":
    unittest.main()