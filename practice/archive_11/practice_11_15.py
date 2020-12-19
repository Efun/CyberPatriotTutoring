#lina make a dict with keys: a, b where the value of  key a is going to be hello and the value of key b is going to be world
# helloWorld = { 
#     "a": "hello",
#     "b": "world"
# }

# #hanna make a dict with keys: a, b where the value of 
# # key a is going to be 1 and the value of keys b is going to be 0 (1 and 0 should be numbers)
# something = {
#     "a": 1,
#     "b": 0
# }

# #lina you get print out key value a of hanna's dict

# print(something["a"])

# #hanna you get to print out key value b of lina's dict
# print(helloWorld["b"])

# #lina add key c and value 1 to your dict print it out right after
# helloWorld["c"] = 1
# print(helloWorld["c"])

# #hanna add key c and value "potato" to your dict print it out right after
# something["c"] = "potato"
# print(something["c"])

# #lina change something's a value to 100
# something["a"] = 100

# #hanna increment something's b value by 12
# something["b"] += 12

#find the max

#we set some initial value that's really small
#every time we find a value greater than it, we update that really small value to be that greater value instead

intList = [420, 69, 1337, 0, 1, 42, 7, 13, 3]

#set some initial value with -1000000
maximum = -10000000 

#loop through the list and every time we find something greater than the maximum value, that becomes the new maximum value
for x in intList: 
    if x > maximum:
        maximum = x

print(maximum)
