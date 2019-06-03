"""
A map : takes a list and with a function change the list , and then spits out new list after the changes
a map function has a function contains :
map(funciton,data)
"""

from random import shuffle

def anaGram(word):
    anagramooos = list(word)
    shuffle(anagramooos)
    return "".join(anagramooos)


data = ["potatoes","tomatoes","broccoli"]

anagram = []

# using a for loop
for i in data:
    anagram.append(anaGram(i))
print (anagram)


print("------------")
# by using a map function

print(list(map(anaGram,data)))


print("---------")
# list comprehension way

print([anaGram(i) for i in data  ])