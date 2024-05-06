import pygame
import random
import time
from mario import Mario
from red import Red
from coin import Coin
from bomb import Bomb
from luigi import Luigi
from background import Background

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Coin Collector!")

# set up variables for the display
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 530
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

points_p1 = 0
points_p2 = 0
hs = open("high_scores", "r")
high_score = hs.readline().strip()
high_score_set = False
if high_score != "":
    high_score_set = True
name = "Collect coins as fast as you can!"
p1_points_msg = "Player 1 Points: " + str(points_p1)
p2_points_msg = "Player 2 Points: " + str(points_p2)
game_over_msg = "Game Over!"
tutorial_1 = "Use WASD or arrow keys to move"
tutorial_2 = "You have 10 seconds to collect as many coins as possible"
tutorial_3 = "Click anywhere on the screen to begin"
high_score_message = "High score: " + str(high_score)
game_start = False
game_over = False
coin_hit = False
red_spawned = False
bomb_spawned = False
red_duration = 0
r = 50
g = 0
b = 100
direction = random.randint(1, 4)
red_spawn_time = random.randint(1, 9)
bomb_spawn_time = random.randint(1, 9)
current_time = 0
time_remaining = 10
start_time = 0

# render the text for later
display_name = my_font.render(name, True, (255, 255, 255))
display_p1_message = my_font.render(p1_points_msg, True, (255, 255, 255))
display_p2_message = my_font.render(p2_points_msg, True, (255, 255, 255))
display_high_score = my_font.render(high_score_message, True, (255, 255, 255))
display_game_over = my_font.render(game_over_msg, True, (255, 255, 255))
display_time = my_font.render("Time remaining: " + str(10) + "s", True, (255, 255, 255))
display_tut_1 = my_font.render(tutorial_1, True, (255, 255, 255))
display_tut_2 = my_font.render(tutorial_2, True, (255, 255, 255))
display_tut_3 = my_font.render(tutorial_3, True, (255, 255, 255))

c = Coin(240, 300)
red = Red(1000, 1000)
bomb = Bomb(1000, 1000)
p1 = Mario(140, 60)
p2 = Luigi(340, 60)
bg = Background(0, 0)
# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:
    if not game_start:
        start_time = time.time()
    if game_start:
        current_time = time.time()

        if not game_over:
            time_remaining = round(10 + start_time - current_time, 2)
            keys = pygame.key.get_pressed()  # checking pressed keys
            if keys[pygame.K_d]:
                p1.move_direction("right")
            if keys[pygame.K_s]:
                p1.move_direction("down")
            if keys[pygame.K_a]:
                p1.move_direction("left")
            if keys[pygame.K_w]:
                p1.move_direction("up")

            if keys[pygame.K_RIGHT]:
                p2.move_direction("right")
            if keys[pygame.K_DOWN]:
                p2.move_direction("down")
            if keys[pygame.K_LEFT]:
                p2.move_direction("left")
            if keys[pygame.K_UP]:
                p2.move_direction("up")

            display_time = my_font.render("Time remaining: " + str(time_remaining) + "s", True, (255, 255, 255))

            if bomb_spawned:
                bomb.move_direction(direction)
                if bomb.x > 500:
                    direction = 2
                    bomb.set_location(49, bomb.y)
                    bomb.times_hit_limit = bomb.times_hit_limit + 1
                if bomb.x < 0:
                    direction = 1
                    bomb.set_location(1, bomb.y)
                    bomb.times_hit_limit = bomb.times_hit_limit + 1
                if bomb.y > 340:
                    direction = 3
                    bomb.set_location(bomb.x, 339)
                    bomb.times_hit_limit = bomb.times_hit_limit + 1
                if bomb.y < 0:
                    direction = 4
                    bomb.set_location(bomb.x, 1)
                    bomb.times_hit_limit = bomb.times_hit_limit + 1
            if bomb.times_hit_limit == 2:
                bomb_spawned = False
                direction = 0
                bomb.set_location(1000, 1000)

            # collision
            if p1.rect.colliderect(c.rect):
                points_p1 = points_p1 + 10
                p1_points_msg = "Player 1 Points: " + str(points_p1)
                display_p1_message = my_font.render(p1_points_msg, True, (255, 255, 255))
                coin_hit = True
            if p1.rect.colliderect(red.rect):
                points_p1 = points_p1 + 20
                p1_points_msg = "Player 1 Points: " + str(points_p1)
                display_p1_message = my_font.render(p1_points_msg, True, (255, 255, 255))
                red_spawned = False
            if p1.rect.colliderect(bomb.rect):
                points_p1 = points_p1 - 20
                p1_points_msg = "Player 1 Points: " + str(points_p1)
                display_p1_message = my_font.render(p1_points_msg, True, (255, 255, 255))
                bomb_spawned = False
            if p2.rect.colliderect(c.rect):
                points_p2 = points_p2 + 10
                p2_points_msg = "Player 2 Points: " + str(points_p2)
                display_p2_message = my_font.render(p2_points_msg, True, (255, 255, 255))
                coin_hit = True
            if p2.rect.colliderect(red.rect):
                points_p2 = points_p2 + 20
                p2_points_msg = "Player 2 Points: " + str(points_p2)
                display_p2_message = my_font.render(p2_points_msg, True, (255, 255, 255))
                red_spawned = False
            if p2.rect.colliderect(bomb.rect):
                points_p2 = points_p2 - 20
                p2_points_msg = "Player 2 Points: " + str(points_p2)
                display_p2_message = my_font.render(p2_points_msg, True, (255, 255, 255))
                bomb_spawned = False
            if coin_hit:
                coin_hit = False
                c.x = random.randint(20, 510)
                c.y = random.randint(20, 350)
                c.set_location(c.x, c.y)

            if time_remaining == red_spawn_time:
                red_spawned = True
                red.x = random.randint(0, 430)
                red.y = random.randint(0, 270)
                red_duration = random.randint(1, red_spawn_time)
                red.set_location(red.x, red.y)
                red_spawn_time = -1
            if time_remaining == bomb_spawn_time:
                bomb_spawned = True
                bomb.x = random.randint(40, 460)
                bomb.y = random.randint(40, 300)
                bomb_duration = random.randint(1, bomb_spawn_time)
                bomb.set_location(bomb.x, bomb.y)
                bomb_spawn_time = -1
            if not red_spawned:
                red.set_location(1000, 1000)
            if not bomb_spawned:
                bomb.set_location(1000, 1000)
            if time_remaining == red_duration:
                red_spawned = False

            if time_remaining <= 0 or points_p1 < 0 or points_p2 < 0:
                game_over = True

            if game_over:
                if not high_score_set:
                    hs = open("high_scores", "w")
                    hs.write(str(points_p1))
                elif high_score_set:
                    if points_p1 > points_p2:
                        if points_p1 > int(high_score) or not high_score_set:
                            hs = open("high_scores", "w")
                            hs.write(str(points_p1))
                            high_score_message = "High score: " + str(points_p1) + " (NEW HIGH SCORE!)"
                    if points_p1 < points_p2:
                        if points_p2 > int(high_score) or not high_score_set:
                            hs = open("high_scores", "w")
                            hs.write(str(points_p2))
                            high_score_message = "High score: " + str(points_p2) + " (NEW HIGH SCORE!)"
                    if points_p1 == points_p2:
                        if points_p2 > int(high_score) or not high_score_set:
                            hs = open("high_scores", "w")
                            hs.write(str(points_p1))
                            high_score_message = "High score: " + str(points_p1) + " (NEW HIGH SCORE!)"
                display_high_score = my_font.render(high_score_message, True, (255, 255, 255))


    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_start = True
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
    screen.fill((231, 95, 19))
    screen.blit(bg.image, bg.rect)
    screen.blit(bomb.image, bomb.rect)
    screen.blit(c.image, c.rect)
    screen.blit(p1.image, p1.rect)
    screen.blit(p2.image, p2.rect)
    if not game_start:
        screen.blit(display_tut_1, (100, 150))
        screen.blit(display_tut_2, (100, 165))
        screen.blit(display_tut_3, (100, 180))
    elif game_start:
        screen.blit(display_name, (0, 0))
        screen.blit(display_p1_message, (0, 15))
        screen.blit(display_p2_message, (0, 30))
        screen.blit(display_time, (0, 45))
        screen.blit(display_high_score, (0, 60))

    if game_over:
        if points_p1 > points_p2 or points_p2 < 0:
            game_over_msg = "GAME OVER! PLAYER 1 WINS!"
        if points_p2 > points_p1 or points_p1 < 0:
            game_over_msg = "GAME OVER! PLAYER 2 WINS!"
        if points_p2 == points_p1:
            game_over_msg = "GAME OVER! DRAW!"
        display_game_over = my_font.render(game_over_msg, True, (255, 255, 255))
        screen.blit(display_game_over, (180, 100))
    if red_spawned:
        screen.blit(red.image, red.rect)
    if bomb_spawned:
        screen.blit(bomb.image, bomb.rect)
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
