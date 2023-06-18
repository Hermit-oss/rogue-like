import random
import pygame
import tile
#import character
from bullet import Bullet

ZERO=(155,155,0)
ONE=(0,155,155)
TWO=(155,0,155)
EN_SIZE = 16


class enemy_class():

    def __init__(self, screen):
        self.enemy_list=[]
        self.enemy_X=[]
        self.enemy_Y=[]
#        self.enemies_imgs=[]
        self.enemy_recs=[]
        self.enemy_colors=[]
        self.enemy_change_X=[]
        self.enemy_change_Y=[]
        self.enemy_hp=[]
        self.if_draw=[]
        self.shooter=[]
        self.enemy_bullets=[]
        self.enemy_dmg=[]
        self.enemy_attack_cooldown=[]

        win_x, win_y = screen.get_size()
        amount = random.randint(3, 5)
        for i in range(amount):
            enemy_type = random.randint(0,2)  #losuje rodzaj oponenta
            enemy_X = random.randint(60, win_x-80)
            enemy_Y = random.randint(60,win_y-80)

            self.enemy_list.append(enemy_type)
            self.enemy_X.append(enemy_X)
            self.enemy_Y.append(enemy_Y)
            self.if_draw.append(False)

            if enemy_type==0:                   #op typu 0, nie za szybki idzie w kierunku gracza, troszkę twardszy
#                self.enemies_imgs.append(pygame.image.load("assets/imgs/slow_biegacz.png"))
                self.enemy_recs.append(pygame.Rect(enemy_X, enemy_Y, EN_SIZE, EN_SIZE))
                self.enemy_colors.append(ZERO)
                self.enemy_change_X.append(2)
                self.enemy_change_Y.append(2)
                self.enemy_hp.append(30)
                self.shooter.append(False)
                self.enemy_dmg.append(1)
                self.enemy_attack_cooldown.append(35)

            elif enemy_type==1:                 #op typu 1, bedzie strzelal i ucieka od gracza. nie bardzo twardy
#                self.enemies_imgs.append(pygame.image.load("assets/imgs/strzelacz.png"))
                self.enemy_recs.append(pygame.Rect(enemy_X, enemy_Y, EN_SIZE, EN_SIZE))
                self.enemy_colors.append(ONE)
                self.enemy_change_X.append(-2)
                self.enemy_change_Y.append(-2)
                self.enemy_hp.append(20)
                self.shooter.append(True)
                self.enemy_dmg.append(1)
                self.enemy_attack_cooldown.append(80)


            else:                               #op typu 2, biegnie do gracza, szybko, miękki
#                self.enemies_imgs.append(pygame.image.load("assets/imgs/amognus.png"))
                self.enemy_recs.append(pygame.Rect(enemy_X, enemy_Y, EN_SIZE, EN_SIZE))
                self.enemy_colors.append(TWO)
                self.enemy_change_X.append(3)
                self.enemy_change_Y.append(3)
                self.enemy_hp.append(10)
                self.shooter.append(False)
                self.enemy_dmg.append(1)
                self.enemy_attack_cooldown.append(25)


#            width = self.enemies_imgs[i].get_width()
#            height = self.enemies_imgs[i].get_height()
#            self.enemies_imgs[i]=pygame.transform.scale(self.enemies_imgs[i], (int(0.05*width), int(0.05*height)))


    def display_enemy(self, screen):
        for i in range(len(self.enemy_list)):
            pygame.draw.rect(screen, self.enemy_colors[i], self.enemy_recs[i])

#                screen.blit(self.enemies_imgs[i], (self.enemy_X[i], self.enemy_Y[i]))

    def remove_enemies(self):
        i=0
        length=len(self.enemy_list)
        while i < length:
            if self.if_draw[i]==False:
                self.enemy_list.pop(i)
                self.enemy_X.pop(i)
                self.enemy_Y.pop(i)
                self.enemy_recs.pop(i)
                self.enemy_colors.pop(i)
                self.enemy_change_X.pop(i)
                self.enemy_change_Y.pop(i)
                self.enemy_hp.pop(i)
                self.if_draw.pop(i)
                self.shooter.pop(i)
                self.enemy_dmg.pop(i)
                self.enemy_attack_cooldown.pop(i)
                i-=1
                length-=1
            i+=1


    def hit(self, enemy_idx, hero_bullet_power):
        self.enemy_hp[enemy_idx]-=hero_bullet_power
        if self.enemy_hp[enemy_idx]<=0:
            self.if_draw[enemy_idx]=False
        self.remove_enemies()           


    def MoveAndDo(self, mouse_pos, char, cooldown):
        dealt_dmg = False
        orient=0
        for i in range(len(self.enemy_list)):
            self.enemy_recs.pop(i)
            if mouse_pos[0]>self.enemy_X[i]:
                future_rect1 = pygame.Rect(self.enemy_X[i]+self.enemy_change_X[i], self.enemy_Y[i], EN_SIZE, EN_SIZE)  # Character.rect after movement
                orient+=1

                if not future_rect1.collidelistall(tile.TileMap.collision_map) and not future_rect1.collidelistall(self.enemy_recs) and not future_rect1.colliderect(char.rect):
                    self.enemy_X[i]+=self.enemy_change_X[i]
                if future_rect1.colliderect(char.rect) and self.shooter[i]==False and cooldown%self.enemy_attack_cooldown[i]==0:
                    char.hit(self.enemy_dmg[i])
                    dealt_dmg=True

            elif mouse_pos[0]<self.enemy_X[i]:
                future_rect1 = pygame.Rect(self.enemy_X[i]-self.enemy_change_X[i], self.enemy_Y[i], EN_SIZE, EN_SIZE)  # Character.rect after movement
                orient+=6

                if not future_rect1.collidelistall(tile.TileMap.collision_map) and not future_rect1.collidelistall(self.enemy_recs) and not future_rect1.colliderect(char.rect):
                    self.enemy_X[i]-=self.enemy_change_X[i]
                elif future_rect1.colliderect(char.rect) and self.shooter[i]==False and cooldown%self.enemy_attack_cooldown[i]==0:
                    char.hit(self.enemy_dmg[i])
                    dealt_dmg=True


            if mouse_pos[1]>self.enemy_Y[i]:
                future_rect1 = pygame.Rect(self.enemy_X[i], self.enemy_Y[i]+self.enemy_change_Y[i], EN_SIZE, EN_SIZE)  # Character.rect after movement
                orient+=4

                if not future_rect1.collidelistall(tile.TileMap.collision_map) and not future_rect1.collidelistall(self.enemy_recs) and not future_rect1.colliderect(char.rect):
                    self.enemy_Y[i]+=self.enemy_change_Y[i]
                elif future_rect1.colliderect(char.rect) and self.shooter[i]==False and cooldown%self.enemy_attack_cooldown[i]==0:
                    if dealt_dmg == False:
                        char.hit(self.enemy_dmg[i])

            elif mouse_pos[1]<self.enemy_Y[i]:
                future_rect1 = pygame.Rect(self.enemy_X[i], self.enemy_Y[i]-self.enemy_change_Y[i], EN_SIZE, EN_SIZE)  # Character.rect after movement
                orient+=2

                if not future_rect1.collidelistall(tile.TileMap.collision_map) and not future_rect1.collidelistall(self.enemy_recs) and not future_rect1.colliderect(char.rect):
                    self.enemy_Y[i]-=self.enemy_change_Y[i]
                elif future_rect1.colliderect(char.rect) and self.shooter[i]==False and cooldown%self.enemy_attack_cooldown[i]==0:
                    self.enemy_Y[i]-=self.enemy_change_Y[i]
                    if dealt_dmg == False:
                        char.hit(self.enemy_dmg[i])


            if dealt_dmg==False and self.shooter[i]==True and (cooldown%self.enemy_attack_cooldown[i]==0) and (orient in {1, 2, 3, 4, 5, 6, 8, 10}):
                self.enemy_bullets.append(Bullet(self.enemy_X[i] , self.enemy_Y[i] , 4, (0,0,0), orient, self.enemy_dmg[i]))

            dealt_dmg = False
            self.enemy_recs.insert(i, pygame.Rect(self.enemy_X[i], self.enemy_Y[i], EN_SIZE, EN_SIZE))
