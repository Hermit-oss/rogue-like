import random
import box_bomb
import os
from tile import TileMap
from utility import csv_reader
from objects import genre_objects
import pygame
from enemies import enemy_class

MAPS_PATH = "assets/maps/"
MAPS_OBJ = "assets/mapsObj/"
TILE_SIZE = 40

class Room():
    def __init__(self, surface, x_coord, y_coord):
        maps = os.listdir(MAPS_PATH)
        mapsObj = os.listdir(MAPS_OBJ)
        random_map = random.choice(maps)
        random_map_obj = random.choice(mapsObj)
        map_path = os.path.join(MAPS_PATH, random_map)
        map_obj = os.path.join(MAPS_OBJ, random_map_obj)
        genre_objects(map_path, map_obj)
        self.tile_map = TileMap(csv_reader(map_obj), TILE_SIZE)
       
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord

        self.boxesPower = []
        self.boxesHealth = []
        self.enemies = enemy_class(surface)
        self.isGenerated = False

        
        

    def draw(self, surface):
        self.tile_map.draw(surface)
        box_bomb.Box.show_message(surface)
        if(not self.isGenerated):
            self.boxesPower,self.boxesHealth=box_bomb.genre_boxes(self.tile_map, surface)
            self.isGenerated = True
        self.enemies.display_enemy(surface)

    def place_enemies(self, enemy_check):
        if enemy_check==True:
            for checked_enemy in range(len(self.enemies.enemy_list)):
                temp_rect=pygame.Rect(self.enemies.enemy_X[checked_enemy], self.enemies.enemy_Y[checked_enemy], 16, 16)
                if not temp_rect.collidelistall(self.tile_map.collision_map):
                    self.enemies.if_draw[checked_enemy]=True
            self.enemies.remove_enemies()


    def get_coordinates(self):
        return (self.x_coordinate, self.y_coordinate)

    def get_tile_map(self):
        return self.tile_map

    def remove_door(self, direction):
        self.tile_map.door_remover(direction)