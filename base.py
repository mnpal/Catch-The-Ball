import pygame
from pygame.sprite import Sprite

class Base(Sprite):
    def __init__(self, catch_settings, screen):
        super().__init__()
        self.screen = screen
        self.catch_settings = catch_settings

        self.image = pygame.image.load('images/minus.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.catch_settings.base_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.catch_settings.base_speed_factor
        self.rect.centerx = self.center

    def center_base(self):
        self.center = self.screen_rect.centerx

    def blitme(self):
        self.screen.blit(self.image, self.rect)
