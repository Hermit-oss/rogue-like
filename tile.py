import pygame
from utility import csv_reader
from box_bomb import Box
TILE_SIZE = 32

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW=(255,255,0)
PURPLE=(38,43,226)
MAGENTA=(255,0,255)



def csv_to_tile_map(csv_map):
    tile_map = []


class Tile(object):

    def __init__(self, collision, color, x, y):
        self.collision = collision
        self.color = color
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class TileMap():
    cmap = []  # Map of collisions
    dmap = []  # Map of tiles that cause damage
    box = []
    def __init__(self, data):
        self.width = len(data[0])
        self.height = len(data)
        self.tiles = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                val = int(data[y][x])
                collision = 1 if val in [-1, -2, 20, 30] else 0
                if val == 1 or val == 2:
                    color = pygame.Color('white')
                elif val == 0:
                    color = pygame.Color('red')
                elif val == -1:
                    color = pygame.Color('blue')
                elif val == 10:
                    color = pygame.Color('yellow')
                elif val == 20:
                    TileMap.box.append(tile.rect)
                    color = pygame.Color('purple')
                elif val == 30:
                    TileMap.box.append(tile.rect)
                    color = pygame.Color('magenta')
                else:
                    color = pygame.Color('black')
                tile = Tile(collision, color, x * TILE_SIZE, y * TILE_SIZE)
                if tile.collision == 1:  # Check collision
                    TileMap.cmap.append(tile.rect)  # Add tile to map of collisions
                if val == 10:  # Check if tile is yellow
                    TileMap.dmap.append(tile.rect)  # Add tile to map of tiles that cause damage
                row.append(tile)
            self.tiles.append(row)


    def draw(self, screen):
        for row in self.tile_map:
            for tile in row:
                tile.draw(screen)

