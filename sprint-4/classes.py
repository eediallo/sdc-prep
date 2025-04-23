from datetime import date

class Person:
    def __init__(self, name: str, dob: date, preferred_operating_system: str, address: str, nationality: str):
        self.name = name
        self.dob = dob
        self.preferred_operating_system = preferred_operating_system
        self.address = address
        self.nationality = nationality

    def is_adult(self) -> bool:
        today = date.today()
        print(today, '===>')
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age >= 18



imran = Person("Imran", date(2010, 1, 6), "Ubuntu", "Stratford Loadge, UB9 5AX", "Guinea")
# elhadj = Person("Elhadj", 27, "Linux")
# Mariam = Person("Imran", 21, "Windows")

# print(imran.name)
# print(imran.address)

# eliza = Person("Eliza", 34, "Arch Linux", "Dedford Bridge, Lewisham", "British")
# print(eliza.name)
# print(eliza.address)


# def is_adult(person: Person) -> bool:
#     return person.age >= 18

# def is_british(person: Person) -> bool:
#     return person.nationality == "British"


print(imran.is_adult())