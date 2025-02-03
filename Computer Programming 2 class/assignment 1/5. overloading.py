'''
5. Constructor Overloading with Default Arguments
In Python, constructors can be overloaded by using default arguments.
Write a program where you create a class Employee. The class should have attributes name,
age, and department. Implement two constructors:
• The first constructor that accepts all attributes.
• The second constructor that accepts only name and department, and assigns default
values to age.
Instructions: Demonstrate constructor overloading with default arguments and provide a
sample output showing both constructors in use.
'''

class Employee:
    def __init__(self, name, age=25, department=None):
        self.name = name
        self.age = age
        self.department = department

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")


# Using the first constructor
emp1 = Employee("John Doe", 30, "HR")
emp1.display_details()

# Using the second constructor
emp2 = Employee("Jane Doe", department="Marketing")
emp2.display_details()