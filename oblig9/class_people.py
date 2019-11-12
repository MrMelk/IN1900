class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def name_change(self, newname):
        self.name = newname
    
    def age_change(self, newage):
        self.age = newage
    
    def gender_change(self, newgender):
        self.gender = newgender
    
    def __str__(self):
        return f"Name: {self.name}, age: {self.age}, gender: {self.gender}"

person = Person("John", "32", "male")
print(person)
person.name_change("Ada")
person.age_change("21")
person.gender_change("female")
print(person)

"""
Run example
C:\Users\areto\Documents\Høst2019\IN1900\oblig9>python class_people.py
Name: John, age: 32, gender: male
Name: Ada, age: 21, gender: female
"""