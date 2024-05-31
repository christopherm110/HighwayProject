import pygame
import random


class Test(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.delta = 3.5
        self.points_given = False
        self.traffic_list = ["blue_car.png", "gray_van.png", "green_truck.png", "white_cargo_truck.png",
                             "yellow_coupe.png"]
        self.car_rng = random.randint(0, 4)
        self.image = pygame.image.load(self.traffic_list[self.car_rng])
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def lane_center(self, lane):
        # Blue Car
        if self.car_rng == 0:
            if lane == "left":
                self.x = 430
            if lane == "middle":
                self.x = 525
            if lane == "right":
                self.x = 620
        # Gray Van
        if self.car_rng == 1:
            if lane == "left":
                self.x = 425
            if lane == "middle":
                self.x = 520
            if lane == "right":
                self.x = 616
        # Green Truck
        if self.car_rng == 2:
            if lane == "left":
                self.x = 424
            if lane == "middle":
                self.x = 518
            if lane == "right":
                self.x = 615
        # White Cargo Truck
        if self.car_rng == 3:
            if lane == "left":
                self.x = 427
            if lane == "middle":
                self.x = 521
            if lane == "right":
                self.x = 618
        # Yellow Coupe
        if self.car_rng == 4:
            if lane == "left":
                self.x = 430
            if lane == "middle":
                self.x = 527
            if lane == "right":
                self.x = 624
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move_direction(self, direction):
        if direction == "up":
            self.y = self.y - self.delta
        if direction == "down":
            self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def traffic_movement(self):
        self.move_direction("down")
        if self.y > 1208:
            self.y = random.randint(-500, -128)
            random_speed = random.randint(-5, 5)
            speed = random_speed / 10
            self.delta = self.delta + speed
            if self.delta < 2:
                self.delta = 2

    def detect_off_screen(self):
        if self.y > 720 and not self.points_given:
            self.points_given = True
            self.car_rng = random.randint(0, 4)
            self.image = pygame.image.load(self.traffic_list[self.car_rng])
            return True
        if 0 < self.y < 720 and self.points_given:
            self.points_given = False
            return False