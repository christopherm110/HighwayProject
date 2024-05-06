import pygame
import time
import random
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
t = Traffic(430, (random.randint(250, 500)))
t2 = Traffic2(620, -100)
t3 = Traffic3(525, random.randint(0, 250))
bg = Background(280, 0)
ex = Explosion(-1000, 0)

ghost = False
ghost_used = False
exploded = False
collisions = 0
points = 0
time_elapsed = "0s"
current_time = 0
time_remaining = 3
ghost_start_time = 0
ghost_time = 0
collided_car = "none"
start_time = time.time()

display_message = my_font.render(message, True, (255, 255, 255))
display_time = my_font.render(time_elapsed, True, (255, 255, 255))

run = True

while run:
    current_time = time.time()

    time_elapsed = round(current_time - start_time, 1)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and not exploded:
        c.y_vel = c.y_vel + 2
        c.move_direction("up")
    if keys[pygame.K_s] and not exploded:
        c.y_vel = c.y_vel + 2
        c.move_direction("down")

    # Traffic Movement
    if not exploded:
        t.traffic_movement()
        t2.traffic_movement()
        t3.traffic_movement()

    if collisions == 1 and not ghost_used:
        ghost = True
        ghost_used = True

    if collisions == 2:
        exploded = True

    if ghost:
        ghost_start_time = time.time()
        pygame.Surface.set_alpha(c.image, 125)
        ghost_time = round(ghost_start_time - start_time, 1)
        if ghost_time == 3:
            ghost = False

    if not ghost:
        pygame.Surface.set_alpha(c.image, 255)
        # Collisions
        other_cars = [t, t2, t3]
        for car in other_cars:
            if pygame.Rect.colliderect(c.rect, car.rect):
                collided_car = car
                collisions = collisions + 1

    display_time = my_font.render(str(time_elapsed) + "s", True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN and not exploded:
            if event.key == 97:
                c.move_direction("left")
            if event.key == 100:
                c.move_direction("right")

    # bg.move_direction("up")
    # fog.set_alpha(127)
    # screen.blit(fog, (0, 0))
    screen.fill((106, 190, 48))
    screen.blit(bg.image, bg.rect)
    screen.blit(display_message, (1, 0))
    screen.blit(display_time, (1, 20))
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
