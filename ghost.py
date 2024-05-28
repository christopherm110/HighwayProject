import pygame
import random


class Ghost:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ghost_obtained = False
        self.delta = 3
        self.image = pygame.image.load("ghost.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def movement(self):
        self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def check_collisions(self, other_car):
        if pygame.Rect.colliderect(self.rect, other_car.rect):
            self.y = 1000
            self.ghost_obtained = True

