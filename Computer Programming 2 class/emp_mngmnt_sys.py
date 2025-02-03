class Employee:
    def __init__(self, emp_id, name, deptt, salary):
        self.emp_id = emp_id
        self.name = name
        self.deptt = deptt
        self.__salary = salary
    
    def get_details(self):
        return f'''Name: {self.name}\nEmployee ID: {self.emp_id}\nDepartment: {self.deptt}\nSalary: ₹{self.__salary}\n'''
    
    def update_details(self,  name=None, deptt=None, salary=None):
        if name:
            self.name = name
        if deptt:
            self.deptt = deptt
        if salary:
            self.__salary = salary

    def increment_salary(self, percent):
        self.__salary += (self.__salary * (percent / 100))

class Employee_management:
    def __init__(self):
        print('Management system activated')
        self.reg = {}
    def add_employee(self, emp_id, name, deptt, salary):
        if emp_id in self.reg:
            print('Employee already exists.\nTry Again with different Employee ID...')
            print(self.reg[emp_id].get_details())
        self.reg[emp_id] = Employee(emp_id, name, deptt, salary)


# main code

print("Welcome to GLA University 💀 \n\n")

system = Employee_management()

while True:
    print('''Available Choices:
    1. Add Employee
    2. Display Employee
    3. Update Employee
    4. Increment Salary
    5. Remove Employee
    6. Exit
    ''')
    choice = int(input('Enter the choice [1-6]: '))
    if choice == 1:
        emp_id = int(input('Enter Employee ID: '))
        name = input('Enter Employee Name: ')
        deptt = input('Enter Department: ')
        salary = int(input('Enter Salary: '))
        
        system.add_employee(emp_id, name, deptt, salary)
    elif choice == 2:
        emp_id = int(input('Enter Employee ID: '))
        if emp_id in system.reg:
            print(system.reg[emp_id].get_details())
        else:
            print('Employee not found.')
    elif choice == 3:
        emp_id = int(input('Enter Employee ID: '))
        if emp_id in system.reg:
            name = input('Enter new Employee Name (press enter to skip): ')
            deptt = input('Enter new Department (press enter to skip): ')
            salary = input('Enter new Salary (press enter to skip): ')
            if salary:
                salary = int(salary)
            else:
                salary = None
            system.reg[emp_id].update_details(name or None, deptt or None, salary)
            print('Employee details updated.')
        else:
            print('Employee not found.')
    elif choice == 4:
        emp_id = int(input('Enter Employee ID: '))
        if emp_id in system.reg:
            percent = int(input('Enter percentage to increment salary: '))
            system.reg[emp_id].increment_salary(percent)
            print('Salary incremented.')
        else:
            print('Employee not found.')
    elif choice == 5:
        emp_id = int(input('Enter Employee ID: '))
        if emp_id in system.reg:
            del system.reg[emp_id]
            print('Employee removed.')
        else:
            print('Employee not found.')
    elif choice == 6:
        print('Exiting the system.')
        break
    else:
        print('Invalid choice. Please try again.')


# emp1 = Employee(1, "Idk", "CSE", 50000)
# emp1.update_details(salary=100000)
# emp1.increment_salary(10)
# print(emp1.get_details())