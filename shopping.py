from abc import ABC, abstractmethod

class Product:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, quantity):
        if self.__stock >= quantity:
            self.__stock -= quantity
            return True
        return False

    def calculate_discount(self):
        return 0


class Electronics(Product):
    def __init__(self, name, price, stock, warranty_period):
        super().__init__(name, price, stock)
        self.__warranty_period = warranty_period

    def get_warranty(self):
        return self.__warranty_period

    def calculate_discount(self):
        return 0.1 * self.get_price()


class Clothing(Product):
    def __init__(self, name, price, stock, size):
        super().__init__(name, price, stock)
        self.__size = size

    def get_size(self):
        return self.__size

    def calculate_discount(self):
        return 0.2 * self.get_price()


class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount:.2f}")
        return True


class PayPalPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount:.2f}")
        return True


class Cart:
    def __init__(self):
        self.__items = []

    def add_product(self, product, quantity):
        if product.update_stock(quantity):
            self.__items.append((product, quantity))
            print(f"Added {quantity} of {product.get_name()} to cart.")
        else:
            print("Not enough stock available.")

    def remove_product(self, product):
        self.__items = [(p, q) for p, q in self.__items if p != product]
        print(f"Removed {product.get_name()} from cart.")

    def calculate_total(self):
        total = sum(product.get_price() * quantity for product, quantity in self.__items)
        return total

    def apply_discount(self):
        total_discount = sum(product.calculate_discount() * quantity for product, quantity in self.__items)
        return total_discount

    def view_cart(self):
        if not self.__items:
            print("Your cart is empty.")
        else:
            print("Cart Contents:")
            for product, quantity in self.__items:
                print(f"- {product.get_name()} x{quantity} (${product.get_price():.2f} each)")

    def clear_cart(self):
        self.__items.clear()
        print("Cart has been cleared.")


class Order:
    def __init__(self, cart, payment_method):
        self.__cart = cart
        self.__payment_method = payment_method

    def checkout(self):
        total = self.__cart.calculate_total()
        discount = self.__cart.apply_discount()
        final_amount = total - discount

        print("\nInvoice:")
        print(f"Total: ${total:.2f}")
        print(f"Discount: ${discount:.2f}")
        print(f"Final Amount: ${final_amount:.2f}")

        if self.__payment_method.process_payment(final_amount):
            print("Payment successful. Order placed!")
            self.__cart.clear_cart()
        else:
            print("Payment failed.")


def display_products(products):
    print("\nAvailable Products:")
    for key, product in products.items():
        print(f"{key}. {product.get_name()} - ${product.get_price():.2f} (Stock: {product.get_stock()})")


def main():
    laptop = Electronics("Laptop", 1000, 10, "1 year")
    shirt = Clothing("Shirt", 50, 20, "M")
    phone = Electronics("Smartphone", 800, 5, "6 months")

    products = {
        1: laptop,
        2: shirt,
        3: phone
    }

    cart = Cart()

    while True:
        print("\n--- Online Shopping Cart System ---")
        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. Remove Product from Cart")
        print("4. View Cart")
        print("5. Clear Cart")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_products(products)

        elif choice == "2":
            display_products(products)
            try:
                product_id = int(input("Enter the product ID to add: "))
                quantity = int(input("Enter the quantity: "))
                if product_id in products:
                    cart.add_product(products[product_id], quantity)
                else:
                    print("Invalid product ID.")
            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "3":
            cart.view_cart()
            try:
                product_id = int(input("Enter the product ID to remove: "))
                if product_id in products:
                    cart.remove_product(products[product_id])
                else:
                    print("Invalid product ID.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            cart.view_cart()

        elif choice == "5":
            cart.clear_cart()

        elif choice == "6":
            print("\nSelect Payment Method:")
            print("1. Credit Card")
            print("2. PayPal")
            payment_choice = input("Enter your choice: ")
            if payment_choice == "1":
                payment_method = CreditCardPayment()
            elif payment_choice == "2":
                payment_method = PayPalPayment()
            else:
                print("Invalid payment method.")
                continue

            order = Order(cart, payment_method)
            order.checkout()

        elif choice == "7":
            print("Thank you for shopping with us!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()