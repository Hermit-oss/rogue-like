import random
import tile
import pygame
health=0
power=0

def genre_boxes(tileMap, surface):
    boxWithBulletPower=[]
    boxWithHealth=[]
    for index in range(len(tileMap.box_bullet)):
        boxWithBulletPower.append(Box(tileMap.box_bullet[index][0],tileMap.box_bullet[index][1],60,0,surface))
    for index in range(len(tileMap.box_health)):
        boxWithHealth.append(Box(tileMap.box_health[index][0],tileMap.box_health[index][1],60,1,surface))

    return boxWithBulletPower,boxWithHealth

class Box(object):

    message = ""
    
    def __init__(self,x,y,health_points,type, surface):
        self.health_point=health_points
        self.index=0
        self.x=x
        self.y=y
        self.width=40
        self.height=40
        self.type=type #0-money 1- bomb
        self.destroyed= False
        self.surface = surface

    def hit(self,hero_bullet_power):
        self.health_point-=hero_bullet_power
        if self.health_point<=0 and not self.destroyed:
            self.destroyed= True
            if self.type==0:
                Box.dead_bullet_power(self)
            if self.type==1:
                Box.dead_health_points(self)
        elif self.health_point<=-40 and self.destroyed:
            Box.message = "Już zniszczone"
        else:
            Box.message = ""
        

    @staticmethod
    def show_message(surface):
        surface.blit(pygame.font.SysFont(None, 32).render(Box.message, True, (255,255,255), (0,0,0)), (400,10))


    def dead_bullet_power(self):
        global power
        power=1
        Box.message = "Silniejszy pocisk"

    
    def dead_health_points(self):
        global health
        health +=  random.randint(2,5)
        Box.message = "Wieksze życie"
        
        
        
        




