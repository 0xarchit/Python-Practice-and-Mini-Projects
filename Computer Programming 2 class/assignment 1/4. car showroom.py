'''
4. Class with Constructor: Car Showroom
You are tasked to model a Car Showroom system.
Create a Car class with the following attributes:
• model, brand, price
Implement the constructor to initialize these attributes and a method display_info to
print car details.
Instructions: Write the program to allow multiple cars to be added and display the details.
Each car should be represented as an object.
'''

class Car:
    def __init__(self, model, brand, price):
        self.model = model
        self.brand = brand
        self.price = price

    def display_info(self):
        print(f"Model: {self.model}")
        print(f"Brand: {self.brand}")
        print(f"Price: {self.price}")

def main():
    cars = []
    while True:
        print("\n1. Add Car")
        print("2. Display Cars")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            model = input("Enter car model: ")
            brand = input("Enter car brand: ")
            price = float(input("Enter car price: "))
            car = Car(model, brand, price)
            cars.append(car)
        elif choice == "2":
            for i, car in enumerate(cars, start=1):
                print(f"\nCar {i} Details:")
                car.display_info()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()