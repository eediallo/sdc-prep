from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name:str
    age: int
    children: list['Person']


abdoul = Person('Abdoul', 27, children=[])
halima = Person('Halimatou', 21, children=[])
moumini = Person('Moumini',29, children=[])
aissatou = Person('Aissatou', 49, children=[abdoul, halima, moumini])

def print_family_tree(person: Person)->None:
    print(f'Hey there {person.name}! Here is your family tree')
    for child in person.children:
        print(f'{child.name} - {child.age}')



# print_family_tree(abdoul)
print_family_tree(aissatou)