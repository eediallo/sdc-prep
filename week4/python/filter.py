
content = "This is a list of words"
char = 'i'

TODO = []

for word in content.split(' '):
    if char in word:
        TODO.append(word)

filtered = TODO

print(filtered)