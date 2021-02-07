import random
from bullet import Bullet

# :) 
class Gun:
    #properties 
    bullets = []
    capacity = 5

    #actions
    #polymorphism

    #default constructor
    def __init__(self):
        #we create capacity# of bullets, randomly select 1 and make it not a blank
        #for x in range(...)
        self.reload()


    #parametrized constructor
    # def __init__(self, bullets, capacity): 
    #     self.bullets = bullets 
    #     self.capacity = capacity

    def fire(self, person):
        randomBullet = random.choice(self.bullets)

        randomBullet.kill(person)

    def reload(self):
        self.bullets.clear()

        for x in range(self.capacity):
            newBullet = Bullet() 
            self.bullets.append(newBullet)

        random.choice(self.bullets).blank = False

        for x in self.bullets:
            print(x.blank)
