import sys
import pygame
from settings import Settings
from base import Base
from ball import Ball
from pygame.sprite import Group
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    catch_settings = Settings()
    screen = pygame.display.set_mode((catch_settings.screen_width, catch_settings.screen_height))
    pygame.display.set_caption("Catch The Ball")

    play_button = Button(catch_settings, screen, "Start")
    stats = GameStats(catch_settings)
    sb = Scoreboard(catch_settings, screen, stats)
    base = Base(catch_settings, screen)
    balls = Group()
    gf.create_balls(catch_settings, screen, balls)

    while True:
        gf.check_events(catch_settings, screen, stats, sb, play_button, base, balls)
        if stats.game_active:
            gf.update_base(base)
            gf.update_balls(catch_settings, stats, screen, sb, base, balls)
        gf.update_screen(catch_settings, screen, stats, sb, base, balls, play_button)

run_game()
