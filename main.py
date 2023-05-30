import pygame
import box_bomb
from bullet import *
from character import Character
from utility import csv_reader
from tile import TileMap
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
ch = Character(100, 100, 0.3, 3,5) #x,y,speed,health,causing damage


bullets = []

boxes,bombs=box_bomb.genre_boxes()
facing =0

# Set the current room
current_room_index = 0
current_room = rooms[current_room_index]

def redrawGameWindow():
    current_room.draw(screen)
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
        if len(bullets) < 3: #max 3 pociski
            facing=ch.orientation # w ktora maja leciec 
            bullets.append(Bullet(ch.x , ch.y , 4, (0,0,0), facing,ch.causing_damage)) 
            
    
    if key[pygame.K_m]:
        print("kasa",box_bomb.money_amount)
    Bullet.shoot(bullets,SCREEN_WIDTH,SCREEN_HEIGHT,boxes, bombs,ch.causing_damage)
    


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
