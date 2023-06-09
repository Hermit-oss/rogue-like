import random
import os
from tile import TileMap
from utility import csv_reader

MAPS_PATH = "assets/maps/"
TILE_SIZE = 40

class Room():
    def __init__(self, x_coord, y_coord):
        maps = os.listdir(MAPS_PATH)
        random_map = random.choice(maps)
        map_path = os.path.join(MAPS_PATH, random_map)
        self.tile_map = TileMap(csv_reader(map_path), TILE_SIZE)
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord

    def draw(self, surface):
        self.tile_map.draw(surface)

    def get_coordinates(self):
        return (self.x_coordinate, self.y_coordinate)
