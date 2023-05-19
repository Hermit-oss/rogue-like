import arcade
import random
import pygame

class enemy_class():
    def __init__(self):
        self.enemy_list=[]
        self.enemy_X=[]
        self.enemy_Y=[]
        self.enemies_imgs=[]
        self.enemy_change_X=[]
        self.enemy_change_Y=[]
        self.enemy_hp=[]
        amount = random.randint(1, 5)
        for i in range(amount):
            enemy_type = random.randint(0,2)  #losuje rodzaj oponenta
            enemy_X=random.randint(0, 1000)
            enemy_Y=random.randint(0,1000)
            self.enemy_list.append(enemy_type)
            self.enemy_X.append(enemy_X)
            self.enemy_Y.append(enemy_Y)
            if enemy_type==0:                   #op typu 0, nie za szybki idzie w kierunku gracza, troszkę twardszy
                self.enemies_imgs.append(pygame.image.load("assets/imgs/slow_biegacz.png"))
                self.enemy_change_X.append(0.2)
                self.enemy_change_Y.append(0.2)
                self.enemy_hp.append(5)
            elif enemy_type==1:                 #op typu 1, bedzie strzelal i ucieka od gracza. nie bardzo twardy
                self.enemies_imgs.append(pygame.image.load("assets/imgs/strzelacz.png"))
                self.enemy_change_X.append(-0.1)
                self.enemy_change_Y.append(-0.1)
                self.enemy_hp.append(3)
            else:                               #op typu 2, biegnie do gracza, szybko, miękki
                self.enemies_imgs.append(pygame.image.load("assets/imgs/amognus.png"))
                self.enemy_change_X.append(0.5)
                self.enemy_change_Y.append(0.5)
                self.enemy_hp.append(1)
            width = self.enemies_imgs[i].get_width()
            height = self.enemies_imgs[i].get_height()
            self.enemies_imgs[i]=pygame.transform.scale(self.enemies_imgs[i], (int(0.1*width), int(0.1*height)))

    def display_enemy(self, screen):
        for i in range(len(self.enemy_list)):
            screen.blit(self.enemies_imgs[i], (self.enemy_X[i], self.enemy_Y[i]))

    def move(self, mouse_pos):
        for i in range(len(self.enemy_list)):
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
            