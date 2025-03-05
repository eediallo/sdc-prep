
content = ['Go to the Gym', 'Go shopping', 'Call Michael', 'Attend meeting', 'Do homework', 'Give Demo']
char = 'i'

includesChar = lambda word: char in word

filtered = filter(includesChar, content)

print(list(filtered))