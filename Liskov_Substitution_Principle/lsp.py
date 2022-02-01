'''
Liskov Substitution Principle states that

"Objects in a program can be replaceable with instances of their subtypes without
altering the correctness of that program"
'''

'''
The better way to implement LSP is to use setter and getter methods inside the super class
"Car" instead of leaving that implementation to the individual devlopers
This way we can get the properties using the setter method  and its implementation remains
internal to super class
'''

class Car:
    def __init__(self, type) -> None:
        self.type = type
        self.car_properties = {}

    def set_properties(self, color, gear, capacity) -> None:
        self.car_properties = {"Color": color, "Gear": gear, "Capacity": capacity}

    def get_properties(self) -> dict:
        return self.car_properties

class PetrolCar(Car):
    def __init__(self, type) -> None:
        # super().__init__(type)
        self.type = type
        self.car_properties = {}

car = Car("SUV")
car.properties = {"Color": "Red", "Gear": "Auto", "Capacity": 6}
print(car.properties)

petrolcar = PetrolCar("Sedan")
petrolcar.properties = ("Blue", "Manual", 4)
print(petrolcar.properties)

def find_red_car(cars):
    red_car = 0
    for car in cars:
        if car.get_properties()['Color'] == "Red":
            red_car += 1
    print(f'Number of Red cars = {red_car}')

cars = [car, petrolcar]