class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def findage(self):
        return self.age


per = Person("Keshav", 32)
print(per.findage())
print(type(per))