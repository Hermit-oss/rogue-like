import pygame
from spritesheet import SpriteSheet

class Tile:
    """
    The Tile class represents a single tile in the game map.

    Attributes:
        x (int): The x-coordinate of the tile.
        y (int): The y-coordinate of the tile.
        value (int): The value of the tile.
        empty (bool): Flag indicating if the tile is empty.
        collision (bool): Flag indicating if the tile has collision.
        tile_size (int): The size of the tile.
        image (pygame.Surface): The image to draw on the tile.

    """

    def __init__(self, x, y, value, tile_size, image=None):
        """
        Initialize a Tile object.

        Args:
            x (int): The x-coordinate of the tile.
            y (int): The y-coordinate of the tile.
            value (int): The value of the tile.
            tile_size (int): The size of the tile.
            image (pygame.Surface, optional): The image to draw on the tile.

        """
        self.x = x
        self.y = y
        self.value = value
        self.empty = value == 1  # If value == 1: empty = 1, else empty = 0
        self.collision = value != 0  # If value == 0: collision = 0, else collision = 1
        self.tile_size = tile_size
        self.image = image

    def draw(self, surface):
        """
        Draw the tile on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the tile on.

        """
        if self.image is not None:
            # Draw the image on the tile
            surface.blit(self.image, (self.x * self.tile_size, self.y * self.tile_size))
        else:
            # Determine the tile color based on its value
            tile_color = pygame.Color("white")  # Default color if no image

            if self.value == -2:  # Ultimate wall
                tile_color = pygame.Color("black")
            elif self.value == -1:  # Wall
                tile_color = pygame.Color("gray")
            elif self.value == 0:  # Door
                tile_color = pygame.Color("brown")
            elif self.value == 1:  # Empty
                tile_color = pygame.Color("white")
            elif self.value == 2:  # Rock
                tile_color = pygame.Color("gray")
            # Add more conditions for different values if needed

            # Draw the tile with the color
            tile_rect = pygame.Rect(self.x * self.tile_size, self.y * self.tile_size, self.tile_size, self.tile_size)
            pygame.draw.rect(surface, tile_color, tile_rect)



class TileMap:
    """
    The TileMap class represents a map made up of tiles.

    Attributes:
        width (int): The width of the tile map.
        height (int): The height of the tile map.
        tile_map (list): The 2D list representing the tile map.

    """

    def __init__(self, map_data, tile_size):
        """
        Initialize a TileMap object.

        Args:
            map_data (list): The map data as a 2D list.
            tile_size (int): The size of each tile.

        """
        self.width = 0
        self.height = 0
        self.tile_map = []

        # Create a SpriteSheet object to load images
        sprite_sheet = SpriteSheet(pygame.image.load("assets/images/tile_sprite.png"))

        for y, row in enumerate(map_data):
            tile_row = []
            for x, value in enumerate(row):
                # Get the image for the tile based on its value
                value = int(value)
                image = sprite_sheet.get_image(value+2, tile_size, tile_size, 1, (1, 0, 0))

                # Create the tile with the image
                tile = Tile(x, y, int(value), tile_size, image)
                tile_row.append(tile)
                self.width += 1
            self.tile_map.append(tile_row)
            self.height += 1

    def draw(self, surface):
        """
        Draw the tile map on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the tile map on.

        """
        for row in self.tile_map:
            for tile in row:
                tile.draw(surface)
