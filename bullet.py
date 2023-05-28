import pygame
import tile
class Bullet(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 1
        self.rect = pygame.Rect(x, y, 4,4)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
        

    def shoot(screen,bullets,SCREEN_WIDTH,box):
        
        for bullet in bullets:

            if bullet.x<(tile.TileMap.box[0][0]) and bullet.x>(tile.TileMap.box[0][0]+32):
                print("Jestem w x")
                if bullet.y<(tile.TileMap.box[0][0]) and bullet.y>(tile.TileMap.box[0][0]+32):
                    print("jestem  w y")
                    box.hit()
                    bullets.pop(bullets.index(bullet)) 

            if bullet.facing==0:
                if bullet.x < SCREEN_WIDTH and bullet.x > 0:
                    bullet.x += bullet.vel  
                    #bullet.draw(screen)
                else:
                    bullets.pop(bullets.index(bullet)) 
                    
            if bullet.facing==1:
                if bullet.x < SCREEN_WIDTH and bullet.x > 0:
                    bullet.x -= bullet.vel
                    #bullet.draw(screen)
                else:
                    bullets.pop(bullets.index(bullet)) 

