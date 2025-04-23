from dataclasses import dataclass
from datetime import date, datetime

@dataclass
class Student:
    name: str
    age: date
    sex: str
    country: str
    subjects: list[str]

    def tell_your_name(self) -> str:
        return(f'my name is {self.name}, I am {self.age} years old and I am from {self.country}')
    
    def is_adult(self)->str:
        currentDate = date.today()
        age = currentDate.year - self.age.year
        if age >= 18:
            return f'You are {age} years old, therefore, you are are allowed to drive'
        else: 
            return f'You are {age} years old, therefore, you are are not allowed to drive'





elhadj = Student("Elhadj", datetime(2010, 6, 1), "M", "Guinea", ["Math", "English", "Biology"])
fatim = Student("Elhadj", datetime(1998, 6, 1), "M", "Guinea", ["Math", "English", "Biology"])
print(elhadj.subjects)
is_adult = elhadj.is_adult()
print(is_adult)
print(elhadj == fatim)

