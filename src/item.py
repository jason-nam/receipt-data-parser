# class for each items in receipt data

class Item:
    def __init__(self, text, x_coord, y_coord, width, height):
        self.text = text
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.width = width
        self.height = height
        
    #TODO

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"