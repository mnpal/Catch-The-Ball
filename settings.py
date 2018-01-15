from random import randint

class Settings():
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = 102, 120, 150

        self.ball_missing_limit = 3
        self.ball_direction = randint(-1, 1)

        self.speedup_scale = 1.05
        self.score_points = 2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.base_speed_factor = 1
        self.ball_speed_factor = 1
        self.ball_speed_x = 1

    def increase_speed(self):
        self.base_speed_factor *= self.speedup_scale
        self.ball_speed_factor *= self.speedup_scale
        self.ball_speed_x *= self.speedup_scale
