import random
import pygame
import tile

ZERO=(155,155,0)
ONE=(0,155,155)
TWO=(155,0,155)
EN_SIZE = 16


class enemy_class():
    def __init__(self):
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
        amount = random.randint(3, 5)
        for i in range(amount):
            enemy_type = random.randint(0,2)  #losuje rodzaj oponenta
            enemy_X=random.randint(0, 300)
            enemy_Y=random.randint(0,300)

            self.enemy_list.append(enemy_type)
            self.enemy_X.append(enemy_X)
            self.enemy_Y.append(enemy_Y)
            self.if_draw.append(False)

            if enemy_type==0:                   #op typu 0, nie za szybki idzie w kierunku gracza, troszkę twardszy
#                self.enemies_imgs.append(pygame.image.load("assets/imgs/slow_biegacz.png"))
                self.enemy_recs.append(pygame.Rect(enemy_X, enemy_Y, EN_SIZE, EN_SIZE))
                self.enemy_colors.append(ZERO)
                self.enemy_change_X.append(0.2)
                self.enemy_change_Y.append(0.2)
                self.enemy_hp.append(5)
            elif enemy_type==1:                 #op typu 1, bedzie strzelal i ucieka od gracza. nie bardzo twardy
#                self.enemies_imgs.append(pygame.image.load("assets/imgs/strzelacz.png"))
                self.enemy_recs.append(pygame.Rect(enemy_X, enemy_Y, EN_SIZE, EN_SIZE))
                self.enemy_colors.append(ONE)
                self.enemy_change_X.append(-0.1)
                self.enemy_change_Y.append(-0.1)
                self.enemy_hp.append(3)
            else:                               #op typu 2, biegnie do gracza, szybko, miękki
#                self.enemies_imgs.append(pygame.image.load("assets/imgs/amognus.png"))
                self.enemy_recs.append(pygame.Rect(enemy_X, enemy_Y, EN_SIZE, EN_SIZE))
                self.enemy_colors.append(TWO)
                self.enemy_change_X.append(0.3)
                self.enemy_change_Y.append(0.3)
                self.enemy_hp.append(1)
#            width = self.enemies_imgs[i].get_width()
#            height = self.enemies_imgs[i].get_height()
#            self.enemies_imgs[i]=pygame.transform.scale(self.enemies_imgs[i], (int(0.05*width), int(0.05*height)))


    def display_enemy(self, screen):
        for i in range(len(self.enemy_list)):
            if self.if_draw[i]==True:
                pygame.draw.rect(screen, self.enemy_colors[i], self.enemy_recs[i])

#                screen.blit(self.enemies_imgs[i], (self.enemy_X[i], self.enemy_Y[i]))

    def move(self, mouse_pos):
        for i in range(len(self.enemy_list)):
            if mouse_pos[0]>self.enemy_X[i] and mouse_pos[1]>self.enemy_Y[i]:
                future_rect = pygame.Rect(self.enemy_X[i]+self.enemy_change_X[i], self.enemy_Y[i]+self.enemy_change_Y[i], EN_SIZE, EN_SIZE)  # Character.rect after movement

                if future_rect.collidelistall(tile.TileMap.cmap):  # Check if next movement will cause collision
                    pass
                else:
                    self.enemy_X[i]+=self.enemy_change_X[i]
                    self.enemy_Y[i]+=self.enemy_change_Y[i]

            elif mouse_pos[0]>self.enemy_X[i]:
                future_rect = pygame.Rect(self.enemy_X[i]+self.enemy_change_X[i], self.enemy_Y[i], EN_SIZE, EN_SIZE)  # Character.rect after movement

                if future_rect.collidelistall(tile.TileMap.cmap):  # Check if next movement will cause collision
                    pass
                else:
                    self.enemy_X[i]+=self.enemy_change_X[i]

            elif mouse_pos[0]>self.enemy_Y[i]:
                future_rect = pygame.Rect(self.enemy_X[i], self.enemy_Y[i]+self.enemy_change_Y[i], EN_SIZE, EN_SIZE)  # Character.rect after movement

                if future_rect.collidelistall(tile.TileMap.cmap):  # Check if next movement will cause collision
                    pass
                else:
                    self.enemy_Y[i]+=self.enemy_change_Y[i]


            if mouse_pos[0]<self.enemy_X[i] and mouse_pos[1]<self.enemy_Y[i]:
                future_rect = pygame.Rect(self.enemy_X[i]-self.enemy_change_X[i], self.enemy_Y[i]-self.enemy_change_Y[i], EN_SIZE, EN_SIZE)  # Character.rect after movement

                if future_rect.collidelistall(tile.TileMap.cmap):  # Check if next movement will cause collision
                    pass
                else:
                    self.enemy_X[i]-=self.enemy_change_X[i]
                    self.enemy_Y[i]-=self.enemy_change_Y[i]

            elif mouse_pos[0]<self.enemy_X[i]:
                future_rect = pygame.Rect(self.enemy_X[i]-self.enemy_change_X[i], self.enemy_Y[i], EN_SIZE, EN_SIZE)  # Character.rect after movement

                if future_rect.collidelistall(tile.TileMap.cmap):  # Check if next movement will cause collision
                    pass
                else:
                    self.enemy_X[i]-=self.enemy_change_X[i]

            elif mouse_pos[0]<self.enemy_Y[i]:
                future_rect = pygame.Rect(self.enemy_X[i], self.enemy_Y[i]-self.enemy_change_Y[i], EN_SIZE, EN_SIZE)  # Character.rect after movement

                if future_rect.collidelistall(tile.TileMap.cmap):  # Check if next movement will cause collision
                    pass
                else:
                    self.enemy_Y[i]-=self.enemy_change_Y[i]

            self.enemy_recs[i]=pygame.Rect(self.enemy_X[i], self.enemy_Y[i], EN_SIZE, EN_SIZE)         
            '''
            if mouse_pos[0]>self.enemy_X[i]:
                if self.enemy_change_X[i]>0 and self.enemy_X[i]<950:
                    self.enemy_X[i]+=self.enemy_change_X[i]
                elif self.enemy_change_X[i]<0 and self.enemy_X[i]>0:
                    self.enemy_X[i]+=self.enemy_change_X[i]
            elif mouse_pos[0]<self.enemy_X[i]:
                if self.enemy_change_X[i]<0 and self.enemy_X[i]<950:
                    self.enemy_X[i]-=self.enemy_change_X[i]
                elif self.enemy_change_X[i]>0 and self.enemy_X[i]>0:
                    self.enemy_X[i]-=self.enemy_change_X[i]
            

            if mouse_pos[1]>self.enemy_Y[i]:
                if self.enemy_change_Y[i]>0 and self.enemy_Y[i]<950:
                    self.enemy_Y[i]+=self.enemy_change_Y[i]
                elif self.enemy_change_Y[i]<0 and self.enemy_Y[i]>0:
                    self.enemy_Y[i]+=self.enemy_change_Y[i]
            elif mouse_pos[1]<self.enemy_Y[i]:
                if self.enemy_change_Y[i]<0 and self.enemy_Y[i]<950:
                    self.enemy_Y[i]-=self.enemy_change_Y[i]
                elif self.enemy_change_Y[i]>0 and self.enemy_Y[i]>0:
                    self.enemy_Y[i]-=self.enemy_change_Y[i]
            '''
