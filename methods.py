class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):          #Class methods reference the class not self
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person('nana')
p2 = Person('yaw')
p3 = Person('afriyie')

print(Person.number_of_people_())   # Prints out 3 since three objects have been created from the Person Class

