import pygame
import tile

CHARACTER_SIZE = 16
I_FRAMES = 1500
COLOR_OF_CHARACTER_ALIVE = (31, 14, 65)
COLOR_OF_CHARACTER_DEAD = (255, 0, 2)


class Character(object):
    def __init__(self, x, y, speed, health_point):
        self.i_frames = I_FRAMES  # Invincibility frames, can't get hit in this time
        self.can_hit = 1  # 0 can't get hit, 1 can get hit
        self.color = COLOR_OF_CHARACTER_ALIVE
        self.status = 1  # 1 alive, 0 dead
        self.health_points = health_point  # How many hits can character take
        self.speed = speed  # Speed of character's movement
        self.x = x  # Position of character in x-axis
        self.y = y  # Position of character in y-axis
        self.rect = pygame.Rect(x, y, CHARACTER_SIZE, CHARACTER_SIZE)
        self.can_go_through_door = 1

        self.money=0 #how much money does character has
        self.bomb=0 # how many bombs does character has
        self.causing_damage=10 #how much damage can character cause
        self.orientation=1 # 1=left or 0=right orientation to shot bullets


    def update(self):
        self.rect.update(self.x, self.y, CHARACTER_SIZE, CHARACTER_SIZE)  # Update collision rect
        #if self.rect.collidelistall(tile.TileMap.dmap) and self.can_hit:  # Check if collide with list of tiles that causes damage
        #    self.health_points -= 1
        #    self.can_hit = 0
        #    self.i_frames = 0
        if (self.rect.colliderect(tile.TileMap.door_map[0]) or self.rect.colliderect(tile.TileMap.door_map[1])) and self.can_go_through_door:
            #Go up
            print("go up")
            self.can_go_through_door = 0

        if (self.rect.colliderect(tile.TileMap.door_map[2]) or self.rect.colliderect(tile.TileMap.door_map[4])) and self.can_go_through_door:
        # Go left
            print("go left")
            self.can_go_through_door = 0

        if (self.rect.colliderect(tile.TileMap.door_map[3]) or self.rect.colliderect(tile.TileMap.door_map[5])) and self.can_go_through_door:
        # Go right
            print("go right")
            self.can_go_through_door = 0

        if (self.rect.colliderect(tile.TileMap.door_map[6]) or self.rect.colliderect(tile.TileMap.door_map[7])) and self.can_go_through_door:
        # Go down
            print("go down")
            self.can_go_through_door = 0


        if self.i_frames < I_FRAMES and self.can_hit == 0:  # Increase i_frames every frame after hit
             self.i_frames += 1

        if self.i_frames == I_FRAMES and self.can_hit == 0:  # Check if character can be hit
            self.can_hit = 1 # Character can be hit

        if self.health_points <= 0 and self.status == 1:  # Check if character is dead
            self.status = 0  # Character is dead
            self.color = COLOR_OF_CHARACTER_DEAD

    def move_left(self):
        future_rect = pygame.Rect(self.x - self.speed, self.y, CHARACTER_SIZE, CHARACTER_SIZE)  # Character.rect after movement
        if future_rect.collidelistall(tile.TileMap.collision_map):  # Check if next movement will cause collision
            pass  # Collision -> No movement
        else:
            self.orientation=1
            self.x -= self.speed  # No collision -> Movement

    def move_right(self):
        future_rect = pygame.Rect(self.x + self.speed, self.y, CHARACTER_SIZE, CHARACTER_SIZE)
        if future_rect.collidelistall(tile.TileMap.collision_map):
            pass
        else:
            self.orientation=0
            self.x += self.speed

    def move_down(self):
        future_rect = pygame.Rect(self.x, self.y + self.speed, CHARACTER_SIZE, CHARACTER_SIZE)
        if future_rect.collidelistall(tile.TileMap.collision_map):
            pass
        else:
            self.y += self.speed

    def move_up(self):
        future_rect = pygame.Rect(self.x, self.y - self.speed, CHARACTER_SIZE, CHARACTER_SIZE)
        if future_rect.collidelistall(tile.TileMap.collision_map):
            pass
        else:
            self.y -= self.speed
