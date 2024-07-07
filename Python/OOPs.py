class Student: # Class names prerabbly written in Pascalcase
    hasExams = True
    hasStudied = True
    willPass = hasExams & hasStudied

alex = Student()
print(alex.willPass) # True

class Human:
    def __init__(self, name, iq): # Constructor function for dynamic instances
        self.name = name
        self.iq = iq

person = Human("Pierre", "97")
print(person.name)
print(person.iq)

me = Human("Meet", "3423432865482365082365083260523532523085863208")
print(me.name)
print(me.iq)