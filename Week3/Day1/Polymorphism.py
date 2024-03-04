class Animal():
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, speak):
        super().__init__(name)
        self.speak = speak
    
    def bark(self):
        return f"{self.name} says {self.speak}"

if __name__ == "__main__":
    dog1 = Dog("Buddy", "Woof")
    print(dog1.bark())