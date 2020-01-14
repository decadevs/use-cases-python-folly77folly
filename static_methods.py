# Document at least 3 use cases of static methods
# A method that doesn't have class or self as argument
class Laptop:
    def __init__(self, name, year_of_model):
        self.name = name
        self.year_model=year_of_model

    @staticmethod
    def is_new(year):
        if year > 2015 :
            return True
        else:
            return False


print(Laptop.is_new(2017))


# Reformating a date string 
from datetime import date
class Dates:
    def __init__(self, Date):
        pass

    @staticmethod
    def dates_to_dot(my_date):
        return my_date.replace('/','.')


my_date = ('2020/1/14')
print(Dates.dates_to_dot(my_date))
print(my_date)


class Vehicle:
    def __init__(self, color, name, km, hour):
        self.name = name
        self.color = color
        self.distance = km
        self.hour = hour
    
    def dis_travelled (self):
        return self.distance * hour 
    
    @classmethod
    def production_date():
        pass
    
class Motor(Vehicle):
    def __init__(self, color, name, km, hour, passenger):
        super().__init__(color, name, km, hour)
        self.passenger = passenger

    def dis_travelled(self):
        return self.passenger * self.distance


sport_car = Motor('red', 'toyota', 1000, 1, 4)
print(sport_car.passenger)
print(sport_car.dis_travelled())
        





