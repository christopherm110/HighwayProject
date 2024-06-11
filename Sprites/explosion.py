import pygame


class Explosion:

    def __init__(self):
        self.x = -1000
        self.y = 0
        self.image = pygame.image.load("Assets/explosion.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def restart(self):
        self.x = -1000
        self.y = 0
        self.image = pygame.image.load("Assets/explosion.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
