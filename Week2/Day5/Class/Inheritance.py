class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(self.name)
        print(self.price)

   
    
class Maruti(Car):
    def __init__(self, name, price, color):
        self.color = color
        Car.__init__(self, name, price)
    def display(self):
        super().display()
        print(self.color)

if __name__ == "__main__":
    new = Maruti("Maruti-SSDV", 1120000, "Black")
    new.display()
