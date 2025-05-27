class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_number, course, year, hall):
        super().__init__(name, age)
        self.student_number = student_number
        self.course = course
        self.year = year
        self.hall = hall

    def display_info(self):
        super().display_info()
        print(f"Student Number: {self.student_number}")
        print(f"Course: {self.course}")
        print(f"Year of Study: {self.year}")
        print(f"Hall of Residence: {self.hall}")
        print("-" * 30)

class Lecturer(Person):
    def __init__(self, name, age, courses_taught, department):
        super().__init__(name, age)
        self.courses_taught = courses_taught
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        print("Courses Taught:")
        for course in self.courses_taught:
            print(f"  - {course}")
        print("-" * 30)

class Staff(Person):
    def __init__(self, name, age, staff_id, role):
        super().__init__(name, age)
        self.staff_id = staff_id
        self.role = role

    def display_info(self):
        super().display_info()
        print(f"Staff ID: {self.staff_id}")
        print(f"Role: {self.role}")
        print("-" * 30)

#Instances
student1 = Student("Ntensibe Mark", 20, "S12345", "Computer Science", 2, "University Hall")
lecturer1 = Lecturer("Prof.Agaba Joab", 43, ["Object Oriented Programming", "Technical Analysis and Design"], "Computing")
staff1 = Staff("Kimuli Roderick", 22, "MAKSTF001", "General Duties")

student2 = Student("Mutagubya Aloysious", 20, "23/U/12262/EVE", "Software Engineering", 2, "Living stone hall")
lecturer2 = Lecturer("Dr.Ruth", 45, ["Python Programming", "Machine Learning"], "Computing")
staff2 = Staff("Bbosa Sharif", 23, "MAKSTF002", "IT Support")



# Display information
print("STUDENT INFORMATION:")
student1.display_info()

print("\nLECTURER INFORMATION:")
lecturer1.display_info()

print("\nSTAFF INFORMATION:")
staff1.display_info()

#Display information student 2

print("STUDENT INFORMATION:")
student2.display_info()

print("\nLECTURER INFORMATION:")
lecturer2.display_info()

print("\nSTAFF INFORMATION:")
staff2.display_info()