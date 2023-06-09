import pygame
from utility import csv_reader
from tile import Tile, TileMap
from map import MapGenerator
from character import Character
# Set up Pygame and the display
pygame.init()
WINDOW_SIZE = (1280, 720)
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

# Create an instance of the MapGenerator
generator = MapGenerator(9, 13)
generator.generate_map()
spawn = generator.get_spawn_room()
character = Character(640, 240, 2, 3)
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

    # Draw the tile map
    spawn.draw(screen)

    # Display the map
    generator.display_map(screen, spawn.get_coordinates())
    generator.display_map(screen, spawn.get_coordinates())
    Character.update(character)
    pygame.draw.rect(screen, character.color, character.rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
