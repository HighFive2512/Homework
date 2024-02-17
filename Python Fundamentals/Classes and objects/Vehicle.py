class Vehicle:
    def __init__(self,type:str,model:str,price:float):
        self.owner = None
        self.type = type
        self.model = model
        self.price = price

    def buy(self,money:int,owner:str):
        if money >= self.price and self.owner == None:
            change = "{:.2f}".format(money - self.price)
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {change}"
        elif money >= self.price and self.owner != None:
            return "Car already sold"
        else:
            return "Sorry, not enough money"

    def sell(self):
        if self.owner != None:
            self.owner = None
        else:
            return "Vehicle has no owner"
    def __repr__(self):
        if self.owner != None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"
vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)