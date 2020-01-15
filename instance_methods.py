# Document at least 3 use cases of instance methods

#to create a class to calculate area of a circle
from math import pi
class Circle:
    try:
        from math import pi


        def __init__(self, radius = 1):
            self.radius = radius
            self.diameter = 2 * self.radius

        def area(self):
            return pi * (self.radius ** 2)

        
    except Exception as e:
        raise (e)


# c = Circle(2)
# print(c.diameter)
# print(c.area())

#no2
class Score:
    def __init__(self, score1, score2):
        self.score1 = score1
        self.score2 = score2
    
    def get_avg(self):
        return (self.score1 + self.score2)/2

student=Score(6, 9)
print(student.get_avg())

#no3
class Student:
    no_of_student = 0

    def __init__(self, firstname, lastname, age, sex, dob):
        self.firstname = firstname
        self.lastname =lastname
        self.age = age
        self.sex = sex
        self.dob = dob
        Student.no_of_student += 1

    def get_name(self):
        return self.firstname + ' ' + self.lastname
    
pupil = Student('Tolu','Ola', 25, 'Male', '10/feb/1991')
pupil1 = Student('sola','tunji', 20, 'Female', '10/feb/1991')
pupil2 = Student('Tunde','femi', 21, 'Male', '10/feb/1991')

print(pupil.get_name())
print(Student.no_of_student)