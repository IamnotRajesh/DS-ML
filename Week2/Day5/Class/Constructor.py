class Animals:
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.species = args[1]
        elif len(args) == 3:
            self.name = args[0]
            self.species = args[1]
            self.age = args[2]

    

    def  speak(self):
        print(f"{self.name} is barking")

if __name__ == "__main__":
    animal_01 = Animals("Dog", "Dog Family")
    animal_01.speak()

