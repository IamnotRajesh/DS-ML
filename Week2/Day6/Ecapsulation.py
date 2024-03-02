#Private Access
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age


class Ram(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def display(self):
        print(f"The person name is {self._name} is {self._age} years old.")

if__name__ = "__main__"
person_test = Ram(name = "Rajesh", age = 20)
person_test.display()