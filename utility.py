import pygame
import os
import csv

# RESOURCES
FONT_PATH = './assets/fonts/yoster.ttf'
DEFAULT_FONT_SIZE = 10
DEFAULT_ROOM_LAYOUT = [
    [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
    [-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2],
    [-2,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-2],
    [-2,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-2],
    [-2,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-2],
    [-2,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-2],
    [-2,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-2],
    [-2,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-2],
    [-2,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-2],
    [-2,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-2],
    [-2,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-2],
    [-2,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-2],
    [-2,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-2],
    [-2,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-2],
    [-2,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-2],
    [-2,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-2],
    [-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2],
    [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2]
]

def csv_reader(filename):
    """
    Read a .csv file (comma delimiter) and return the matrix.

    Parameters:
        filename (str): The path to the .csv file.

    Returns:
        list: The map as a matrix.
    """
    map = []
    try:
        with open(os.path.join(filename)) as map_data:
            map_data = csv.reader(map_data, delimiter=',')
            for row in map_data:
                map.append(list(row))
        return map
    except Exception as e:
        print(e)
        map_data = csv.reader(DEFAULT_ROOM_LAYOUT, delimiter=',')
        for row in map_data:
            map.append(list(row))
        return map

def get_font(size):
    """
    Get a font object in the specified size.

    Parameters:
        size (int): The desired font size.

    Returns:
        pygame.font.Font: The font object.
    """
    try:
        return pygame.font.Font(FONT_PATH, size)
    except Exception as e:
        print(e)
        try:
            return pygame.font.Font(pygame.font.get_default_font(), size)
        except Exception as e:
            print(e)
            return pygame.font.Font(pygame.font.get_default_font(), DEFAULT_FONT_SIZE)
