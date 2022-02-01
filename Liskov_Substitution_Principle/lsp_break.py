'''
Liskov Substitution Principle states that

"Objects in a program can be replaceable with instances of their subtypes without
altering the correctness of that program"
'''

# Breaking - Liskov Substitution Principle

class Car:
    def __init__(self, type) -> None:
        self.type = type

class PetrolCar:
    def __init__(self, type) -> None:
        self.type = type

car = Car("SUV")
car.properties = {"Color": "Red", "Gear": "Auto", "Capacity": 6}

petrolcar = PetrolCar("Sedan")
petrolcar.properties = ("Blue", "Manual", 4)


def find_red_car(cars):
    red_car = 0
    for car in cars:
        if car.properties['Color'] == "Red":
            red_car += 1
    print(f'Number of Red cars = {red_car}')

cars = [car, petrolcar]
# this will error as petrol car can not be used as a Car type 
# this will give type error, as Car peoperties as given as dict
# but PetrolCar properties are given as tuple
# so the instance of PetrolCar which is sub class of Car
# cannot replace the instance of Class Car
# Hence breaking Liskov Substituion Principle
find_red_car(cars)