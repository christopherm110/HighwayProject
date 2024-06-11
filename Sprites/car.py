import pygame


class Car:

    def __init__(self):
        self.x = 527
        self.y = 500
        self.start = 527
        self.lower_limit = 605
        self.image = pygame.image.load("Assets/hellcat.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.name = "Dodge Challenger SRT"
        self.lives = 1
        self.points = 0
        self.milestone = 10
        self.down_scroll_vel = 2
        self.up_vel = 2.5
        self.down_vel = 3
        self.lost_life = False
        self.collided = False
        self.exploded = False
        self.milestone_reached = False
        self.lane = "middle"

    def move_direction(self, direction):
        if direction == "up":
            self.y = self.y - self.up_vel
        if direction == "down":
            self.y = self.y + self.down_vel

        if self.name == "Dodge Challenger SRT":
            if direction == "left" and self.lane == "middle":
                self.lane = "left"
                self.x = 432
            if direction == "left" and self.lane == "right":
                self.lane = "middle"
                self.x = 527
            if direction == "right" and self.lane == "middle":
                self.lane = "right"
                self.x = 625
            if direction == "right" and self.lane == "left":
                self.lane = "middle"
                self.x = 527

        if self.name == "SF21":
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

        if self.name == "Ducati Corse Panigale":
            if direction == "left" and self.lane == "middle":
                self.lane = "left"
                self.x = 452
            if direction == "left" and self.lane == "right":
                self.lane = "middle"
                self.x = 547
            if direction == "right" and self.lane == "middle":
                self.lane = "right"
                self.x = 643
            if direction == "right" and self.lane == "left":
                self.lane = "middle"
                self.x = 547

        if self.y >= self.lower_limit:
            self.down_vel = 0

        if self.y <= 0:
            self.up_vel = 0

        if 0 < self.y < self.lower_limit:
            self.up_vel = 2.5
            self.down_vel = 3

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def update_car(self, car):
        if car == "Assets/sf21.png":
            self.name = "SF21"
            self.start = 535
            self.lower_limit = 529
        if car == "Assets/hellcat.png":
            self.name = "Dodge Challenger SRT"
            self.start = 527
            self.lower_limit = 605
        if car == "Assets/motorcycle.png":
            self.name = "Ducati Corse Panigale"
            self.start = 547
            self.lower_limit = 655
        self.image = pygame.image.load(car)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def restart(self):
        self.x = self.start
        self.y = 500
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.lives = 1
        self.points = 0
        self.milestone = 10
        self.down_scroll_vel = 2
        self.up_vel = 2.5
        self.down_vel = 3
        self.lost_life = False
        self.collided = False
        self.exploded = False
        self.milestone_reached = False
        self.lane = "middle"
