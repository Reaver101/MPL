class Product: 
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart: 
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))
        print(product.name, "Added to cart.")

    def total_cost(self):
        total = 0

        for product, quantity in self.items:
            total = total + product.price * quantity

        return total

    def display_cart(self): 
        print("\nItems in cart: ")

        for product, quantity in self.items: 
            print(product.name, " ", quantity)

        print("Total Cost =", self.total_cost())

p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 500)
p3 = Product("Keyboard", 500)

cart = ShoppingCart()

cart.add_item(p1, 1)
cart.add_item(p2, 2)
cart.add_item(p3, 3)

cart.display_cart()
