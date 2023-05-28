import pygame
import tile
class Bullet(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 0.5
        self.rect = pygame.Rect(x, y, 4,4)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
        

    def shoot(screen,bullets,SCREEN_WIDTH,boxes, bombs):
        
        for bullet in bullets:
            if len(boxes)>0:
                for boxindex in range(len(boxes)):    
                    if bullet.x>(boxes[boxindex].x) and bullet.x<(boxes[boxindex].x+32):
                        if bullet.y>(boxes[boxindex].y) and bullet.y<(boxes[boxindex].y+32):
                            boxes[boxindex].hit()
                            bullets.pop(bullets.index(bullet)) 

            if len(bombs)>0:
                for bombindex in range(len(bombs)):    
                    if bullet.x>(bombs[bombindex].x) and bullet.x<(bombs[bombindex].x+32):
                        if bullet.y>(bombs[bombindex].y) and bullet.y<(bombs[bombindex].y+32):
                            bombs[bombindex].hit()
                            bullets.pop(bullets.index(bullet)) 

            if bullet.facing==0:
                if bullet.x < SCREEN_WIDTH and bullet.x > 0:
                    bullet.x += bullet.vel  
                else:
                    bullets.pop(bullets.index(bullet)) 
                    
            if bullet.facing==1:
                if bullet.x < SCREEN_WIDTH and bullet.x > 0:
                    bullet.x -= bullet.vel
                else:
                    bullets.pop(bullets.index(bullet)) 

