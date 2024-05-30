import pygame


class Menu:

    def __init__(self):

        # Controls
        self.con_x = 90
        self.con_y = 180
        self.controls = pygame.image.load("controls.png")
        self.controls_size = self.controls.get_size()
        self.controls_rect = pygame.Rect(90, 180, self.controls_size[0], self.controls_size[1])

        # Stats
        self.stats_x = 2
        self.stats_y = 2
        self.stats = pygame.image.load("stats.png")
        self.stats_size = self.stats.get_size()
        self.stats_rect = pygame.Rect(2, 2, self.stats_size[0], self.stats_size[1])



