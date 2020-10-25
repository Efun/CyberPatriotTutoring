import random

#how to generate a random int
x = random.randint(0, 10)
print(str(x))

#how to get the length of our list
stringList = ["a", "b", "c", "d", "e"]
print(len(stringList))

#print c from the list

for x in range(3):
    print(stringList[random.randint(0, len(stringList) - 1)]) 
