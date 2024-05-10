import pygame
import time
# import random
from car import Car
from traffic import Traffic
from traffic2 import Traffic2
from traffic3 import Traffic3
from background import Background
from explosion import Explosion

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Final Project Demo")
clock = pygame.time.Clock()

fps = 144

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1080
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

message = "Points: 0"

c = Car(535, 500)
t = Traffic(430, -1040)
t2 = Traffic2(620, -720)
t3 = Traffic3(525, -360)
bg = Background(280, -360)
ex = Explosion(-1000, 0)

ghost = False
ghost_used = False
exploded = False
game_running = False
collisions = 0
points = 0
time_elapsed = "0s"
current_time = 0
time_remaining = 3
ghost_start_time = 0
ghost_time = 0
ghost_end_time = 0
collided_car = "none"
other_cars = [t, t2, t3]
start_time = 0
total_pause_time = 0
milestone = 10
total_time = 0
time_at_unpause = 0
milestone_reached = False
game_paused = False
milestone_message = round((milestone - 10) / 10)

display_points = my_font.render(message, True, (255, 255, 255))
display_time = my_font.render(time_elapsed, True, (255, 255, 255))
display_milestone = my_font.render("Milestone: " + str(milestone_message), True, (255, 255, 255))

run = True

while run:
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

        if game_paused:
            start_time = time.time()
            time_at_unpause = time_elapsed

        if not game_paused:

            if time_elapsed >= milestone:
                milestone_reached = True

            if milestone_reached:
                milestone_reached = False
                milestone = milestone + 10
                milestone_message = round((milestone - 10) / 10)
                points = points + 50
                for cars in other_cars:
                    cars.delta = cars.delta + 0.5
            display_milestone = my_font.render("Milestone: " + str(milestone_message), True, (255, 255, 255))

            # Point System
            for car in other_cars:
                if car.detect_off_screen():
                    points = points + 10
            display_points = my_font.render("Points: " + str(points), True, (255, 255, 255))

            # Traffic Movement
            if not exploded:
                t.traffic_movement()
                t2.traffic_movement()
                t3.traffic_movement()
                bg.move_direction("down")

            # Vertical Player Movement
            if keys[pygame.K_w] and not exploded:
                c.y_vel = c.y_vel + 2
                c.move_direction("up")
            if keys[pygame.K_s] and not exploded:
                c.y_vel = c.y_vel + 2
                c.move_direction("down")

            # Ghost Mode & Collisions
            if collisions == 1 and not ghost_used:
                ghost = True
                ghost_used = True
                ghost_end_time = time_elapsed + 3
            if collisions == 2:
                exploded = True
                game_running = False
            if ghost:
                pygame.Surface.set_alpha(c.image, 125)
            if not ghost:
                pygame.Surface.set_alpha(c.image, 255)
                # Collisions
                for car in other_cars:
                    if pygame.Rect.colliderect(c.rect, car.rect):
                        collided_car = car
                        collisions = collisions + 1
            if time_elapsed == ghost_end_time:
                ghost = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Horizontal Player Movement
        if event.type == pygame.KEYDOWN and not exploded:
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
            if event.key == 27 and game_running:
                game_paused = not game_paused

    screen.fill((106, 190, 48))
    screen.blit(bg.image, bg.rect)
    screen.blit(display_points, (1, 0))
    screen.blit(display_time, (1, 20))
    screen.blit(display_milestone, (1, 40))
    screen.blit(t.image, t.rect)
    screen.blit(t2.image, t2.rect)
    screen.blit(t3.image, t3.rect)
    screen.blit(c.image, c.rect)
    if exploded:
        if c.y - collided_car.y < 0:
            ex.move(c.x - 80, c.y + 10)
        if c.y - collided_car.y > 0:
            ex.move(c.x - 80, c.y - 80)
        if c.y - collided_car.y == 0:
            ex.move(c.x - 80, c.y - 40)
        screen.blit(ex.image, ex.rect)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
