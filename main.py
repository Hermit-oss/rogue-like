import pygame
from utility import csv_reader
from tile import Tile, TileMap
from map import MapGenerator
from character import Character
from bullet import Bullet

# Set up Pygame and the display
pygame.init()
WINDOW_SIZE = (1280, 720)
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

# Create an instance of the MapGenerator
generator = MapGenerator(9, 13)
generator.generate_map(screen)
spawn = generator.get_spawn_room()
actual_room = spawn
character = Character(3, 3)
enemy_check=True
bullets=[]
bullet_counter=0
# Create the TileMap object
TILE_SIZE = 40

fullscreen = False  # Flag to track fullscreen state

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                fullscreen = not fullscreen  # Toggle fullscreen

                # Set the display mode
                if fullscreen:
                    pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN)
                else:
                    pygame.display.set_mode(WINDOW_SIZE)
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        character.move_left()
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        character.move_right()
    if key[pygame.K_UP] or key[pygame.K_w]:
        character.move_up()
    if key[pygame.K_DOWN] or key[pygame.K_s]:
        character.move_down()
    screen.fill((255, 255, 255))  # Fill the screen with white
    if key[pygame.K_c]:
        if len(bullets) < 3: #max 3 pociski
            if bullet_counter%10==0:
                bullets.append(Bullet(character.x , character.y , 4, (0,0,0), character.orientation, character.causing_damage))

    # Draw the tile map
    actual_room.draw(screen)
       
    Bullet.shoot(bullets, screen.get_size()[0], screen.get_size()[1], actual_room, character.causing_damage)
    for bullet in bullets:
        bullet.draw(screen)

    actual_room.place_enemies(enemy_check)
    actual_room.enemies.MoveAndDo((character.x, character.y))

    # Display the map
    #generator.display_map(screen, actual_room.get_coordinates())
    generator.display_map(screen, actual_room.get_coordinates())
    actual_room, enemy_check = Character.update(character, actual_room, generator)
    pygame.draw.rect(screen, character.color, character.rect)

    pygame.display.flip()
    clock.tick(60)
    bullet_counter+=1

pygame.quit()
