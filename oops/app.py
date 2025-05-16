# class Student:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
        
#     def show_details(self):
#         print("Name: ",self.name)
#         print("age: ",self.age)
#         print("gender:", self.gender)
        
# student = Student("Ibad",21,"male")
# student.show_details()

from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self,name,age):
        self.name = name
        self.__age = age # private variable
    
    def get_age(self): # getter
        return self.__age
    
    @abstractmethod
    def get_role(self): # Abstract method
        pass

class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade
        
    def get_role(self): # Polymorphism
        return "Student"
    
    def study(self):
        print(f"{self.name} is studying in {self.grade} grade")
    
class Teacher(Person):
    def __init__(self, name, age,subject):
        super().__init__(name, age)
        self.subject = subject
    
    def get_role(self):
        return "Teacher"
    
    def teach(self):
        print(f"{self.name} teach {self.subject}")
        
student = Student("Ibad",21,"BSCS")
teacher = Teacher("Arsalan",25,"Python")

print(f"{student.name} is a {student.get_role()}")
student.study()
print(f"Age: {student.get_age()}")

print(f"{teacher.name} is a {teacher.get_role()}")
student.study()
print(f"Age: {teacher.get_age()}")
