import argparse

parser = argparse.ArgumentParser(
    prog="count-containing-words",
    description="Counts words in a file that contain a particular character",
)

parser.add_argument("-c", "--char", help="The character to search for", default="e")
parser.add_argument("path", help="The file to search")

args = parser.parse_args()

with open(args.path, 'r') as file:
    content = file.read().split(' ')

char = args.char
numberOfChars = 0

for word in content:
    if char in word:
        numberOfChars+=1

print(numberOfChars)