from hat import hat as hatType


class player:
    #properties
    isImposter = False
    color = ""
    hat = None
    userName = ""

    #actions
    def __init__(self, userName, color):
        self.userName = str(userName)
        self.color = str(color)

    #getters and setters
    def getColor(self):
        return self.color

    def setColor(self, color):
        if (type(color) is str):
            self.color = color
        else:
            print("That's not a color!")

    def getIsImposter(self):
        return self.isImposter

    def setIsImposter(self, isImposter):
        if (type(isImposter) is bool):
            self.isImposter = isImposter
        else:
            print("That's not a boolean!")

    def getHat(self):
        return self.hat

    def setHat(self, hat):
        if (type(hat) is hatType):
            self.hat = hat
        else:
            print("no")
