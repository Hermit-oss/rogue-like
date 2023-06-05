import pygame

class SpriteSheet:
    """
    The SpriteSheet class represents a sprite sheet image containing multiple frames of an animation.

    Attributes:
        sheet (pygame.Surface): The sprite sheet image.

    Methods:
        get_image(frame, width, height, scale, colour): Extracts a specific frame from the sprite sheet and returns
                                                       it as a scaled and color-keyed image.
    """

    def __init__(self, image):
        """
        Initializes a new instance of the SpriteSheet class.

        Parameters:
            image (pygame.Surface): The sprite sheet image to use.
        """
        self.sheet = image

    def get_image(self, frame, width, height, scale, colour):
        """
        Extracts a specific frame from the sprite sheet and returns it as a scaled and color-keyed image.

        Parameters:
            frame (int): The index of the frame to extract.
            width (int): The width of each frame in pixels.
            height (int): The height of each frame in pixels.
            scale (int): The scaling factor to apply to the extracted frame.
            colour (tuple): The color to set as transparent (color key).

        Returns:
            pygame.Surface: The extracted frame as a scaled and color-keyed image.
        """
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)

        return image
