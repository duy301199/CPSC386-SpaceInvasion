import pygame.font
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 128, 255)


class Button():
    def __init__(self, screen, msg, ul):
        self.screen = screen

        self.width, self.height = 200, 40
        self.colors = [BLUE, GREEN]
        self.color_idx = 0
        self.color = self.colors[self.color_idx]
        self.color = BLUE
        self.text_color = WHITE
        self.font = pygame.font.SysFont("Segoe UI", 40)
        self.ul = ul

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.left, self.rect.top = ul[0], ul[1]

        self.msg = msg
        self.image = self.font.render(self.msg, True, self.text_color, self.color)
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.rect.center

    def toggle_colors(self): 
        self.color_idx += 1
        self.color_idx %= 2
        self.draw()

    def draw(self):
        color = self.colors[self.color_idx]
        self.image = self.font.render(self.msg, True, self.text_color, color)
        self.screen.fill(color, self.rect)
        self.screen.blit(self.image, self.image_rect)
    