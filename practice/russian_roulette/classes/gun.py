# :) 
class gun:
    #properties 
    bullets = []
    capacity = 5

    #actions
    #polymorphism

    #default constructor
    def __init__(self):
        pass

    #parametrized constructor
    def __init__(self, bullets, capacity): 
        self.bullets = bullets 
        self.capacity = capacity

    def fire(self):
        pass

    def reload(self):
        pass
