import random
import tile
money_amount=0


def genre_boxes():
    box=[]
    bomb=[]
    for index in range(len(tile.TileMap.box)):
        box.append(Box(tile.TileMap.box[index][0],tile.TileMap.box[index][1],60,0))
    for index in range(len(tile.TileMap.bomb)):
        bomb.append(Box(tile.TileMap.bomb[index][0],tile.TileMap.bomb[index][1],60,1))
        
    return box,bomb

class Box(object):
    
    def __init__(self,x,y,health_points,type):
        self.health_point=health_points
        self.index=0
        self.x=x
        self.y=y
        self.width=32
        self.height=32
        self.type=type #0-money 1- bomb
        

    def hit(self,hero_bullet_power):
        
        self.health_point-=hero_bullet_power
        if self.health_point==0:
            if self.type==1:
                Box.dead_money(self)
            if self.type==0:
                Box.dead_bomb(self)

    def dead_money(self):
        global money_amount 
        money_amount +=  random.randint(2,5)
        print("Im dead, a ty bedziesz bogaty")
        #money+=random.randint(2,5)
        #print("Jestem taki bogaty!!!",money)

    
    def dead_bomb(self):
        print("Im dead, i lap bombe")




