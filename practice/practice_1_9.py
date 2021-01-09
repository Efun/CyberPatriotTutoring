condition1 = False
condition2 = True

#while true loop, that breaks when condition 2 becomes false
#

x = 0

# while x < 10:
#     x += 1
#     print(x) #this printed the number 9
     
#what is x at the beginning of the loop when we print out 9

#rewrite the loop above into a while true

y = 0

#we want the loop to stop if condition 1 is false
#= means assign
#== means compare, returns a boolean
#stop the loop if condition2 is true
#we're asking if True == True (will always be True) versus if True

#let's stop the loop when condition1 is False and conditon2 is True
#you cannot use == operator
#all on one line

while True: 
    if y < 10:
        y += 1 
        print(y) 
    # if condition2: 
    #     break 

    if condition2 and not condition1: 
        break 