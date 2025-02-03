'''
6. Method to Calculate Area of Shapes
Create a class Rectangle and another class Circle. Both classes should implement a method
to calculate the area of the respective shape.
• Rectangle should have attributes length and width.
• Circle should have an attribute radius.
Instructions: Create a menu-driven program where the user can choose between a rectangle
or a circle and calculate the area for each. The calculation method should be in the class, and
the user should interact with objects.
'''

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * (self.radius ** 2)

def main():
    while True:
        print("1. Calculate area of Rectangle")
        print("2. Calculate area of Circle")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            length = float(input("Enter length of Rectangle: "))
            width = float(input("Enter width of Rectangle: "))
            rectangle = Rectangle(length, width)
            print("Area of Rectangle: ", rectangle.calculate_area())
        elif choice == "2":
            radius = float(input("Enter radius of Circle: "))
            circle = Circle(radius)
            print("Area of Circle: ", circle.calculate_area())
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()