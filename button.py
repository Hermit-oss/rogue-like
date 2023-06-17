import pygame

class Button():
    def __init__(self, image, x, y, text_input, font, base_color, hovering_color, scale):
        self.clicked=False
        self.x=x
        self.y=y

        self.color=base_color
        self.base_color=base_color
        self.hovering_color=hovering_color


        self.image=image
        if image!=None:
            width = image.get_width()
            height = image.get_height()
            self.image=pygame.transform.scale(image, (int(width*scale), int(height*scale)))

        else:
            self.font=font
            self.text_input=text_input
            self.text = self.font.render(self.text_input, True, self.base_color)

        if self.image is None:
            self.image=self.text
            self.text_rect = self.text.get_rect(center=(self.x, self.y))

        self.rect = self.image.get_rect(center=(self.x, self.y))


    def update(self, screen):
    # If there is an image, blit it to the screen
        if self.image != None:
            screen.blit(self.image, self.rect)
    # Blit the text to the screen
        else:
            screen.blit(self.text, self.text_rect)


    def interaction(self, pos):
        action=False
#       pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if self.image==None:
                self.color=self.hovering_color
                self.text = self.font.render(self.text_input, True, self.hovering_color)
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == False:
                self.clicked = False
        else:
            if self.image==None:
                self.color = self.base_color
                self.text = self.font.render(self.text_input, True, self.hovering_color)
            
        return action
