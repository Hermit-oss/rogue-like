import pygame

class Box(object):
    def __init__(self,health_points):
        self.health_point=health_points


    def hit(self):
        self.health_point-=2
        if self.health_point==0:
            print("Im dead")
        print("hit")

