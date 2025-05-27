class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: {self.name}, {self.age} years old"

class Student(Person):
    def __str__(self):
        return f"Student: {self.name}, {self.age}, studying Computer Science"

# Usage
person = Person("Mus", 30)
student = Student("Mark", 20)

print(person)   # Output: Person: Mus, 30 years old
print(student)  # Output: Student: Mark, 20, studying Computer Science