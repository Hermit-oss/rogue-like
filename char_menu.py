import pygame
from button import Button

def get_font(size): 
    return pygame.font.Font('assets/fonts/yoster.ttf', size)


class Char_menu():
    def __init__(self, surface, mid_x, mid_y):
        width = mid_x * 2
        height = mid_y * 2
        self.chosen = 1
        self.first_x = mid_x - 30
        self.first_y = mid_y - 100
        self.second_x = mid_x - 30 - width / 3
        self.second_y = mid_y - 100
        self.third_x = mid_x - 30 + width / 3
        self.third_y = mid_y - 100
        self.surface = surface
        self.chosen_color = None

        color0 = (0, 0, 0)
        color1 = (0, 255, 0)
        color2 = (0, 0, 255)
        self.choice_color = (150, 150, 150)
        
        pygame.draw.rect(surface, color0, pygame.Rect(self.second_x, self.second_y, 60, 60))
        pygame.draw.rect(surface, color1, pygame.Rect(self.first_x, self.first_y, 60, 60))
        pygame.draw.rect(surface, color2, pygame.Rect(self.third_x, self.third_y, 60, 60))

        pygame.draw.rect(surface, self.choice_color, pygame.Rect(self.first_x - 5, self.first_y - 5, 70, 70), 4)

        self.Left = Button(image=pygame.image.load("assets/images/arrow_left.png"), x=mid_x - 300,
                           y=mid_y + height / 4, text_input=None, font=None, base_color=None, hovering_color=None,
                           scale=3)
        self.Left.update(surface)
        self.Right = Button(image=pygame.image.load("assets/images/arrow_right.png"), x=mid_x + 300,
                            y=mid_y + height / 4, text_input=None, font=None, base_color=None, hovering_color=None,
                            scale=3)
        self.Right.update(surface)

        self.Mid = Button(image=None, x=200, y=200, text_input="", font=get_font(75), base_color="brown4",
                          hovering_color="red", scale=1)
        self.Mid.update(surface)

    def get_chosen_color(self):
        return self.chosen_color

    def change_char(self, pos):
        changed = False
        play = False

        if self.Left.interaction(pos):
            if self.chosen != 0:
                self.chosen -= 1
            else:
                self.chosen = 2
            changed = True
        elif self.Right.interaction(pos):
            if self.chosen != 2:
                self.chosen += 1
            else:
                self.chosen = 0
            changed = True
        elif self.Mid.interaction(pos):
            play = True

        self.show_choice(self.surface)
        
        chosen_color = None
        if self.chosen == 0:
            chosen_color = (0, 0, 0)
        elif self.chosen == 1:
            chosen_color = (0, 255, 0)
        elif self.chosen == 2:
            chosen_color = (0, 0, 255)

        self.chosen_color = chosen_color  # Update the chosen color attribute

        return self.chosen, changed, play, self.chosen_color

    def show_choice(self, surface):
        black = (0, 0, 0)

        if self.chosen == 0:
            pygame.draw.rect(surface, self.choice_color, pygame.Rect(self.second_x - 5, self.second_y - 5, 70, 70), 4)
            pygame.draw.rect(surface, black, pygame.Rect(self.first_x - 5, self.first_y - 5, 70, 70), 4)
            pygame.draw.rect(surface, black, pygame.Rect(self.third_x - 5, self.third_y - 5, 70, 70), 4)
            

        if self.chosen == 1:
            pygame.draw.rect(surface, self.choice_color, pygame.Rect(self.first_x - 5, self.first_y - 5, 70, 70), 4)
            pygame.draw.rect(surface, black, pygame.Rect(self.third_x - 5, self.third_y - 5, 70, 70), 4)
            pygame.draw.rect(surface, black, pygame.Rect(self.second_x - 5, self.second_y - 5, 70, 70), 4)
            

        if self.chosen == 2:
            pygame.draw.rect(surface, self.choice_color, pygame.Rect(self.third_x - 5, self.third_y - 5, 70, 70), 4)
            pygame.draw.rect(surface, black, pygame.Rect(self.second_x - 5, self.second_y - 5, 70, 70), 4)
            pygame.draw.rect(surface, black, pygame.Rect(self.first_x - 5, self.first_y - 5, 70, 70), 4)
            
