class Person:
    number_of_people = 0 #Class attribute

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1 # Keeps track of objects created from the Person Class

p1 = Person('nana')
p2 = Person('yaw')
p3 = Person('afriyie')

# number_of_people is defined for the entire class. It can be modified using the object or by calling the class itself
# Person.number_of_people = 8
# print(p1.number_of_people)  # This will print out 8

print(Person.number_of_people)