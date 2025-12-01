# Single Responsibility Principle applied to a Shopping Cart
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(self, item: Item):
        self.items.remove(item)

    def calculate_total(self) -> float:
        return sum(item.price for item in self.items)

# Open/Closed Principle applied to Payment Processing
class DiscountStrategy:
    def apply_discount(self, total: float) -> float:
        raise NotImplementedError 

class Nodiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        return total
    
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply_discount(self, total: float) -> float:
        return total * ( 1 - self.percentage / 100 )

class FixedDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        self.amount = amount

    def apply_discount(self, total: float) -> float:
        return max(0, total - self.amount)

# Liskov Substitution Principle applied to Payment Methods
class InvoicePrinter:
    def print_invoice(self, cart: ShoppingCart, discount: DiscountStrategy):
        total = cart.calculate_total()
        discounted_total = discount.apply_discount(total)
        print("Invoice:")
        for item in cart.items:
            print(f"- {item.name}: ${item.price:.2f}")
        print(f"Total: ${total:.2f}")
        print(f"Discounted Total: ${discounted_total:.2f}")

# example 
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item(Item("Book", 12.99))
    cart.add_item(Item("Pen", 1.49))
    cart.add_item(Item("Notebook", 4.99))

    discount = PercentageDiscount(10)
    printer = InvoicePrinter()
    printer.print_invoice(cart, discount)