import random
import tile
money_amount=0


def genre_boxes(tileMap):
    boxWithBulletPower=[]
    boxWithHealth=[]
    for index in range(len(tileMap.box_bullet)):
        boxWithBulletPower.append(Box(tileMap.box_bullet[index][0],tileMap.box_bullet[index][1],60,0))
    for index in range(len(tileMap.box_health)):
        boxWithHealth.append(Box(tileMap.box_health[index][0],tileMap.box_health[index][1],60,1))

    return boxWithBulletPower,boxWithHealth

class Box(object):
    
    def __init__(self,x,y,health_points,type):
        self.health_point=health_points
        self.index=0
        self.x=x
        self.y=y
        self.width=40
        self.height=40
        self.type=type #0-money 1- bomb
        

    def hit(self,hero_bullet_power):
        
        self.health_point-=hero_bullet_power
        if self.health_point<=0:
            if self.type==0:
                Box.dead_bullet_power(self)
                print("zgon")
            if self.type==1:
                Box.dead_health_points(self)
                print("zgon")

    def dead_bullet_power(self):
        global money_amount 
        money_amount +=  random.randint(2,5)
        print("Im dead, a ty masz mocniejszy pocisk")
    
    def dead_health_points(self):
        print("Im dead, a ty zdrowszy")




