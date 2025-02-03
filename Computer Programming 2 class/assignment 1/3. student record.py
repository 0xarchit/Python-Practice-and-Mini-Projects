'''
3. Menu-Driven Program: Student Records
Create a menu-driven program to maintain Student Records. Implement the following
features:
• Add student (name, roll number, course)
• View all students
• Search for a student by roll number
• Exit
Use a class Student to hold student information.
Instructions: Implement the program using a class and methods to manage students. Provide
the class diagram or flowchart showing how objects of the class interact.
'''

class Student:
    def __init__(self, name, roll_number, course):
        self.name = name
        self.roll_number = roll_number
        self.course = course

    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, Course: {self.course}"


class StudentRecords:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter student name: ")
        roll_number = input("Enter student roll number: ")
        course = input("Enter student course: ")
        student = Student(name, roll_number, course)
        self.students.append(student)
        print("Student added successfully!")

    def view_all(self):
        if not self.students:
            print("No students in the records.")
        else:
            for student in self.students:
                print(student)

    def search_student(self):
        roll_number = input("Enter roll number to search: ")
        for student in self.students:
            if student.roll_number == roll_number:
                print(student)
                return
        print("Student not found.")

    def exit(self):
        print("Exiting the program. Goodbye!")


def main():
    records = StudentRecords()
    while True:
        print("\nStudent Records Menu:")
        print("1. Add student")
        print("2. View all students")
        print("3. Search for a student")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            records.add_student()
        elif choice == "2":
            records.view_all()
        elif choice == "3":
            records.search_student()
        elif choice == "4":
            records.exit()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()