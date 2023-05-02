import pygame
from utility import csv_reader
from tile import TileMap
from room import Room

# Define some constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create the rooms
tile_map = TileMap(csv_reader("./assets/map/map1.csv"))
rooms = [Room(tile_map), Room(tile_map), Room(tile_map)]

# Set the current room
current_room_index = 0
current_room = rooms[current_room_index]

# Game loop
running = True
while running:
    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current_room_index = (current_room_index + 1) % len(rooms)
                current_room = rooms[current_room_index]


    # Draw the current room
    current_room.draw(screen)

    # Update the screen
    pygame.display.flip()

# Quit pygame
pygame.quit()
