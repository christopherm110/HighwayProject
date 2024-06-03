import pygame


class Menu:

    def __init__(self):

        # Controls

        self.controls = pygame.image.load("controls.png")
        self.controls_size = self.controls.get_size()
        self.controls_rect = pygame.Rect(90, 180, self.controls_size[0], self.controls_size[1])

        # Stats
        self.stats = pygame.image.load("stats.png")
        self.stats_size = self.stats.get_size()
        self.stats_rect = pygame.Rect(2, 2, self.stats_size[0], self.stats_size[1])

        # Pause Menu

        # Background Scroll Button
        self.bg_scroll = pygame.image.load("background_scroll.png")
        self.bg_scroll_size = self.bg_scroll.get_size()
        self.bg_scroll_rect = pygame.Rect(800, 180, self.bg_scroll_size[0], self.bg_scroll_size[1])

        # Enabled Button
        self.bg_scroll_enabled = True

        self.bg_button = pygame.image.load("enabled.png")
        self.bg_button_size = self.bg_button.get_size()
        self.bg_button_rect = pygame.Rect(900, 254, self.bg_button_size[0], self.bg_button_size[1])

        # Return to Title Screen
        self.return_to_menu = pygame.image.load("return_to_menu.png")
        self.return_to_menu_size = self.return_to_menu.get_size()
        self.return_to_menu_rect = pygame.Rect(800, 328, self.return_to_menu_size[0], self.return_to_menu_size[1])

        # Arrow Button
        self.arrow_left = pygame.image.load("arrow.png")
        self.arrow_left_size = self.arrow_left.get_size()
        self.arrow_left_rect = pygame.Rect(800, 370, self.arrow_left_size[0], self.arrow_left_size[1])

        self.arrow_right = pygame.image.load("arrow.png")
        self.arrow_right_size = self.arrow_right.get_size()
        self.arrow_right_rect = pygame.Rect(800, 444, self.arrow_right_size[0], self.arrow_right_size[1])
        self.arrow_right = pygame.transform.flip(self.arrow_right, True, False)

        # Ghost Mode
        self.ghost_icon = pygame.image.load("ghost_menu.png")
        self.ghost_icon_size = self.ghost_icon.get_size()
        self.ghost_icon_rect = pygame.Rect(838, 96, self.ghost_icon_size[0], self.ghost_icon_size[1])

        # Hourglass
        self.hourglass_icon = pygame.image.load("hourglass_menu.png")
        self.hourglass_icon_size = self.hourglass_icon.get_size()
        self.hourglass_icon_rect = pygame.Rect(944, 96, self.hourglass_icon_size[0], self.hourglass_icon_size[1])

        # E Button
        self.e_button = pygame.image.load("e_button.png")
        self.e_button_size = self.e_button.get_size()
        self.e_button_rect = pygame.Rect(944, 22, self.e_button_size[0], self.e_button_size[1])

        # Q Button
        self.q_button = pygame.image.load("q_button.png")
        self.q_button_size = self.q_button.get_size()
        self.q_button_rect = pygame.Rect(838, 22, self.q_button_size[0], self.q_button_size[1])

    def disable_bg_scroll(self):
        self.bg_scroll_enabled = not self.bg_scroll_enabled

        if self.bg_scroll_enabled:
            self.bg_button = pygame.image.load("enabled.png")
        if not self.bg_scroll_enabled:
            self.bg_button = pygame.image.load("disabled.png")

        self.bg_button_size = self.bg_button.get_size()
        self.bg_button_rect = pygame.Rect(900, 254, self.bg_button_size[0], self.bg_button_size[1])
