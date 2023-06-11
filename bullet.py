import pygame
import tile
import room
class Bullet(object):
    def __init__(self,x,y,radius,color,facing,power):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8
        self.rect = pygame.Rect(x, y, 4,4)
        self.power=power

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
        

    def shoot(bullets,SCREEN_WIDTH,SCREEN_HEIGHT, actualroom: room.Room):

        boxes = actualroom.boxesPower
        bombs = actualroom.boxesHealth

        for bullet in bullets:
            if len(boxes)>0:
                for boxindex in range(len(boxes)):    
                    if bullet.x>(boxes[boxindex].x) and bullet.x<(boxes[boxindex].x+40):
                        if bullet.y>(boxes[boxindex].y) and bullet.y<(boxes[boxindex].y+40):
                            boxes[boxindex].hit(20)
                            bullets.pop(bullets.index(bullet)) 
                            break


            if len(bombs)>0:
                for bombindex in range(len(bombs)):    
                    if bullet.x>(bombs[bombindex].x) and bullet.x<(bombs[bombindex].x+40):
                        if bullet.y>(bombs[bombindex].y) and bullet.y<(bombs[bombindex].y+40):
                            bombs[bombindex].hit(20)
                            bullets.pop(bullets.index(bullet)) 
                            break

            if bullet.facing==0: #w prawo leci pocisk
                if bullet.x < SCREEN_WIDTH and bullet.x > 0:
                    bullet.x += bullet.vel  
                else:
                    bullets.pop(bullets.index(bullet)) 
                    
            if bullet.facing==1: #w lewo leci pocisk
                if bullet.x < SCREEN_WIDTH and bullet.x > 0:
                    bullet.x -= bullet.vel
                else:
                    bullets.pop(bullets.index(bullet)) 

            if bullet.facing==2: #w dol
                if bullet.y < SCREEN_HEIGHT and bullet.y > 0:
                    bullet.y += bullet.vel
                else:
                    bullets.pop(bullets.index(bullet)) 

            if bullet.facing==3: #w gore
                if bullet.y < SCREEN_HEIGHT and bullet.y > 0:
                    bullet.y -= bullet.vel
                else:
                    bullets.pop(bullets.index(bullet))   
