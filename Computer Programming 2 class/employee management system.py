class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")

    def increment_salary(self, increment_amount):
        if increment_amount > 0:
            self.__salary += increment_amount
        else:
            print("Invalid increment amount")

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.get_salary()}")


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_name):
        for employee in self.employees:
            if employee.name == employee_name:
                self.employees.remove(employee)
                print(f"Employee {employee_name} removed successfully")
                return
        print(f"Employee {employee_name} not found")

    def display_employees(self):
        for employee in self.employees:
            employee.display_details()
            print("------------------------")

    def increment_employee_salary(self, employee_name, increment_amount):
        for employee in self.employees:
            if employee.name == employee_name:
                employee.increment_salary(increment_amount)
                print(f"Salary of employee {employee_name} incremented successfully")
                return
        print(f"Employee {employee_name} not found")


def main():
    ems = EmployeeManagementSystem()

    while True:
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Display Employees")
        print("4. Increment Employee Salary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            age = int(input("Enter employee age: "))
            salary = float(input("Enter employee salary: "))
            employee = Employee(name, age, salary)
            ems.add_employee(employee)
        elif choice == "2":
            employee_name = input("Enter employee name to remove: ")
            ems.remove_employee(employee_name)
        elif choice == "3":
            ems.display_employees()
        elif choice == "4":
            employee_name = input("Enter employee name to increment salary: ")
            increment_amount = float(input("Enter increment amount: "))
            ems.increment_employee_salary(employee_name, increment_amount)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

main()