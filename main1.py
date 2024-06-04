import pygame
import time
from car import Car
from background import Background
from explosion import Explosion
from ghost import Ghost
from hourglass import Hourglass
from highscore import Highscore
from menu import Menu
from traffic import Traffic

# Initializing Pygame
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Bahnschrift', 20)
pygame.display.set_caption("Final Project Demo")
clock = pygame.time.Clock()

fps = 144

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1080
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

# Initializing Classes
c = Car()
bg = Background()
ex = Explosion()
menu = Menu()
g = Ghost()
h = Hourglass()
classes = [c, bg, ex, menu, g, h]

# Sprite Groups & Initializing Traffic
traffic_group = pygame.sprite.Group()

t1 = Traffic(0, -1040, "left")
traffic_group.add(t1)

t2 = Traffic(0, -360, "middle")
traffic_group.add(t2)

t3 = Traffic(0, -720, "right")
traffic_group.add(t3)

traffic_cars = [t1, t2, t3]

# Initializing High Score
hs = Highscore(0)
hs_set = hs.high_score_set

# Time
time_elapsed = 0
current_time = 0
time_remaining = 3
start_time = 0
total_pause_time = 0
pause_time = -1
total_time = 0
time_at_unpause = 0

# Messagesd
milestone_message = round((c.milestone - 10) / 10)
time_until_pause = round(pause_time - time_elapsed)
pause_message = "Pausing in... " + str(time_until_pause)
high_score_message = str(hs.high_score)
hide_controls_message = "Press 'H' to hide controls"
credit_message = "Art, coding, by Christopher Meregildo"

display_points = my_font.render(str(c.points), True, (255, 255, 255))
display_time = my_font.render(str(time_elapsed) + "s", True, (255, 255, 255))
display_milestone = my_font.render(str(milestone_message), True, (255, 255, 255))
display_pause_time = my_font.render(pause_message, True, (255, 255, 255))
display_high_score = my_font.render(high_score_message, True, (255, 255, 255))
display_hide_controls = my_font.render(hide_controls_message, True, (255, 255, 255))
display_credits = my_font.render(credit_message, True, (255, 255, 255))

# Function to randomize & centers traffic and powerups on a lane
t1.randomize_car()
t2.randomize_car()
t3.randomize_car()
g.update_lane()
h.update_lane()

game_running = False
game_paused = False
show_pause = False
run = True

while run:

    # Updates Messages
    time_until_pause = round(pause_time - time_elapsed)
    pause_message = "Pausing in... " + str(time_until_pause)
    display_pause_time = my_font.render(pause_message, True, (255, 255, 255))
    display_high_score = my_font.render(high_score_message, True, (255, 255, 255))

    # Key Inputs
    keys = pygame.key.get_pressed()

    # Vertical Movement
    if not game_paused:
        if keys[pygame.K_w] and not c.exploded:
            c.move_direction("up")
        if keys[pygame.K_s] and not c.exploded:
            c.move_direction("down")

    if game_running:

        # Time
        current_time = time.time()
        time_elapsed = round(current_time - start_time + time_at_unpause, 1)
        total_time = round(time_elapsed - total_pause_time, 1)
        display_time = my_font.render(str(time_elapsed) + "s", True, (255, 255, 255))

        # Pausing
        if time_elapsed == pause_time:
            game_paused = not game_paused
        if game_paused:
            start_time = time.time()
            time_at_unpause = time_elapsed

        if not game_paused:
            if time_elapsed == pause_time:
                game_paused = True

            # Milestone Mechanic
            if time_elapsed >= c.milestone:
                c.milestone_reached = True
            if c.milestone_reached:
                c.milestone_reached = False
                c.milestone = c.milestone + 10
                milestone_message = round((c.milestone - 10) / 10)
                c.points = c.points + 50
                for cars in traffic_cars:
                    cars.delta = cars.delta + 0.5
            display_milestone = my_font.render(str(milestone_message), True, (255, 255, 255))

            # Point System
            for car in traffic_cars:
                if car.detect_off_screen():
                    car.randomize_car()
                    c.points = c.points + 10
            display_points = my_font.render(str(c.points), True, (255, 255, 255))

            # Traffic Movement
            if not c.exploded:
                t1.traffic_movement()
                t2.traffic_movement()
                t3.traffic_movement()
                if menu.bg_scroll_enabled:
                    bg.down_scroll()

                # Power-ups
                power_ups = [h, g]

                for power_up in power_ups:
                    power_up.check_collisions(c)
                    if time_elapsed == power_up.spawn_time:
                        power_up.spawned = True
                        power_up.new_spawn_time(time_elapsed)

                    if power_up.spawned:
                        power_up.movement()

                # Hourglass Powerup
                if h.obtained:
                    h.remaining_uses = g.remaining_uses + 1
                    h.obtained = False

                if h.enabled:
                    pygame.Surface.set_alpha(menu.hourglass_icon, 255)
                    t1.delta = 1
                    t2.delta = 1
                    t3.delta = 1
                    bg.delta = 1

                if not h.enabled:
                    pygame.Surface.set_alpha(menu.hourglass_icon, 125)

                if time_elapsed == h.duration:
                    t1.delta = h.temp_delta1
                    t2.delta = h.temp_delta2
                    t3.delta = h.temp_delta4
                    bg.delta = 2
                    h.enabled = False

                # Ghost Mode Powerup
                if g.obtained:
                    g.remaining_uses = g.remaining_uses + 1
                    g.obtained = False

                if g.remaining_uses < 0:
                    g.remaining_uses = 0

                if g.enabled:
                    pygame.Surface.set_alpha(c.image, 75)
                    pygame.Surface.set_alpha(menu.ghost_icon, 255)
                if not g.enabled:
                    pygame.Surface.set_alpha(c.image, 255)
                    pygame.Surface.set_alpha(menu.ghost_icon, 125)
                    # Collisions
                    for car in traffic_cars:
                        if pygame.Rect.colliderect(c.rect, car.rect):
                            c.collided = True
                            if c.lives < 1:
                                c.exploded = True
                        if c.collided:
                            g.duration = time_elapsed + 1.5
                            g.enabled = True
                            c.collided = False
                            c.lost_life = True
                            c.lives = c.lives - 1
                            car.y = 721

                if c.lives < 0:
                    c.lives = 0

                if time_elapsed == g.duration:
                    g.enabled = False
                    c.lost_life = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Horizontal Player Movement
        if event.type == pygame.KEYDOWN:
            if not c.exploded:
                # H Key
                if event.key == 104:
                    menu.show_tutorial = not menu.show_tutorial
                if not game_paused:
                    # A key
                    if event.key == 97:
                        c.move_direction("left")
                    # D key
                    if event.key == 100:
                        c.move_direction("right")
                # Q Key
                if event.key == 113 and g.remaining_uses > 0:
                    g.remaining_uses = g.remaining_uses - 1
                    g.duration = time_elapsed + 3
                    g.enabled = True
                # E Key
                if event.key == 101 and h.remaining_uses > 0:
                    h.remaining_uses = h.remaining_uses - 1
                    h.duration = time_elapsed + 3
                    h.temp_delta1 = t1.delta
                    h.temp_delta2 = t2.delta
                    h.temp_delta4 = t3.delta
                    h.enabled = True

                # Space bar
                if event.key == 32 and not game_running:
                    start_time = time.time()
                    game_running = True
                # Esc key
                if event.key == 27 and game_running and not show_pause:
                    if not game_paused:
                        pause_time = time_elapsed + 3
                        show_pause = True
                    if game_paused:
                        game_paused = False
            # Game Restart
            if c.exploded and event.key == 32:
                menu.game_restart = True

        if menu.game_restart:
            for obj in classes:
                obj.restart()

            t1.y = -1040
            t2.y = -360
            t3.y = -720

            # Initializing High Score
            hs = Highscore(0)
            hs_set = hs.high_score_set

            # Time
            time_elapsed = 0
            current_time = 0
            time_remaining = 3
            start_time = 0
            total_pause_time = 0
            pause_time = -1
            total_time = 0
            time_at_unpause = 0

            # Messages
            milestone_message = round((c.milestone - 10) / 10)
            time_until_pause = round(pause_time - time_elapsed)
            pause_message = "Pausing in... " + str(time_until_pause)
            high_score_message = str(hs.high_score)

            display_points = my_font.render(str(c.points), True, (255, 255, 255))
            display_time = my_font.render(str(time_elapsed) + "s", True, (255, 255, 255))
            display_milestone = my_font.render(str(milestone_message), True, (255, 255, 255))
            display_pause_time = my_font.render(pause_message, True, (255, 255, 255))
            display_high_score = my_font.render(high_score_message, True, (255, 255, 255))

            # Function to randomize & centers traffic and powerups on a lane
            t1.randomize_car()
            t2.randomize_car()
            t3.randomize_car()
            g.update_lane()
            h.update_lane()

            game_running = False
            game_paused = False
            show_pause = False

        if event.type == pygame.MOUSEBUTTONUP:
            # Disables background scroll
            if menu.bg_button_rect.collidepoint(event.pos):
                menu.disable_bg_scroll()
            # Restarts the game at any time
            if menu.restart_rect.collidepoint(event.pos):
                menu.game_restart = True

    # Game Over
    if c.exploded:
        game_running = False
        hs = Highscore(c.points)
        ex.move(c.x - 135, c.y - 90)

    # High Score
    hs = Highscore(c.points)
    hs.check_for_hs()
    hs_broken = hs.new_high_score

    screen.fill((106, 190, 48))
    screen.blit(bg.image, bg.rect)
    screen.blit(c.image, c.rect)
    screen.blit(menu.stats, menu.stats_rect)

    if menu.show_tutorial:
        screen.blit(menu.controls, menu.controls_rect)
        screen.blit(display_hide_controls, (2, 679))

    screen.blit(display_credits, (2, 699))
    screen.blit(display_points, (149, 9))
    screen.blit(display_time, (100, 43))
    screen.blit(display_milestone, (196, 77))
    screen.blit(display_high_score, (196, 111))

    if time_until_pause == 0:
        show_pause = False

        screen.blit(menu.return_to_menu, menu.return_to_menu_rect)
        screen.blit(menu.bg_button, menu.bg_button_rect)
        screen.blit(menu.bg_scroll, menu.bg_scroll_rect)
        screen.blit(menu.restart_img, menu.restart_rect)

    if h.remaining_uses > 0 or h.enabled:
        screen.blit(menu.hourglass_icon, menu.hourglass_icon_rect)
        screen.blit(menu.e_button, menu.e_button_rect)
    if g.remaining_uses > 0 or (g.enabled and not c.lost_life):
        screen.blit(menu.ghost_icon, menu.ghost_icon_rect)
        screen.blit(menu.q_button, menu.q_button_rect)

    if show_pause:
        screen.blit(display_pause_time, (500, 10))

    screen.blit(t1.image, t1.rect)
    screen.blit(t2.image, t2.rect)
    screen.blit(t3.image, t3.rect)
    screen.blit(g.image, g.rect)
    screen.blit(h.image, h.rect)
    screen.blit(c.image, c.rect)
    screen.blit(ex.image, ex.rect)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
