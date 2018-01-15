import pygame
from pygame.sprite import Sprite
from random import randint

class Ball(Sprite):
    def __init__(self, catch_settings, screen):
        super().__init__()
        self.screen = screen
        self.catch_settings = catch_settings

        self.image = pygame.image.load('images/tennis-ball.png')
        self.rect = self.image.get_rect()

        self.rect.x = randint(self.rect.width, self.catch_settings.screen_width-self.rect.width)
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.rect.y += self.catch_settings.ball_speed_factor
        self.rect.x += self.catch_settings.ball_speed_x*self.catch_settings.ball_direction

    def blitme(self):
        self.screen.blit(self.image, self.rect)
