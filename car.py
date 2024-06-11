import pygame


class Car:

    def __init__(self):
        self.x = 535
        self.y = 500
        self.image = pygame.image.load("Assets/f1.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.lives = 1
        self.lost_life = False
        self.collided = False
        self.points = 0
        self.milestone = 10
        self.down_scroll_vel = 2
        self.up_vel = 2.5
        self.down_vel = 3
        self.exploded = False
        self.milestone_reached = False
        self.lane = "middle"

    def move_direction(self, direction):
        if direction == "up":
            self.y = self.y - self.up_vel
        if direction == "down":
            self.y = self.y + self.down_vel
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

        if self.y >= 592:
            self.down_vel = 0

        if self.y <= 0:
            self.up_vel = 0

        if 0 < self.y < 592:
            self.up_vel = 2.5
            self.down_vel = 3

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def update_car(self, car):
        self.image = pygame.image.load(car)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def restart(self):
        self.x = 535
        self.y = 500
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.lives = 1
        self.collided = False
        self.points = 0
        self.milestone = 10
        self.down_scroll_vel = 2
        self.up_vel = 2.5
        self.down_vel = 3
        self.exploded = False
        self.milestone_reached = False
        self.lane = "middle"
