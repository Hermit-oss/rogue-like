import pygame
import os
import csv

# RESOURCES
FONT_PATH = './assets/font/yoster.ttf'

# Reads the .csv file and stores it
def csv_reader(filename):
    map = []
    # Try to open the specified file and return the list
    try:
        with open(os.path.join(filename)) as map_data:
            map_data = csv.reader(map_data, delimiter=',')
            for row in map_data:
                map.append(list(row))
        return map
    # Otherwise print the error and return an empty list
    except Exception as e:
        print(e)
        return map

# Returns the font at FONT_PATH in a desired size
def get_font(size):
    # Try to get the font and return it
    try:
        return pygame.font.Font(FONT_PATH, size)
    # Otherwise print the error and return the default font
    except Exception as e:
        print(e)
        return pygame.font.Font(pygame.font.get_default_font(), size)
