#type out a dict with 5 elements, we need 2 of the same value and that value must be the maximum
randomDict = {
    "watermelon": 0,
    "lime": 1,
    "apple": 2,
    "orange": 4,
    "banana": 4,
    "pear": 4,
    "dragonfruit": 5,
    "tomato": 5
}

maximum = -1000000
maxFruit = ""
#right here is the first line
for x in randomDict.items():
    if x[1] > maximum:
        maximum = x[1]
        maxFruit = x[0]

#what's the value of maximum here: 4
#what's the value of fruits here: orange

#how do we know whether there are 2 matching maximum values?
for x in randomDict.items():
    if maximum == x[1]: 
        #we want to check that the current x's fruit name is not equal to the max fruit before we print
        if x[0] != maxFruit:
            print("It's a tie")
            break

#print(fruits) 

