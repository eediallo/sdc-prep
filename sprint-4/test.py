# from typing import Set, Union

# def  sum_of_numbers(nums: list[int]) -> int:
#     return sum(nums)



# def average(scoredCard: dict[str, int]) -> float:
#     marks = scoredCard.values()
#     return sum(marks)/len(marks)


# def uniques_count(nums: list[int]) -> int:
#     uniques: Set[int] = set()
#     for num in nums:
#         uniques.add(num)
#     return len(uniques)


# # unions
# def print_favorite_color(person: dict[str, str]) -> None:
#     fav_color = person.get('favorite_color')
#     # reveal_type(fav_color)
#     print(fav_color, '==>>>>>>')
#     if fav_color is None:
#         print("You do not have a favorite color")
#     else:
#         print(f'You favorite color is: {fav_color}')

# def print_item(item: Union[str, list[str]]) -> None:
#     # reveal_type(item)
#     if isinstance(item, list):
#         for data in item:
#             # reveal_type(item)
#             print(data)
#     else:
#         # reveal_type(item)
#         print(item)
    
# """
# print(f'sum is equal ===> {sum([5, 5])}')
# print(f'Number of marks ===> {average({"english": 23, "math": 23, "Biology": 55 })}')
# print(f'Uniques Count ===> {uniques_count([5, 5, 6, 7, 6, 5, 6, 7])}') 
# """

# # me = {"name": "ediallo", "favorite_color": "red" }
# # print(print_favorite_color(me))

# # print_item('Hi!')
# # print_item(['This is a test', "of polymorphism"])

# # Any type


# def triple_num(num: int) -> int:
#     reveal_type(num)
#     return num * 3



# print(f'RESULT =>: {triple_num(5)}')


from typing import Union

def open_account(balances: dict[str, int], name: str, amount:int)-> None:
   balances[name] = amount

def sum_balances(accounts:dict[str, int]) -> int:
    total = 0
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total

def format_pence_as_string(total_pence: int)->str:
    if total_pence < 100:
        return f"{total_pence}p"
    pounds = int(total_pence / 100)
    pence = total_pence % 100
    return f"£{pounds}.{pence:02d}"

balances = {
    "Sima": 700,
    "Linn": 545,
    "Georg": 83,
}

open_account(balances, "Tobi", 913)
open_account(balances, "Olya", 713)

total_pence = sum_balances(balances)
total_string = format_pence_as_string(total_pence)

print(f"The bank accounts total {total_string}")

