letterList = ["a", "b", "c", "d"]

#how do we print instead of 
# a
# b
# c
# d

# 1.) a
# 2.) b
# 3.) c
# 4.) d

#how do we just print out 1 2 3 4 by using this loop
integerVariable = 1

for x in letterList:
    print(str(integerVariable) + ". " + x)
    integerVariable += 1