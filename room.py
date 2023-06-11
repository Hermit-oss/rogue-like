import random
import box_bomb
import os
from tile import TileMap
from utility import csv_reader
from objects import genre_objects

MAPS_PATH = "assets/maps/"
MAPS_OBJ = "assets/mapsObj/"
TILE_SIZE = 40

class Room():
    def __init__(self, x_coord, y_coord):
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

    def draw(self, surface):
        self.tile_map.draw(surface)
        self.boxesPower,self.boxesHealth=box_bomb.genre_boxes(self.tile_map)

    def get_coordinates(self):
        return (self.x_coordinate, self.y_coordinate)

    def get_tile_map(self):
        return self.tile_map
