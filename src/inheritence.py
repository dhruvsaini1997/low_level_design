class Vehicle:
    def __init__(self, color):
        self.color = color

    def honk(self):
        print("Honk Honk!")

class Car(Vehicle):
    def __init__(self, color, manufacturing_year):
        super().__init__(color)
        self.manufacturing_year = manufacturing_year

    def get_manufacturing_year(self):
        print(self.manufacturing_year)




if __name__ == '__main__':
    car_obj = Car("Red", 1997)
    car_obj.honk()