import pygame.font

class Scoreboard():
    def __init__(self, catch_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.catch_settings = catch_settings
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 30)

        self.prep_score()
        self.prep_high_score()

    def prep_high_score(self):
        high_score_str = str(self.stats.high_score)
        self.high_score_image = self.font.render("High Score: " + high_score_str, True, self.text_color, self.catch_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 10

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.catch_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
