# class for receipt

class Receipt:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = 0.0
        for item in self.items:
            total += item.price
        return total
    
    def __str__(self):
        receipt_str = "Receipt:\n"
        for item in self.items:
            receipt_str += f"{item}\n"
        receipt_str += f"Total: ${self.calculate_total():.2f}"
        return receipt_str

if __name__ == "__main__":
    receipt = Receipt()