'''
Open Close Principle states that "Software entities should be open for extension 
and not for Modification"

Here extension means - extend the functionality using a child class
modification means chainging the base class.
'''

## Voilation of Open Close Principle

# class Animal:
#     def __init__(self, name: str):
#         self.name = name
    
#     def get_name(self) -> str:
#         pass

# animals = [
#     Animal("lion"),
#     Animal("horse"),
# ]

# def animal_sound(animals: list):
#     for animal in animals:
#         if animal.name == "lion":
#             print("roar")
#         elif animal.name == "horse":
#             print("neigh")

# animal_sound(animals)

'''
In the above example, we have to modify the animal_sound function
as the animals inceases, this is clear violation of OCP.

When the application incease to say, evey animal present on earth,
the if-else statement will be repeated so many times, and we have to modiy
the function for each new animal. This will make our work tedious.
'''

## Solution to make it conform to OCp

class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        pass

    def make_sound(self) -> str:
        pass

class Lion(Animal):
    def make_sound(self) -> str:
        return "roar"

class Horse(Animal):
    def make_sound(self) -> str:
        return "neigh"

class Snake(Animal):
    def make_sound(self) -> str:
        return "hiss"

def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())

animals = [
    Lion('lion'),
    Lion('tiger'),
    Horse('horse'),
    Snake('snake')
]

animal_sound(animals)

'''
Animal have a virtual function make_sound.
Each animal will extend the Animal class which has it's own make_sound function

Now we have to add new animal animal_sound doesn't have to change.
we just need to add new animal to animals list, and the animal_sound function
will call the make_sound function on the basis of animal.
'''

'''
Another example can be of a store, where own can give different discount rates
to different customers
'''

class Discout:
    def __init__(self, customer_type, price) -> None:
        self.customer_type = customer_type
        self.price = price

    def discounted_price(self) -> float:
        if self.customer_type == 'normal':
            discount = self.price * 0.2
            return self.price - discount

        elif self.customer_type == 'fav':
            discount = self.price * 0.3
            return self.price - discount
'''
Here if we want to add new customer type then we have to modify
the discounted_price method
form example if a family member wants to shop then we have to modify
the discounted_price method and another elif block

This fails the OCP. To solve this instead of modifing the discounted_price
function, we will extend the Discount class
'''

class Discount:
    def __init__(self, customer_type, price) -> None:
        self.customer_type = customer_type
        self.price = price

    def discounted_price(self) -> float:
        if self.customer_type == 'normal':
            discount = self.price * 0.2
            return self.price - discount

class FavDiscout(Discount):
    def discounted_price(self) -> float:
        discount = self.price * 0.3
        return self.price - discount


class FamDiscout(Discount):
    def discounted_price(self) -> float:
        discount = self.price * 0.4
        return self.price - discount

'''
Now the above example follows Open Close principle
'''
