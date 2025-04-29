class Animal:
    def sound(self):
        print("Animal generic sound")

class Dog(Animal):
    def sound(self):
        print("Woof woof")

class Cat(Animal):
    def sound(self):
        print("Meow meow")

animal = Animal()
animal.sound()

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()

class Vehicle:
    def __init__(self, make, module, year):
        self.make = make
        self.module = module
        self.year = year

    def displayinfo(self):
        print(f"{self.make}, Module : {self.module}, Year : {self.year}")

class Car(Vehicle):
    def __init__(self, make, module, year, body_module):
        super().__init__(make, module, year)
        self.body_module = body_module

class ElectricCar(Car):
    def __init__(self, make, module, year, body_module, battery_capacity):
        super().__init__(make, module, year, body_module)
        self.battery_capacity = battery_capacity

    def charge(self):
        print("Charging the ev")

tesla = ElectricCar ("Tesla", "Modul X", 2023, "Triangle", 122.4)
tesla.displayinfo()
print(tesla.body_module)

list_length = len("Hello World")
print(list_length)

list_numbers = len([1, 2, 3, 4])
print(list_numbers)

sum_of_num = sum([1,2,3,4,5])
print(sum_of_num)

max_of_num = max([1,2,3,4,5])
print(max_of_num)

import math
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
circle = Circle(5)
print("Area of the circle is", circle.area())