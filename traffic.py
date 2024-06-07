import pygame
import random


class Traffic(pygame.sprite.Sprite):
    def __init__(self, x, y, lane):
        super().__init__()
        self.x = x
        self.y = y
        self.lane = lane
        self.delta = 2.75
        self.points_given = False
        self.image = pygame.image.load("blue_car.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move_direction(self, direction):
        if direction == "up":
            self.y = self.y - self.delta
        if direction == "down":
            self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def traffic_movement(self):
        self.move_direction("down")
        if self.y > 730:
            self.y = random.randint(-1000, -128)
            random_speed = random.randint(-5, 5)
            speed = random_speed / 10
            self.delta = self.delta + speed
            if self.delta < 2:
                self.delta = 2
            if self.delta > 5:
                self.delta = 5

    def detect_off_screen(self):
        if self.y > 720 and not self.points_given:
            self.points_given = True
            self.randomize_car()
            return True
        if 0 < self.y < 720 and self.points_given:
            self.points_given = False
            return False

    def randomize_car(self):
        rng = random.randint(1, 75)
        # Blue Car
        if rng <= 20:
            self.image = pygame.image.load("blue_car.png")
            if self.lane == "left":
                self.x = 430
            if self.lane == "middle":
                self.x = 525
            if self.lane == "right":
                self.x = 620
        # Gray Van
        if 20 < rng <= 30:
            self.image = pygame.image.load("gray_van.png")
            if self.lane == "left":
                self.x = 425
            if self.lane == "middle":
                self.x = 520
            if self.lane == "right":
                self.x = 616
        # Green Truck
        if 30 < rng <= 45:
            self.image = pygame.image.load("green_truck.png")
            if self.lane == "left":
                self.x = 424
            if self.lane == "middle":
                self.x = 518
            if self.lane == "right":
                self.x = 615
        # White Cargo Truck
        if 45 < rng <= 55:
            self.image = pygame.image.load("white_cargo_truck.png")
            if self.lane == "left":
                self.x = 427
            if self.lane == "middle":
                self.x = 521
            if self.lane == "right":
                self.x = 618
        # Yellow Coupe
        if 55 < rng <= 75:
            self.image = pygame.image.load("yellow_coupe.png")
            if self.lane == "left":
                self.x = 430
            if self.lane == "middle":
                self.x = 527
            if self.lane == "right":
                self.x = 624

        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def restart(self, x, y, lane):
        self.x = x
        self.y = y
        self.lane = lane
        self.delta = 2.75
        self.points_given = False
        self.image = pygame.image.load("blue_car.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
