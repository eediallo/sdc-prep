from dataclasses import dataclass
from enum import Enum

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch linux"
    UBUNTU = "Ubuntu"

@dataclass
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem

@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]

name = input('Enter your name: ')
age = int(input('Enter your age: '))
preferred_operating_system = input('Enter your preferred operating system (macOS, Arch linux, Ubuntu): ')

# Convert the input to the corresponding OperatingSystem Enum
try:
    preferred_os_enum = OperatingSystem(preferred_operating_system)
except ValueError:
    print("Invalid operating system entered.")
    exit()

person = Person(name=name, age=age, preferred_operating_system=preferred_os_enum)
print(person)

matches = [laptop for laptop in laptops if person.preferred_operating_system == laptop.operating_system]

if matches:
    print(f"Great choice {person.name}! We have {len(matches)} match(es):")
    for laptop in matches:
        print(f" - {laptop.manufacturer} {laptop.model} with {laptop.operating_system.value}.")
    print('You can have a laptop with this operating system')
else:
    print("Sorry! You could not find the operating system you are looking for. Try again later.")