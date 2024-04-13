class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"the name of employee {self.id} is {self.name}")


class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python ")


e = Employee("ram", 1)
e.showDetails()

e2 = Programmer("Shyam", 2)
e2.showLanguage()
