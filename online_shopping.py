#The product class represents a product in a store
class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        
        # Initializing the product's name, price, and quantity in stock
        self.product_name = product_name  #the name of the product
        self.price = price  #the price of the product
        self.quantity_in_stock = quantity_in_stock  #the availability stock of the product
        
        #This method displays the product's information
    def display_product_info(self):
        print(f"Product: {self.product_name}, Price: {self.price}, Stock: {self.quantity_in_stock}")


class ShoppingCart:
    total_carts = 0  

    def __init__(self):
        self.items = []  
        ShoppingCart.total_carts += 1

        #Method to add a product to the cart
    def add_to_cart(self, product, quantity):
        if product.quantity_in_stock >= quantity:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity
        else:
            print(f"Not enough stock for {product.product_name}")

        #Method to remove a product to the cart
    def remove_from_cart(self, product):
        self.items = [(p, q) for p, q in self.items if p != product]

    def display_cart(self):
        for item, quantity in self.items:
            print(f"{item.product_name}: {quantity} units")

    def calculate_total(self):
        total = sum(item.price * quantity for item, quantity in self.items)
        return total

# Creating instances of Product with name, price, and stock quantity
product1 = Product("Laptop", 1000, 10)
product2 = Product("Phone", 500, 20)
product3 = Product("Headphones", 100, 50)

# Creating two shopping cart instances
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Adding products to the first cart
cart1.add_to_cart(product1, 2)
cart1.add_to_cart(product3, 5)
cart1.display_cart()
print(f"Total: {cart1.calculate_total()}")

# Adding products to the second cart
cart2.add_to_cart(product2, 3)
cart2.add_to_cart(product3, 10)
cart2.display_cart()
print(f"Total: {cart2.calculate_total()}")