
content = "This is a list of words"
char = 'i'

includesChar = lambda word: char in word

filtered = filter(includesChar, content.split(' '))

print(list(filtered))