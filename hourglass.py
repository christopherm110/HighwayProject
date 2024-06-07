import pygame
import random


class Hourglass:

    def __init__(self):
        self.x = 542
        self.y = -100
        self.temp_delta1 = 0
        self.temp_delta2 = 0
        self.temp_delta4 = 0
        self.temp_bg_delta = 0
        self.lane_rng = random.randint(1, 3)
        self.spawn_time = random.randint(5, 30)
        self.enabled = False
        self.obtained = False
        self.spawned = False
        self.delta = 3
        self.duration = -1
        self.remaining_uses = 0
        self.image = pygame.image.load("hourglass.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def movement(self):
        self.y = self.y + self.delta
        if self.y > 754:
            self.y = -34
            self.update_lane()
            self.spawned = False
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def check_collisions(self, other_car):
        if pygame.Rect.colliderect(self.rect, other_car.rect):
            self.y = -34
            self.update_lane()
            self.obtained = True
            self.spawned = False
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def new_spawn_time(self, current):
        self.spawn_time = current + random.randint(20, 30)

    def update_lane(self):
        if self.lane_rng == 1:
            self.x = 447
        if self.lane_rng == 2:
            self.x = 542
        if self.lane_rng == 3:
            self.x = 637

    def restart(self):
        self.x = 542
        self.y = -34
        self.temp_delta1 = 0
        self.temp_delta2 = 0
        self.temp_delta4 = 0
        self.temp_bg_delta = 0
        self.lane_rng = random.randint(1, 3)
        self.spawn_time = random.randint(5, 30)
        self.enabled = False
        self.obtained = False
        self.spawned = False
        self.delta = 3
        self.duration = -1
        self.remaining_uses = 0
        self.image = pygame.image.load("hourglass.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])