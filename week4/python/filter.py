
content = "This is a list of words"
char = 'i'

def includesChar(word):
    return char in word

filtered = filter(includesChar, content.split(' '))

print(list(filtered))