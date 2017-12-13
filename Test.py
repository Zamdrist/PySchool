class Person:
    def __init__(self, firstName, middleName, lastName):
        self._firstName = firstName
        self._middleName = middleName
        self._lastName = lastName

person_list = []
person = Person("Steven", "Ross", "Schroeder")
person_list.append(person)
personObj = person_list[0]
print(personObj._firstName)