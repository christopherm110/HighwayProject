import pygame
import time
from car import Car
from background import Background
from explosion import Explosion
from ghost import Ghost
from hourglass import Hourglass
from high_scores_test import Highscore
from menu import Menu
from traffic import Traffic

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

c = Car(535, 500)
bg = Background(280, -360)
ex = Explosion(-1000, 0)
menu = Menu()
g = Ghost()
h = Hourglass()

# Sprite Groups Test
traffic_group = pygame.sprite.Group()

t1 = Traffic(0, -1040)
traffic_group.add(t1)

t2 = Traffic(0, -360)
traffic_group.add(t2)

t3 = Traffic(0, -720)
traffic_group.add(t3)

t1.lane_center("left")
t2.lane_center("middle")
t3.lane_center("right")
#


exploded = False
game_running = False
time_elapsed = 0
current_time = 0
time_remaining = 3
# other_cars = [t, t2, t3]
other_cars = [t1, t2, t3]
start_time = 0
total_pause_time = 0
pause_time = -1
total_time = 0
time_at_unpause = 0
game_paused = False
show_pause = False
show_tut = True

hs = Highscore(c.points)
hs_set = hs.high_score_set

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
t1.randomize_car("left")
t2.randomize_car("middle")
t3.randomize_car("right")
g.update_lane()
h.update_lane()

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
        if keys[pygame.K_w] and not exploded:
            c.y_vel = c.y_vel + 2
            c.move_direction("up")
        if keys[pygame.K_s] and not exploded:
            c.y_vel = c.y_vel + 2
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
                for cars in other_cars:
                    cars.delta = cars.delta + 0.5
            display_milestone = my_font.render(str(milestone_message), True, (255, 255, 255))

            # Point System
            for car in other_cars:
                if car.detect_off_screen():
                    c.points = c.points + 10
            display_points = my_font.render(str(c.points), True, (255, 255, 255))

            # Traffic Randomizer
            t1.randomize_car("left")
            t2.randomize_car("middle")
            t3.randomize_car("right")

            # Traffic Movement
            if not exploded:
                t1.traffic_movement()
                t2.traffic_movement()
                t3.traffic_movement()
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

            if h.obtained:
                h.activated = True
                h.duration = time_elapsed + 3
                h.traffic1_delta = t1.delta
                h.traffic2_delta = t2.delta
                h.traffic3_delta = t3.delta
                h.obtained = False

            if h.activated:
                t1.delta = 1
                t2.delta = 1
                t3.delta = 1
                bg.delta = 1

            if time_elapsed == h.duration:
                t1.delta = h.traffic1_delta
                t2.delta = h.traffic2_delta
                t3.delta = h.traffic3_delta
                bg.delta = 3
                h.activated = False

            # Ghost Mode & Collisions
            if g.obtained:
                g.remaining_uses = g.remaining_uses + 1
                g.obtained = False

            if g.activated:
                g.remaining_uses = g.remaining_uses - 1
                g.enabled = True
                g.duration = time_elapsed + 3
                g.activated = False

            if g.remaining_uses < 0:
                g.remaining_uses = 0

            if g.enabled:
                pygame.Surface.set_alpha(c.image, 125)
            if not g.enabled:
                pygame.Surface.set_alpha(c.image, 255)
                # Collisions
                for car in other_cars:
                    if pygame.Rect.colliderect(c.rect, car.rect):
                        c.collided_car = car
                        c.collisions = c.collisions + 1
                        if g.remaining_uses >= 1:
                            g.activated = True
                        if g.remaining_uses == 0:
                            exploded = True
                            game_running = False

            if time_elapsed == g.duration:
                g.enabled = False

            # Vertical Player Movement
            if keys[pygame.K_w] and not exploded:
                c.y_vel = c.y_vel + 2
                c.move_direction("up")
            if keys[pygame.K_s] and not exploded:
                c.y_vel = c.y_vel + 2
                c.move_direction("down")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Horizontal Player Movement
        if event.type == pygame.KEYDOWN:
            if not exploded:
                if event.key == 104:
                    show_tut = not show_tut
                if not game_paused:
                    # A key
                    if event.key == 97:
                        c.move_direction("left")
                    # D key
                    if event.key == 100:
                        c.move_direction("right")
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
            # if exploded and event.key == 32:
            #     c = Car(535, 500)
            #     t = Traffic(0, -1040)
            #     t2 = Traffic2(0, -360)
            #     t3 = Traffic3(0, -720)
            #     bg = Background(280, -360)
            #     ex = Explosion(-1000, 0)
            #
            #     t.lane_center("left")
            #     t2.lane_center("middle")
            #     t3.lane_center("right")
            #
            #     ghost = False
            #     ghost_uses = 1
            #     ghost_activated = False
            #     collisions = 0
            #     points = 0
            #     time_elapsed = 0
            #     current_time = 0
            #     time_remaining = 3
            #     collided_car = "none"
            #     other_cars = [t, t2, t3]
            #     start_time = 0
            #     total_pause_time = 0
            #     milestone = 10
            #     pause_time = -1
            #     total_time = 0
            #     time_at_unpause = 0
            #     milestone_reached = False
            #     show_pause = False
            #     show_tut = True
            #
            #     hs = Highscore(points)
            #     hs_set = hs.high_score_set
            #
            #     milestone_message = round((milestone - 10) / 10)
            #     time_until_pause = round(pause_time - time_elapsed)
            #     pause_message = "Pausing in... " + str(time_until_pause)
            #     high_score_message = str(hs.high_score)
            #
            #     game_running = False
            #     game_paused = False
            #     exploded = False

    # Game Over
    if exploded:
        # Shows the fireball
        if c.y - c.collided_car.y < 0:
            ex.move(c.x - 80, c.y + 10)
        if c.y - c.collided_car.y > 0:
            ex.move(c.x - 80, c.y - 80)
        if c.y - c.collided_car.y == 0:
            ex.move(c.x - 80, c.y - 40)

        # High Score
        hs = Highscore(c.points)
        hs.check_for_hs()
        hs_broken = hs.new_high_score

    screen.fill((106, 190, 48))
    screen.blit(bg.image, bg.rect)
    screen.blit(c.image, c.rect)
    screen.blit(menu.stats, menu.stats_rect)

    if show_tut:
        screen.blit(menu.controls, menu.controls_rect)
        screen.blit(display_hide_controls, (2, 679))

    screen.blit(display_credits, (2, 699))
    screen.blit(display_points, (200, 9))
    screen.blit(display_time, (100, 43))
    screen.blit(display_milestone, (200, 78))
    screen.blit(display_high_score, (1, 110))

    if time_until_pause == 0:
        show_pause = False
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
