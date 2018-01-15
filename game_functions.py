import sys
import pygame
from ball import Ball
from base import Base
from random import randint
from time import sleep

def check_keydown_events(event, base, stats):
    if event.key == pygame.K_q:
        update_high_score(stats)
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        base.moving_right = True
    elif event.key == pygame.K_LEFT:
        base.moving_left = True

def check_keyup_events(event, base):
    if event.key == pygame.K_RIGHT:
        base.moving_right = False
    if event.key == pygame.K_LEFT:
        base.moving_left = False

def check_events(catch_settings, screen, stats, sb, play_button, base, balls):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            update_high_score(stats)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, base, stats)
            if event.key == pygame.K_p:
                catch_settings.initialize_dynamic_settings()
                start_game(catch_settings, screen, stats, sb, base, balls)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, base)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(catch_settings, screen, stats, sb, play_button, base, balls, mouse_x, mouse_y)

def update_high_score(stats):
    file = open("highest_score.txt", "w")
    file.write(str(stats.high_score))
    file.close()

def start_game(catch_settings, screen, stats, sb, base, balls):
    pygame.mouse.set_visible(False)
    stats.reset_stats()
    sb.prep_score()
    sb.prep_high_score()
    stats.game_active = True
    balls.empty()
    create_balls(catch_settings, screen, balls)
    base.center_base()

def check_play_button(catch_settings, screen, stats, sb, play_button, base, balls, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        catch_settings.initialize_dynamic_settings()
        start_game(catch_settings, screen, stats, sb, base, balls)

def create_balls(catch_settings, screen, balls):
    ball = Ball(catch_settings, screen)
    ball.rect.x = randint(ball.rect.width, ball.catch_settings.screen_width-ball.rect.width)
    ball.rect.y = ball.rect.height
    #ball.rect.x = ball.rect.width

    balls.add(ball)

def check_ball_edges(catch_settings, balls):
    if catch_settings.ball_direction == 0:
        catch_settings.ball_direction = 1
    for ball in balls.sprites():
        if ball.check_edges():
            catch_settings.ball_direction *= -1
            break

def update_base(base):
    base.update()

def ball_missed(catch_settings, stats, screen, base, balls):
    if stats.ball_missed > 0:
        stats.ball_missed -= 1
        balls.empty()
        create_balls(catch_settings, screen, balls)
        base.center_base()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def update_balls(catch_settings, stats, screen, sb, base, balls):
    check_ball_edges(catch_settings, balls)
    balls.update()
    for ball in balls.copy():
        if ball.rect.bottom > catch_settings.screen_height:
            #balls.remove(ball)
            ball_missed(catch_settings, stats, screen, base, balls)

    if pygame.sprite.spritecollideany(base, balls):
        balls.empty()
        stats.score += catch_settings.score_points
        sb.prep_score()
        check_high_score(stats, sb)
        #print("Collected")
    # collisions = pygame.sprite.groupcollide(balls, base, True, False)
    if len(balls) == 0:
        catch_settings.increase_speed()
        create_balls(catch_settings, screen, balls)

def update_screen(catch_settings, screen, stats, sb, base, balls, play_button):
    screen.fill(catch_settings.bg_color)
    base.blitme()
    balls.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
