# Single responsibilities Principle 

# this class is only responsible for baking bread
class BreadBaker:
    def bakeBread(self):
        print(f"Baking high quality bread...") 

# this class is only responsible for manage inventory
class InventoryManager:
    def manageInventory(self):
        print(f"Mananing Inventory...")

# this class is only responsible for supply order
class SupplyOrder:
    def orderSupplies(self):
        print(f"Ordering supplies...")


# this class is only responsible for customer service
class CustomerService:
    def serviceCustomer(self):
        print(f"Serving customer...")

# this class is only responsible for bakery cleaning
class BakeryCleaner:
    def cleanBakary(self):
        print(f"Cleaning the bakary...")


def main():
    baker = BreadBaker()
    inventory = InventoryManager()
    order = SupplyOrder()
    customer = CustomerService()
    cleaning = BakeryCleaner()

    baker.bakeBread()
    inventory.manageInventory()
    order.orderSupplies()
    customer.serviceCustomer()
    cleaning.cleanBakary()


main()