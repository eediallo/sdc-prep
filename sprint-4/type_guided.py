from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_systems: list[str]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: str


def find_possible_laptops(laptops: list[Laptop], person: Person) -> list[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_systems[0]:
            possible_laptops.append(laptop)
    return possible_laptops


people = [
    Person(name="Imran", age=22, preferred_operating_systems=["Ubuntu", "Arch Linux", "macOS"]),
    Person(name="Eliza", age=34, preferred_operating_systems=["Arch Linux", "macOS", "Ubuntu"]),
]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system="Arch Linux"),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="Ubuntu"),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="ubuntu"),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system="macOS"),
]

for person in people:
    possible_laptops = find_possible_laptops(laptops, person)
    for laptop in possible_laptops:
        print(f'{person.name} prefers {laptop.operating_system} most of all, and then {person.preferred_operating_systems[1]}, but will not use {person.preferred_operating_systems[len(person.preferred_operating_systems) -1]}')