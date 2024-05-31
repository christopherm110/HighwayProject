import pygame
import random


class Ghost:

    def __init__(self):
        self.x = 535
        self.y = -34
        self.lane_rng = random.randint(1, 3)
        self.spawn_time = random.randint(5, 30)
        self.enabled = False
        self.activated = False
        self.obtained = False
        self.spawned = False
        self.delta = 3
        self.duration = -1
        self.remaining_uses = 1
        self.image = pygame.image.load("ghost.png")
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
            self.x = 445
        if self.lane_rng == 2:
            self.x = 540
        if self.lane_rng == 3:
            self.x = 635
