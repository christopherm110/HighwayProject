import pygame


class Car:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("f1.png")
        self.image_size = self.image.get_size()
        # scale_size = (self.image_size[0] * .1, self.image_size[1] * .1)
        # self.image = pygame.transform.scale(self.image, scale_size)
        # self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.lane = "middle"
        self.y_vel = 2

    def move_direction(self, direction):
        if direction == "up":
            self.y_vel = 2
            self.y = self.y - self.y_vel
        if direction == "down":
            self.y_vel = 2
            self.y = self.y + self.y_vel
        if direction == "left" and self.lane == "middle":
            self.lane = "left"
            self.x = 440
        if direction == "left" and self.lane == "right":
            self.lane = "middle"
            self.x = 535
        if direction == "right" and self.lane == "middle":
            self.lane = "right"
            self.x = 630
        if direction == "right" and self.lane == "left":
            self.lane = "middle"
            self.x = 535
        if self.y > 720:
            self.y = -130
        if self.y < -140:
            self.y = 730
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
