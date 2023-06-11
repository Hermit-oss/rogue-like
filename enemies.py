import random
import pygame
import tile

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
                self.enemy_hp.append(15)
            elif enemy_type==1:                 #op typu 1, bedzie strzelal i ucieka od gracza. nie bardzo twardy
#                self.enemies_imgs.append(pygame.image.load("assets/imgs/strzelacz.png"))
                self.enemy_recs.append(pygame.Rect(enemy_X, enemy_Y, EN_SIZE, EN_SIZE))
                self.enemy_colors.append(ONE)
                self.enemy_change_X.append(-2)
                self.enemy_change_Y.append(-2)
                self.enemy_hp.append(10)
            else:                               #op typu 2, biegnie do gracza, szybko, miękki
#                self.enemies_imgs.append(pygame.image.load("assets/imgs/amognus.png"))
                self.enemy_recs.append(pygame.Rect(enemy_X, enemy_Y, EN_SIZE, EN_SIZE))
                self.enemy_colors.append(TWO)
                self.enemy_change_X.append(4)
                self.enemy_change_Y.append(4)
                self.enemy_hp.append(5)
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
                i-=1
                length-=1
            i+=1

    def hit(self, enemy_idx, hero_bullet_power):
        self.enemy_hp[enemy_idx]-=hero_bullet_power
        if self.enemy_hp[enemy_idx]<=0:
            self.if_draw[enemy_idx]=False
        self.remove_enemies()           


    def MoveAndDo(self, mouse_pos):
        for i in range(len(self.enemy_list)):
            #current_rect = self.enemy_recs[i]
            self.enemy_recs.pop(i)
            if mouse_pos[0]>self.enemy_X[i]:
                future_rect1 = pygame.Rect(self.enemy_X[i]+self.enemy_change_X[i], self.enemy_Y[i], EN_SIZE, EN_SIZE)  # Character.rect after movement

                if not future_rect1.collidelistall(tile.TileMap.collision_map) and not future_rect1.collidelistall(self.enemy_recs):
                    self.enemy_X[i]+=self.enemy_change_X[i]
            elif mouse_pos[0]<self.enemy_X[i]:
                future_rect1 = pygame.Rect(self.enemy_X[i]-self.enemy_change_X[i], self.enemy_Y[i], EN_SIZE, EN_SIZE)  # Character.rect after movement

                if not future_rect1.collidelistall(tile.TileMap.collision_map) and not future_rect1.collidelistall(self.enemy_recs):
                    self.enemy_X[i]-=self.enemy_change_X[i]


            if mouse_pos[1]>self.enemy_Y[i]:
                future_rect1 = pygame.Rect(self.enemy_X[i], self.enemy_Y[i]+self.enemy_change_Y[i], EN_SIZE, EN_SIZE)  # Character.rect after movement

                if not future_rect1.collidelistall(tile.TileMap.collision_map) and not future_rect1.collidelistall(self.enemy_recs):
                    self.enemy_Y[i]+=self.enemy_change_Y[i]
            elif mouse_pos[1]<self.enemy_Y[i]:
                future_rect1 = pygame.Rect(self.enemy_X[i], self.enemy_Y[i]-self.enemy_change_Y[i], EN_SIZE, EN_SIZE)  # Character.rect after movement

                if not future_rect1.collidelistall(tile.TileMap.collision_map) and not future_rect1.collidelistall(self.enemy_recs):
                    self.enemy_Y[i]-=self.enemy_change_Y[i]
            
            self.enemy_recs.insert(i, pygame.Rect(self.enemy_X[i], self.enemy_Y[i], EN_SIZE, EN_SIZE) )
            #self.enemy_recs[i]=pygame.Rect(self.enemy_X[i], self.enemy_Y[i], EN_SIZE, EN_SIZE)         