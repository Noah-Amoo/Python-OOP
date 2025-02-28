class Dog:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    

d1 = Dog('Frank')
d2 = Dog('Mercy')

print(d1.get_name())
print(d2.get_name())