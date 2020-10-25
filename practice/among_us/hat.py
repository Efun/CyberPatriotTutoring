class hat:
    # properties
    color = ""
    style = ""

    # actions
    def __init__(self, color, style):
        self.color = str(color)
        self.style = str(style)

    def getcolor(self):
        return self.color

    def setcolor(self, color):
        if (type(color) is str):
            self.color = color
        else:
            print("That's not a color")

    def getstyle(self):
        return self.style

    def setstyle(self, style):
        if (type(style) is str):
            self.style = style
        else:
            print("That's not a style?")


# class hat:
#     #properties
#     color = ""
#     style = ""

#     #actions
#     def __init__(self, color, style):
#         self.color = color
#         self.style = style
