class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    

d1 = Dog('Frank', 3)
d2 = Dog('Mercy', 7)

print(d1.get_name(), d1.get_age())
print(d2.get_name(), d2.get_age())