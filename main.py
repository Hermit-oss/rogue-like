import pygame

import tile
from bullet import *
from box_bomb import *
from character import Character
from utility import csv_reader
from tile import TileMap, enemy_class
from room import Room
from objects import *
# Define some constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create the rooms
file_to_copy="./assets/map/map2.csv"
genre_objects(file_to_copy) #Podajemy plik do skopiowania, zwraca zmieniony plik map1.csv (z przedmiotami)

tile_map = TileMap(csv_reader("./assets/map/map1.csv"))
rooms = [Room(tile_map), Room(tile_map), Room(tile_map)]
ch = Character(100, 100, 0.3, 3)


bullets = []
boxes,bombs=genre_boxes()
facing =0

# Set the current room
current_room_index = 0
current_room = rooms[current_room_index]

def redrawGameWindow():
    current_room.draw(screen)
    #current_room.tile_map.enemies.move(pygame.mouse.get_pos())
    current_room.tile_map.enemies.move((ch.x, ch.y))
    pygame.draw.rect(screen, ch.color, ch.rect)
    for bullet in bullets:
        bullet.draw(screen)
        # Update the screen
    pygame.display.flip()
    
    pygame.display.update()

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
            
    if key[pygame.K_c]:
        if len(bullets) < 5:
            facing=ch.orientation
            bullets.append(Bullet(ch.x , ch.y , 4, (0,0,0), facing))
    Bullet.shoot(screen,bullets,SCREEN_WIDTH,boxes, bombs)
    
    if key[pygame.K_q]:
        run = False
    Character.update(ch)


    if ch.status == 0:
        pass
        # TO DO: You are dead screen

    # Draw the current room

    

    redrawGameWindow()

# Quit pygame
pygame.quit()
