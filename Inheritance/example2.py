# Use of super class
class Animal:
    def make_sound(self):
        print("The animal makes Sound")


class Dog(Animal):
    def make_sound_iris(self):
        return super().make_sound()


iris = Dog()
iris.make_sound_iris()
