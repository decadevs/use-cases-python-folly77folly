# Document at least 3 use cases of class methods

#It Can be used to change or overwrite a class variable all instances
#of that class will automatically have the
class Vehicle:
    wheels = 4

    @classmethod
    def change_wheels(cls, number):
        cls.wheels = number

print(Vehicle.wheels)
Vehicle.change_wheels(10)
print(Vehicle.wheels)


# can be used as a constructor for object instantiation as 
class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius  

    @classmethod
    def create_circle(cls, diameter):
        return cls(diameter / 2)
    

my_circle = Circle(2)
my_circle2 = Circle.create_circle(4)

print(my_circle.radius)
print(my_circle.diameter)
print(my_circle2.radius)
# print(my_circle2.diameter)


# date time class in python uses class method to create an object
# using different parameters
from datetime import datetime

my_date = datetime(2020,1,14)
my_date2 = datetime.today()


print(my_date)
print(my_date2)


    




