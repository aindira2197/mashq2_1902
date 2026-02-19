class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Dog(Animal):
    def speak(self):
        return "vov vov"


print(Dog("Bobik").speak())



class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


d = Dog("Bobik", "Pitbul")
print(d.name, d.breed)
