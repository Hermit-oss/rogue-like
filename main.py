import pygame

import tile
from character import Character
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
ch = Character(100, 100)
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

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        ch.move_left()
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        ch.move_right()
    if key[pygame.K_UP] or key[pygame.K_w]:
        ch.move_up()
    if key[pygame.K_DOWN] or key[pygame.K_s]:
        ch.move_down()
    if key[pygame.K_q]:
        run = False
    Character.update(ch)

    # Draw the current room
    current_room.draw(screen)
    pygame.draw.rect(screen, (31, 14, 65), ch.rect)
    # Update the screen
    pygame.display.flip()

# Quit pygame
pygame.quit()
