import pygame
import random


class Traffic:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("blue_car.png")
        self.image_size = self.image.get_size()
        # scale_size = (self.image_size[0] * .1, self.image_size[1] * .1)
        # self.image = pygame.transform.scale(self.image, scale_size)
        # self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 2

    def move_direction(self, direction):
        if direction == "up":
            self.y = self.y - self.delta
        if direction == "down":
            self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def traffic_movement(self):
        self.move_direction("up")
        if self.y < -128:
            self.y = random.randint(828, 1000)
            self.delta += 0.1
