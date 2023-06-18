from box_bomb import Box
import pygame
from room import *
from enemies import *
from tile import *


            

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

    @staticmethod
    def shoot_box_bomb(bullet, elements, heroBulletPower):
        for index in range(len(elements)): 
            if bullet.x>=(elements[index].x-10) and bullet.x<=(elements[index].x+50):
                if bullet.y>=(elements[index].y - 10) and bullet.y<=(elements[index].y+50):
                    elements[index].hit(heroBulletPower)
                    break

    def shoot(bullets, SCREEN_WIDTH, SCREEN_HEIGHT, cur_room, hero_bullet_power, if_enemy, character):

        boxes = cur_room.boxesPower
        bombs = cur_room.boxesHealth

        if if_enemy==False:
            for bullet in bullets:
                if bullet.facing==0:
                    dx = bullet.vel
                    dy=0
                elif bullet.facing==1:
                    dx = -bullet.vel
                    dy = 0
                elif bullet.facing==2:
                    dx=0
                    dy = bullet.vel
                else:
                    dx=0
                    dy = -bullet.vel
                if len(cur_room.enemies.enemy_list)>0:
                    future_rect = pygame.Rect(bullet.x+dx, bullet.y+dy, 4, 4)
                    for enemy in range(len(cur_room.enemies.enemy_list)):
                        if future_rect.colliderect(cur_room.enemies.enemy_recs[enemy]):
                            cur_room.enemies.hit(enemy, hero_bullet_power)
                            bullets.pop(bullets.index(bullet))
                            break
        else:
            for bullet in bullets:
                if bullet.facing==1:
                    dx = 1
                    dy = 0
                elif bullet.facing==6:
                    dx = -1
                    dy = 0
                elif bullet.facing==4:
                    dx = 0
                    dy = 1
                elif bullet.facing==2:
                    dx = 0
                    dy = -1
                elif bullet.facing==3:
                    dx = 1
                    dy = -1
                elif bullet.facing==5:
                    dx = 1
                    dy = 1
                elif bullet.facing==10:
                    dx = -1
                    dy = 1
                elif bullet.facing==8:
                    dx = -1
                    dy = -1

                future_rect = pygame.Rect(bullet.x+dx, bullet.y+dy, 4, 4)
                if future_rect.colliderect(character.rect):
                    character.hit(bullet.power)
                    bullets.pop(bullets.index(bullet))
                    break


        for bullet in bullets:
            Box.message = ""
            if if_enemy==False:
                if bullet.facing==0: #w prawo leci pocisk
                    if bullet.x < SCREEN_WIDTH and bullet.x > 0:
                        future_rect = pygame.Rect(bullet.x+bullet.vel, bullet.y, 4, 4)
                        if not future_rect.collidelistall(tile.TileMap.collision_map):
                            bullet.x += bullet.vel
                        else:
                            if if_enemy==False:
                                if future_rect.collidelistall(tile.TileMap.box_bullet):
                                    Bullet.shoot_box_bomb(bullet, boxes, 20)
                                if future_rect.collidelistall(tile.TileMap.box_health):
                                    Bullet.shoot_box_bomb(bullet, bombs, 20)
                            bullets.pop(bullets.index(bullet))
                    else:
                        # print("hello")
                        bullets.pop(bullets.index(bullet)) 
                    
                if bullet.facing==1: #w lewo leci pocisk
                    if bullet.x < SCREEN_WIDTH and bullet.x > 0:
                        future_rect = pygame.Rect(bullet.x-bullet.vel, bullet.y, 4, 4)
                        if not future_rect.collidelistall(tile.TileMap.collision_map):
                            bullet.x -= bullet.vel
                        else:
                            if if_enemy==False:
                                if future_rect.collidelistall(tile.TileMap.box_bullet):
                                    Bullet.shoot_box_bomb(bullet, boxes, 20)
                                if future_rect.collidelistall(tile.TileMap.box_health):
                                    Bullet.shoot_box_bomb(bullet, bombs, 20)
                            bullets.pop(bullets.index(bullet))
                    else:
                        bullets.pop(bullets.index(bullet)) 

                if bullet.facing==2: #w dol
                    if bullet.y < SCREEN_HEIGHT and bullet.y > 0:
                        future_rect = pygame.Rect(bullet.x, bullet.y+bullet.vel, 4, 4)
                        if not future_rect.collidelistall(tile.TileMap.collision_map):
                            bullet.y += bullet.vel
                        else:
                            if if_enemy==False:
                                if future_rect.collidelistall(tile.TileMap.box_bullet):
                                    Bullet.shoot_box_bomb(bullet, boxes, 20)
                                if future_rect.collidelistall(tile.TileMap.box_health):
                                    Bullet.shoot_box_bomb(bullet, bombs, 20)
                            bullets.pop(bullets.index(bullet))
                    else:
                        bullets.pop(bullets.index(bullet)) 

                if bullet.facing==3: #w gore
                    if bullet.y < SCREEN_HEIGHT and bullet.y > 0:
                        future_rect = pygame.Rect(bullet.x, bullet.y-bullet.vel, 4, 4)
                        if not future_rect.collidelistall(tile.TileMap.collision_map):
                            bullet.y -= bullet.vel
                        else:
                            if if_enemy==False:
                                if future_rect.collidelistall(tile.TileMap.box_bullet):
                                    Bullet.shoot_box_bomb(bullet, boxes, 20)
                                if future_rect.collidelistall(tile.TileMap.box_health):
                                    Bullet.shoot_box_bomb(bullet, bombs, 20)
                            bullets.pop(bullets.index(bullet))
                    else:
                        bullets.pop(bullets.index(bullet))

            else:
                if bullet.facing==1: #w prawo leci pocisk
                    if bullet.x < SCREEN_WIDTH and bullet.x > 0:
                        future_rect = pygame.Rect(bullet.x+1, bullet.y, 4, 4)
                        if not future_rect.collidelistall(tile.TileMap.collision_map):
                            bullet.x += 1
                        else:
                            bullets.pop(bullets.index(bullet))
                    else:
                        bullets.pop(bullets.index(bullet)) 
                    
                if bullet.facing==6: #w lewo leci pocisk
                    if bullet.x < SCREEN_WIDTH and bullet.x > 0:
                        future_rect = pygame.Rect(bullet.x-1, bullet.y, 4, 4)
                        if not future_rect.collidelistall(tile.TileMap.collision_map):
                            bullet.x -= 1
                        else:
                            bullets.pop(bullets.index(bullet))
                    else:
                        bullets.pop(bullets.index(bullet)) 

                if bullet.facing==4: #w dol
                    if bullet.y < SCREEN_HEIGHT and bullet.y > 0:
                        future_rect = pygame.Rect(bullet.x, bullet.y + 1, 4, 4)
                        if not future_rect.collidelistall(tile.TileMap.collision_map):
                            bullet.y += 1
                        else:
                            bullets.pop(bullets.index(bullet))
                    else:
                        bullets.pop(bullets.index(bullet)) 

                if bullet.facing==2: #w gore
                    if bullet.y < SCREEN_HEIGHT and bullet.y > 0:
                        future_rect = pygame.Rect(bullet.x, bullet.y-1, 4, 4)
                        if not future_rect.collidelistall(tile.TileMap.collision_map):
                            bullet.y -= 1
                        else:
                            bullets.pop(bullets.index(bullet))
                    else:
                        bullets.pop(bullets.index(bullet))

                if bullet.facing==3: #w gore-prawo
                    if bullet.y < SCREEN_HEIGHT and bullet.y > 0:
                        future_rect = pygame.Rect(bullet.x+1, bullet.y-1, 4, 4)
                        if not future_rect.collidelistall(tile.TileMap.collision_map):
                            bullet.y -= 1
                            bullet.x += 1
                        else:
                            bullets.pop(bullets.index(bullet))
                    else:
                        bullets.pop(bullets.index(bullet))

                if bullet.facing==8: #w gore-lewo
                    if bullet.y < SCREEN_HEIGHT and bullet.y > 0:
                        future_rect = pygame.Rect(bullet.x-1, bullet.y-1, 4, 4)
                        if not future_rect.collidelistall(tile.TileMap.collision_map):
                            bullet.y -= 1
                            bullet.x -= 1
                        else:
                            bullets.pop(bullets.index(bullet))
                    else:
                        bullets.pop(bullets.index(bullet))

                if bullet.facing==10: #w dol-lewo
                    if bullet.y < SCREEN_HEIGHT and bullet.y > 0:
                        future_rect = pygame.Rect(bullet.x-1, bullet.y+1, 4, 4)
                        if not future_rect.collidelistall(tile.TileMap.collision_map):
                            bullet.y += 1
                            bullet.x -= 1
                        else:
                            bullets.pop(bullets.index(bullet))
                    else:
                        bullets.pop(bullets.index(bullet))

                if bullet.facing==5: #w dol-prawo
                    if bullet.y < SCREEN_HEIGHT and bullet.y > 0:
                        future_rect = pygame.Rect(bullet.x+1, bullet.y+1, 4, 4)
                        if not future_rect.collidelistall(tile.TileMap.collision_map):
                            bullet.y += 1
                            bullet.x += 1
                        else:
                            bullets.pop(bullets.index(bullet))
                    else:
                        bullets.pop(bullets.index(bullet))