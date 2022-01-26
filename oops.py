class Student:
    def __init__(self, name, age, grade): #self point to instance of class
        self.name = name 
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, course_name, max_student):
        self.course = course_name
        self.max = max_student
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max:
            self.students.append(student)
            return True
        return False

    def grade_average(self):
        val = 0 
        for student in self.students:
            val += student.get_grade()
        avg = val / len(self.students)
        return avg
    
s1 = Student('Rohan', 19, 85)
s2 = Student('Rohit', 19, 96)
s3 = Student('Dwayne', 19, 65)
course = Course('Python', 2)
course.add_student(s1)
course.add_student(s2)
# print(course.add_student(s3))
# print(course.grade_average())

#INHERITENCE
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def disp(self):
        return f'Hi, iam {self.name}, and iam {self.age} years old'

    def say(self):
        return 'Dont know what to say'
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def say(self):
        return 'meow'

    def disp(self):
        return f'My color is {self.color}'

class Dog(Animal):
    def say(self):
        return 'Bark'

class Fish(Animal):
    pass

# a = Animal('Bill',7)
# print(a.disp())
# c = Cat('Rose', 5)
# print(c.disp())
# print(c.say())
# print(Fish('Bubble', 10).say())
c = Cat('Rose', 5, 'brown')
# print(c.disp())

#attributes in class
class Person:
    num_persons = 0
    def __init__(self, name):
        self.name = name
        Person.num_persons += 1
# print(Person.num_persons)
p1 = Person('Rohit')
# Person.num_persons = 35
# p1.num_persons = 45
# print(p1.num_persons)
p2 = Person('Garry')
# print(p2.num_persons)

#class method
class Person:
    num_person = 0 #class attribute
    def __init__(self, name): #instance of person class
        self.name = name
        Person.add_num()

    @classmethod
    def num_pers(cls): #pointing person class attribute, but not instance of class person
        return cls.num_person
    
    @classmethod 
    def add_num(cls): #class method point class attribute, but not instance 
        cls.num_person += 1

p1 = Person('Karl')
p2 = Person('ROSY')
# print(Person.num_pers())

# static method --> not changing
class Math:
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def mult2(x):
        return x * 2

    @staticmethod
    def divide5(x):
        return x / 5

    @staticmethod
    def pr(x):
        x = str(x).lower()
        return 'hello ' + x

print(Math.add5(10))
print(Math.add10(10))
print(Math.mult2(10))
print(Math.divide5(10))
print(Math.pr(10))