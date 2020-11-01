import sys

sys.path.append("..")
from classes.animal import animal

conditionA = True
conditionB = True

#truth table

jackie = animal(1, 3, "green", "girl", "tyrannosaurus rex")

#code a, code b, none, or both?

#branch keywords: if, else, and elif

#nesting
if conditionA:
    if conditionB:
        #code A
        print("a and b")
    #code B
    print("a")

#else

#prints one or the other
if jackie.color == "green":
    print("she's green")
else:
    #code B
    print("she's not green")


#prints both
if jackie.color == "green":
    print("she's green")

print("she's not green")

#elif
if jackie.color == "green":
    print("she's green")
elif jackie.color == "blue":
    print("she's blue")
else:
    print("she's neither blue nor green")