# menu driven calculator using class and object

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, *args):
        result = sum(args)
        self.history.append(f"Added {', '.join(map(str, args))} = {result}")
        return result

    def subtract(self, *args):
        result = args[0]
        for num in args[1:]:
            result -= num
        self.history.append(f"Subtracted {', '.join(map(str, args))} = {result}")
        return result

    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        self.history.append(f"Multiplied {', '.join(map(str, args))} = {result}")
        return result

    def divide(self, *args):
        result = args[0]
        for num in args[1:]:
            if num != 0:
                result /= num
            else:
                raise ValueError("Cannot divide by zero")
        self.history.append(f"Divided {', '.join(map(str, args))} = {result}")
        return result

    def print_history(self):
        for entry in self.history:
            print(entry)


def main():
    calculator = Calculator()
    while True:
        print("\nMenu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Print History")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice in ['1', '2', '3', '4']:
            nums = input("Enter numbers separated by space: ")
            nums = list(map(float, nums.split()))
            if choice == '1':
                print(calculator.add(*nums))
            elif choice == '2':
                print(calculator.subtract(*nums))
            elif choice == '3':
                print(calculator.multiply(*nums))
            elif choice == '4':
                try:
                    print(calculator.divide(*nums))
                except ValueError as e:
                    print(e)
        elif choice == '5':
            calculator.print_history()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()