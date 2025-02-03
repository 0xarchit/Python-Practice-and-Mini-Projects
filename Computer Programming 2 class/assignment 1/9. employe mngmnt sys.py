'''
9. Class with Methods: Employee Management System
Scenario:
Create an Employee Management System where an employee has attributes such as name,
designation, and salary.
Instructions:
• Define a class Employee with the following attributes:
o name (The name of the employee)
o designation (The job title/designation of the employee)
o salary (The salary of the employee)
• Implement methods to:
o display_info() – Display the employee's details.
o update_salary() – Update the employee's salary.
o promote() – Change the employee's designation.
'''

class Employee:
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Designation: {self.designation}")
        print(f"Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary

    def promote(self, new_designation):
        self.designation = new_designation