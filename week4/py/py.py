import operator
players = [
    {
        "name": "Daniel",
        "score": 100
    },
    {
        "name": "Kristina",
        "score": 120
    },
    {
        "name": "Iulia",
        "score": 95
    },
    {
        "name": "Aleks",
        "score": 190
    },
    {
        "name": "Daniel",
        "score": 80
    },
    {
        "name": "Fatima",
        "score": 110
    }
]


print(players[0]["name"], ' ====> First Player')
print(players[-1]["name"], '===> last player')

personWithHighestScore = players[0]
for player in players:
    if player["score"] > personWithHighestScore["score"]:
        personWithHighestScore = player
print(personWithHighestScore["name"], personWithHighestScore["score"])


