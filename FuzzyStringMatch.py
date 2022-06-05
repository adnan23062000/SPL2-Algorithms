with open("country.txt", "r") as f:
    words = f.read().split("\n")

print(len(words))

#pip install fuzzywuzzy

from fuzzywuzzy import process

def get_matches(query, choices, limit=3):
    result = process.extract(query, choices, limit=limit)
    return result


list = []
list = get_matches("undr", words)
print(list)

