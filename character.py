import pygame
import tile


class Character(object):
    def __init__(self, x, y, speed):
        self.speed = speed
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 20, 20)

    def update(self):
        self.rect.update(self.x, self.y, 20, 20)

    def move_left(self):
        future_rect = pygame.Rect(self.x - self.speed, self.y, 20, 20)
        if future_rect.collidelistall(tile.TileMap.cmap):
            pass
        else:
            self.x -= self.speed

    def move_right(self):
        future_rect = pygame.Rect(self.x + self.speed, self.y, 20, 20)
        if future_rect.collidelistall(tile.TileMap.cmap):
            pass
        else:
            self.x += self.speed

    def move_down(self):
        future_rect = pygame.Rect(self.x, self.y + self.speed, 20, 20)
        if future_rect.collidelistall(tile.TileMap.cmap):
            pass
        else:
            self.y += self.speed

    def move_up(self):
        future_rect = pygame.Rect(self.x, self.y - self.speed, 20, 20)
        if future_rect.collidelistall(tile.TileMap.cmap):
            pass
        else:
            self.y -= self.speed
