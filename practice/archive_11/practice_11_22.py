#warmup

#hanna make an empty dict and then insert {'hello', 'world'}
notemptydict = {}
notemptydict["hello"] = "world"

#lina make an empty dict and then insert {'hello', 1}

emptyDict = {}
emptyDict["hello"] = 1

#print out your dicts
print(notemptydict)
print(emptyDict)

#print out the value for the key hello
print(notemptydict["hello"])
print(emptyDict["hello"])

intList = [420, 69, 1337, 0, 1, 42, 7, 13, 3]


#find the max val in this list
# maximum = -1000000

# for x in intList:
#     if x > maximum:
#         maximum = x
# print(maximum)
    
for x in intList:
    emptyDict[str(x)] = x

    #on the first iteration of the loop:
        #x = 420
        #32: emptyDict[str(420) = "420"] = x = 420

    #on the second iteration of the loop:
        #x = 69
        #32: emptyDict[str(69) = "69"] = x = 69

print(emptyDict)
{'hello': 1, '420': 420, '69': 69, '1337': 1337, '0': 0, '1': 1, '42': 42, '7': 7, '13': 13, '3': 3}

#items() - a function that dict can use to convert itself into a list of tuples
#converts into [(key, value), (key, value), (key, value)]

#what would the first 2 tuples emptyDict.items() look like?

convertedList = emptyDict.items()

#how do we determine convertedList's maximum value
maximum = -1000000

for x in convertedList: 
    # on the first iteration of this loop, what is x?
    # x = ('420', 420)
    if x[1] > maximum: 
        #can we compare -1000000 to ('420', 420)?
        #how do we access the second item of a tuple? (it's the same as accessing the second item in a list)
        maximum = x[1]

print(maximum)

#in our game what we have is key value pairs of username and votes
