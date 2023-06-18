
from time import sleep
import pygame, sys, os
from button import Button
from char_menu import Char_menu
import pygame
from utility import csv_reader
from tile import Tile, TileMap
from map import MapGenerator
from character import Character
from bullet import Bullet


pygame.init()

Start_music=pygame.mixer.Sound("assets/sound/background.wav")
Start_music.play(-1)

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
WIDTH, HEIGHT = SCREEN.get_size() 
CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2
fullscreen = False

BG = pygame.image.load("assets/images/bg.png")
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

def get_font(size): 
    return pygame.font.Font('assets/fonts/yoster.ttf', size)

def char_menu(fullscreen):
    
    w, h = SCREEN.get_size()
    WINDOW_SIZE= (w,h)

    if fullscreen:
        pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN)
    else:
        pygame.display.set_mode(WINDOW_SIZE)
    SCREEN.blit(BG, (0, 0))
    Run = True
    CHAR_MENU = Char_menu(SCREEN, CENTER_X, CENTER_Y)


    while Run:
        pygame.display.update()
        


        MOUSE_POS = pygame.mouse.get_pos()
        char_change = CHAR_MENU.change_char(MOUSE_POS)

        BACK_BUTTON = Button(image=None, x=100, y=680,
                            text_input="BACK", font=get_font(50), base_color="red4", hovering_color="White", scale=1)
        BACK_BUTTON.update(SCREEN)
        PLAY_BUTTON = Button(image=None, x=640, y=540,
                            text_input="PLAY", font=get_font(90), base_color="red4", hovering_color="White", scale=1)
        PLAY_BUTTON.update(SCREEN)
        TEXT_BUTTON = Button(image=None, x=640, y=100,
                            text_input="CHOOSE YOUR CHARACTER:", font=get_font(60), base_color="red4", hovering_color="White", scale=1)
        TEXT_BUTTON.update(SCREEN)

        if char_change[1]:
            CHAR_MENU.show_choice(SCREEN)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    fullscreen = not fullscreen  # Toggle fullscreen
                    if fullscreen:
                        pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN)
                    else:
                        pygame.display.set_mode(WINDOW_SIZE)
 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.interaction(MOUSE_POS):
                    main_menu(fullscreen)
                if PLAY_BUTTON.interaction(MOUSE_POS):
                     game(CHAR_MENU.get_chosen_color(),fullscreen)

        pygame.display.update()


 

def game(chosen_color,fullscreen):
    w, h = SCREEN.get_size()
    WINDOW_SIZE= (w,h)

    if fullscreen:
        pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN)
    else:
        pygame.display.set_mode(WINDOW_SIZE)
    
    clock = pygame.time.Clock()

    generator = MapGenerator(9, 13)
    generator.generate_map(SCREEN)
    spawn = generator.get_spawn_room()
    actual_room = spawn
    character = Character(3, 3, chosen_color)
    enemy_check=True
    bullets=[]
    cooldown_counter=0
    TILE_SIZE = 40


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
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
        SCREEN.fill((255, 255, 255))  # Fill the screen with white
        if key[pygame.K_c]:
            if len(bullets) < 5: #max 5 pociskow
                if cooldown_counter%10==0:
                    bullets.append(Bullet(character.x , character.y , 4, (0,0,0), character.orientation, character.causing_damage))
        if key[pygame.K_m]:
            print("Zdrowie to: ",character.health_points)
        if key[pygame.K_n]:
            print("Sila pocisku to: ",character.causing_damage)
        if key[pygame.K_ESCAPE]:
            pause()
        if character.health_points <= 0:
            sleep(1)
            game_over(fullscreen)

        actual_room.draw(SCREEN)
       
        Bullet.shoot(bullets, SCREEN.get_size()[0], SCREEN.get_size()[1], actual_room, character.causing_damage, False, character)
        Bullet.shoot(actual_room.enemies.enemy_bullets, SCREEN.get_size()[0], SCREEN.get_size()[1], actual_room, character.causing_damage, True, character)

        for bullet in bullets:
            bullet.draw(SCREEN)

        for bullet in actual_room.enemies.enemy_bullets:
            bullet.draw(SCREEN)

        actual_room.place_enemies(enemy_check)
        actual_room.enemies.MoveAndDo((character.x, character.y), character, cooldown_counter)

        generator.display_map(SCREEN, actual_room.get_coordinates())
        actual_room, enemy_check = Character.update(character, actual_room, generator)
        pygame.draw.rect(SCREEN, character.color, character.rect)
        
        pygame.display.flip()
        clock.tick(60)
        cooldown_counter+=1

def game_over(fullscreen):
    while True:
        SCREEN.fill((0, 0, 0))

        GAME_OVER_TEXT = get_font(90).render("GAME OVER", True, "red4")
        GAME_OVER_RECT = GAME_OVER_TEXT.get_rect(center=(CENTER_X, 100))


        RESTART = Button(image=None, x=CENTER_X, y=260,
                                    text_input="RESTART", font=get_font(60), base_color="WHITE", hovering_color="White", scale=1)
        RESTART.update(SCREEN)

        MENU = Button(image=None, x=CENTER_X, y=360,
                                    text_input="MAIN MENU", font=get_font(60), base_color="WHITE", hovering_color="White", scale=1)
        MENU.update(SCREEN)

        QUIT_BUTTON = Button(image=None, x=CENTER_X, y=460,
                                    text_input="QUIT", font=get_font(60), base_color="WHITE", hovering_color="White", scale=1)
        QUIT_BUTTON.update(SCREEN)
        
        SCREEN.blit(GAME_OVER_TEXT, GAME_OVER_RECT)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if RESTART.interaction(event.pos):
                        char_menu(fullscreen)
                    if QUIT_BUTTON.interaction(event.pos):
                        pygame.quit()
                        sys.exit()
                    if MENU.interaction(event.pos):
                        main_menu(fullscreen)

            pygame.display.flip()

def pause():

        SCREEN.blit(BG, (0, 0))
        PAUSE_MOUSE_POS = pygame.mouse.get_pos()

        PAUSE_TEXT1 = get_font(90).render("PAUSE", True, "red4")
        PAUSE_RECT1 = PAUSE_TEXT1.get_rect(center=(CENTER_X, 100))
        SCREEN.blit(PAUSE_TEXT1, PAUSE_RECT1)


        paused = True

        CONTINUE = Button(image=None, x=CENTER_X, y=230, 
                                text_input="CONTINUE", font=get_font(60), base_color="White", hovering_color="Brown",scale=1)
        CONTINUE.update(SCREEN)

        SAVE_GAME = Button(image=None, x=CENTER_X, y=330, 
                                text_input="SAVE GAME", font=get_font(60), base_color="White", hovering_color="Brown",scale=1)
        SAVE_GAME.update(SCREEN)

        MENU = Button(image=None, x=CENTER_X, y=430,
                                text_input="MAIN MENU", font=get_font(60), base_color="WHITE", hovering_color="White", scale=1)
        MENU.update(SCREEN)

        QUIT_BUTTON = Button(image=None, x=CENTER_X, y=530,
                                text_input="QUIT", font=get_font(60), base_color="WHITE", hovering_color="White", scale=1)
        QUIT_BUTTON.update(SCREEN)

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if CONTINUE.interaction(event.pos):
                        paused = False
                    if QUIT_BUTTON.interaction(event.pos):
                        pygame.quit()
                        sys.exit()
                    if MENU.interaction(event.pos):
                        main_menu(fullscreen)


            pygame.display.flip()

def new_game():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("***GAME***", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, x=460, y=460, 
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Brown",scale=1)

        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.interaction(PLAY_MOUSE_POS):
                    main_menu(fullscreen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

        pygame.display.update()
    
def load_game():
    while True:
        LOAD_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        LOAD_TEXT = get_font(45).render("***LOADGAME***", True, "White")
        LOAD_RECT = LOAD_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(LOAD_TEXT, LOAD_RECT)

        LOAD_BACK = Button(image=None, x=100, y=680,
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green", scale = 1)

        LOAD_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LOAD_BACK.interaction(LOAD_MOUSE_POS):
                    main_menu(fullscreen)

        pygame.display.update()

def save_game():
    while True:
        SAVE_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("green")
        
        SAVE_TEXT = get_font(45).render("***SAVE***", True, "Black")
        SAVE_RECT = SAVE_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(SAVE_TEXT, SAVE_RECT)


        SAVE_BACK = Button(image=None, x=100, y=680,
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green", scale = 1)

        SAVE_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SAVE_BACK.interaction(SAVE_MOUSE_POS):
                    main_menu(fullscreen)

        pygame.display.update()

def options():
    current_gamma = 1

    while True:
        SCREEN.blit(BG, (0, 0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()


        OPTIONS_TEXT = get_font(45).render("***OPTIONS***", True, "brown4")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        BACK_BUTTON = Button(image=None, x=100, y=680,
                             text_input="BACK", font=get_font(50), base_color="red4", hovering_color="Green", scale=1)
        BACK_BUTTON.update(SCREEN)

        INCREASE_GAMMA_BUTTON = Button(image=None, x=CENTER_X, y=300,
                                       text_input="Increase Gamma", font=get_font(50), base_color="red4", hovering_color="Green", scale=1)
        INCREASE_GAMMA_BUTTON.update(SCREEN)

        DECREASE_GAMMA_BUTTON = Button(image=None, x=CENTER_X, y=400,
                                       text_input="Decrease Gamma", font=get_font(50), base_color="red4", hovering_color="Green", scale=1)
        DECREASE_GAMMA_BUTTON.update(SCREEN)

        fullscreen = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.interaction(OPTIONS_MOUSE_POS):
                    main_menu(fullscreen)
                if INCREASE_GAMMA_BUTTON.interaction(OPTIONS_MOUSE_POS):
                    current_gamma += 0.1
                    pygame.display.set_gamma(current_gamma)
                   
                if DECREASE_GAMMA_BUTTON.interaction(OPTIONS_MOUSE_POS):
                    current_gamma -= 0.1
                    pygame.display.set_gamma(current_gamma)
                    
        pygame.display.update()


def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  SCREEN.blit(img, (x, y))



def main_menu(fullscreen):
    while True:
        w, h = SCREEN.get_size()
        WINDOW_SIZE= (w,h)
        
        SCREEN.blit(BG, (0, 0))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        MENU_TEXT = get_font(90).render("GAME NAME!!!!", True, "red4")
        MENU_RECT = MENU_TEXT.get_rect(center=(CENTER_X, 100))

        PLAY_BUTTON = Button(image=None, x=CENTER_X, y=CENTER_Y - 100,
                            text_input="PLAY", font=get_font(70), base_color="brown4", hovering_color="White", scale=1)
        LOAD_BUTTON = Button(image=None, x=CENTER_X, y=CENTER_Y,
                            text_input="LOAD GAME", font=get_font(70),base_color="brown4", hovering_color="White", scale=1)
        OPTIONS_BUTTON = Button(image=None, x=CENTER_X, y=CENTER_Y + 100, 
                            text_input="OPTIONS", font=get_font(70), base_color="brown4", hovering_color="White", scale=1)
        QUIT_BUTTON = Button(image=None, x=CENTER_X, y=CENTER_Y + 200,
                            text_input="QUIT", font=get_font(70), base_color="brown4", hovering_color="White", scale=1)
        SOUND_BUTTON_NO = Button(image=pygame.image.load('assets/images/no_sound.png'),x=50, y=50, 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green", scale=1.5)
        SOUND_BUTTON_LOW = Button(image=pygame.image.load('assets/images/low_sound.png'),x=100, y=50,
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green", scale=1.5)
        SOUND_BUTTON_MAX = Button(image=pygame.image.load('assets/images/sound_max.png'),x=140, y=50,
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green", scale=1.5)

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        PLAY_BUTTON.interaction(MENU_MOUSE_POS)

        for button in [PLAY_BUTTON, LOAD_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, SOUND_BUTTON_NO, SOUND_BUTTON_LOW, SOUND_BUTTON_MAX]:
            button.update(SCREEN)

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    fullscreen = not fullscreen  # Toggle fullscreen
                    if fullscreen:
                        pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN)
                    else:
                        pygame.display.set_mode(WINDOW_SIZE)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.interaction(MENU_MOUSE_POS):
                    char_menu(fullscreen)
                if LOAD_BUTTON.interaction(MENU_MOUSE_POS):
                    load_game()
                if OPTIONS_BUTTON.interaction(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.interaction(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if SOUND_BUTTON_LOW.interaction(MENU_MOUSE_POS):
                    Start_music.set_volume(0.3)
                if SOUND_BUTTON_NO.interaction(MENU_MOUSE_POS):
                    Start_music.set_volume(0)
                if SOUND_BUTTON_MAX.interaction(MENU_MOUSE_POS):
                    Start_music.set_volume(1)

        pygame.display.update()


main_menu(fullscreen)