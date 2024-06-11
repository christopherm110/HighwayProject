import pygame


class Menu:

    def __init__(self):

        # Controls
        self.show_tutorial = True
        self.controls = pygame.image.load("Assets/controls.png")
        self.controls_size = self.controls.get_size()
        self.controls_rect = pygame.Rect(90, 180, self.controls_size[0], self.controls_size[1])

        # Stats
        self.stats = pygame.image.load("Assets/stats.png")
        self.stats_size = self.stats.get_size()
        self.stats_rect = pygame.Rect(2, 2, self.stats_size[0], self.stats_size[1])

        # Pause Menu

        # Background Scroll
        self.bg_scroll = pygame.image.load("Assets/background_scroll.png")
        self.bg_scroll_size = self.bg_scroll.get_size()
        self.bg_scroll_rect = pygame.Rect(800, 180, self.bg_scroll_size[0], self.bg_scroll_size[1])

        # Background Scroll On/Off Button
        self.bg_scroll_enabled = True

        self.bg_button = pygame.image.load("Assets/enabled.png")
        self.bg_button_size = self.bg_button.get_size()
        self.bg_button_rect = pygame.Rect(900, 254, self.bg_button_size[0], self.bg_button_size[1])

        # Return to Title Screen
        self.title_screen = True
        self.return_to_menu = pygame.image.load("Assets/return_to_menu.png")
        self.return_to_menu_size = self.return_to_menu.get_size()
        self.return_to_menu_rect = pygame.Rect(800, 402, self.return_to_menu_size[0], self.return_to_menu_size[1])

        # Arrow Button
        self.arrow_left = pygame.image.load("Assets/arrow.png")
        self.arrow_left_size = self.arrow_left.get_size()
        self.arrow_left_rect = pygame.Rect(849, 407, self.arrow_left_size[0], self.arrow_left_size[1])

        self.arrow_right = pygame.image.load("Assets/arrow.png")
        self.arrow_right_size = self.arrow_right.get_size()
        self.arrow_right_rect = pygame.Rect(1019, 407, self.arrow_right_size[0], self.arrow_right_size[1])
        self.arrow_right = pygame.transform.flip(self.arrow_right, True, False)

        # Ghost Mode
        self.ghost_icon = pygame.image.load("Assets/ghost_menu.png")
        self.ghost_icon_size = self.ghost_icon.get_size()
        self.ghost_icon_rect = pygame.Rect(838, 96, self.ghost_icon_size[0], self.ghost_icon_size[1])

        # Hourglass
        self.hourglass_icon = pygame.image.load("Assets/hourglass_menu.png")
        self.hourglass_icon_size = self.hourglass_icon.get_size()
        self.hourglass_icon_rect = pygame.Rect(944, 96, self.hourglass_icon_size[0], self.hourglass_icon_size[1])

        # E Button
        self.e_button = pygame.image.load("Assets/e_button.png")
        self.e_button_size = self.e_button.get_size()
        self.e_button_rect = pygame.Rect(944, 22, self.e_button_size[0], self.e_button_size[1])

        # Q Button
        self.q_button = pygame.image.load("Assets/q_button.png")
        self.q_button_size = self.q_button.get_size()
        self.q_button_rect = pygame.Rect(838, 22, self.q_button_size[0], self.q_button_size[1])

        # Restart Button
        self.game_restart = False

        self.restart_img = pygame.image.load("Assets/restart.png")
        self.restart_size = self.restart_img.get_size()
        self.restart_rect = pygame.Rect(800, 328, self.restart_size[0], self.restart_size[1])

        self.restart_keybind = pygame.image.load("Assets/space_to_restart.png")
        self.restart_keybind_size = self.restart_keybind.get_size()
        self.restart_keybind_rect = pygame.Rect(432, 646, self.restart_keybind_size[0], self.restart_keybind_size[1])

        # Start Button
        self.game_started = False

        self.start_keybind = pygame.image.load("Assets/space_to_start.png")
        self.start_keybind_size = self.start_keybind.get_size()
        self.start_keybind_rect = pygame.Rect(432, 646, self.start_keybind_size[0], self.start_keybind_size[1])

        # Pause Duration
        self.show_pause = False
        self.pausing = pygame.image.load("Assets/pause_duration.png")
        self.pausing_size = self.pausing.get_size()
        self.pausing_rect = pygame.Rect(432, 20, self.pausing_size[0], self.pausing_size[1])

        self.pause_keybind = pygame.image.load("Assets/unpause_keybind.png")
        self.pause_keybind_size = self.pause_keybind.get_size()
        self.pause_keybind_rect = pygame.Rect(432, 646, self.pause_keybind_size[0], self.pause_keybind_size[1])

        # Garage Menu
        self.open_garage = False
        self.garage = pygame.image.load("Assets/garage.png")
        self.garage_size = self.garage.get_size()
        self.garage_rect = pygame.Rect(845, 400, self.garage_size[0], self.garage_size[1])

        self.car_options = ["Assets/hellcat.png", "Assets/sf21.png", "Assets/motorcycle.png"]
        self.index = 0
        self.choice = self.car_options[self.index]
        self.chosen_car = pygame.image.load(self.choice)
        self.chosen_car_size = self.chosen_car.get_size()
        self.chosen_car_rect = pygame.Rect(915, 465, self.chosen_car_size[0], self.chosen_car_size[1])

        self.open_garage_button = pygame.image.load("Assets/open_garage.png")
        self.open_garage_size = self.open_garage_button.get_size()
        self.open_garage_rect = pygame.Rect(540, 485, self.open_garage_size[0], self.open_garage_size[1])

        # Title Screen
        self.title = pygame.image.load("Assets/title.png")
        self.title_size = self.title.get_size()
        self.title_rect = pygame.Rect(0, 0, self.title_size[0], self.title_size[1])

        self.start_button = pygame.image.load("Assets/title_start.png")
        self.start_button_size = self.start_button.get_size()
        self.start_button_rect = pygame.Rect(540, 400, self.start_button_size[0], self.start_button_size[1])

    def disable_bg_scroll(self):
        self.bg_scroll_enabled = not self.bg_scroll_enabled

        if self.bg_scroll_enabled:
            self.bg_button = pygame.image.load("Assets/enabled.png")
        if not self.bg_scroll_enabled:
            self.bg_button = pygame.image.load("Assets/disabled.png")

        self.bg_button_size = self.bg_button.get_size()
        self.bg_button_rect = pygame.Rect(900, 254, self.bg_button_size[0], self.bg_button_size[1])

    def select_car(self, direction):
        if direction == "left":
            self.index = self.index - 1
        if direction == "right":
            self.index = self.index + 1
        self.choice = self.car_options[self.index]
        self.chosen_car = pygame.image.load(self.choice)
        self.chosen_car_size = self.chosen_car.get_size()
        self.chosen_car_rect = pygame.Rect(915, 465, self.chosen_car_size[0], self.chosen_car_size[1])

    def garage_open_close(self):
        if self.open_garage:
            self.open_garage_button = pygame.image.load("Assets/open_garage.png")
            self.open_garage_rect = pygame.Rect(540, 485, self.open_garage_size[0], self.open_garage_size[1])
        if not self.open_garage:
            self.open_garage_button = pygame.image.load("Assets/close_garage.png")
            self.open_garage_size = self.open_garage_button.get_size()
            self.open_garage_rect = pygame.Rect(540, 485, self.open_garage_size[0], self.open_garage_size[1])

    def restart(self):
        self.show_tutorial = True
        self.bg_scroll_enabled = True
        self.bg_button = pygame.image.load("Assets/enabled.png")
        self.bg_button_size = self.bg_button.get_size()
        self.bg_button_rect = pygame.Rect(900, 254, self.bg_button_size[0], self.bg_button_size[1])
        self.game_restart = False
        self.game_started = False
        self.show_pause = False
        self.open_garage = False
        self.title_screen = False
