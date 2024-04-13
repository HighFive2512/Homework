class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, inc_quantity):
        self.inc_quantity = inc_quantity
        if self.quantity + self.inc_quantity <= self.size:
            self.quantity += self.inc_quantity

    def status(self):
        return self.size - self.quantity
