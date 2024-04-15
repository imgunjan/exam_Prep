class Animal:
    def make_sound(self):
        print("The animal makes Sound")


class Dog(Animal):
    def make_sound(self):
        print("The dog barks")


tiger = Animal()
tiger.make_sound()
iris = Dog()
iris.make_sound()
