class Invoice:
    def __init__(self, item):
        self.item = item

    def generate_invoice(self):
        print("Invoice created")

    def udpate_invoice(self):  
        print("Invoice updated.")


invoiceOne = Invoice("Book")
invoiceOne.generate_invoice()
invoiceOne.udpate_invoice()