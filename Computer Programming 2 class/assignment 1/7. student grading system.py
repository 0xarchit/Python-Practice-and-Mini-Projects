'''
7. Real-Life Scenario: Student Grading System
Create a Student Grading System that stores student details like name, roll number, and
marks in three subjects. Create a class Student with methods to calculate the grade based on
marks. The grading system will assign:
• A for marks >= 80
• B for marks >= 60
• C for marks >= 40
• F for marks < 40
Instructions: Implement the program with a class Student and display the grade based on
student marks. Provide a method to calculate and display the grade.
'''

class Student:
    def __init__(self, name, roll_num, marks):
        self.name = name
        self.roll_num = roll_num
        self.marks = marks

    def calc_grade(self):
        average_marks = sum(self.marks) / len(self.marks)
        if average_marks >= 80:
            return 'A'
        elif average_marks >= 60:
            return 'B'
        elif average_marks >= 40:
            return 'C'
        else:
            return 'F'

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_num}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calc_grade()}")

# Example usage:
student1 = Student("John Doe", 1, [90, 85, 95])
student1.display_details()