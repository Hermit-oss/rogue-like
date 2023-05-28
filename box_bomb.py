import pygame
import random
import tile

def genre_boxes():
    box=[]
    bomb=[]
    for index in range(len(tile.TileMap.box)):
        box.append(Box(tile.TileMap.box[index][0],tile.TileMap.box[index][1],20,0))
    for index in range(len(tile.TileMap.bomb)):
        bomb.append(Box(tile.TileMap.bomb[index][0],tile.TileMap.bomb[index][1],20,1))
        
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

    def hit(self):
        self.health_point-=2
        if self.health_point==0:
            if self.type==0:
                Box.dead_money(self)
            if self.type==1:
                Box.dead_bomb(self)

    def dead_money(self):
        print("Im dead, a ty bedziesz bogaty")
    def dead_bomb(self):
        print("Im dead, i lap bombe")




