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
        self.title_screen = False
        self.return_to_menu = pygame.image.load("Assets/return_to_menu.png")
        self.return_to_menu_size = self.return_to_menu.get_size()
        self.return_to_menu_rect = pygame.Rect(800, 402, self.return_to_menu_size[0], self.return_to_menu_size[1])

        # Arrow Button
        self.arrow_left = pygame.image.load("Assets/arrow.png")
        self.arrow_left_size = self.arrow_left.get_size()
        self.arrow_left_rect = pygame.Rect(780, 328, self.arrow_left_size[0], self.arrow_left_size[1])

        self.arrow_right = pygame.image.load("Assets/arrow.png")
        self.arrow_right_size = self.arrow_right.get_size()
        self.arrow_right_rect = pygame.Rect(1003, 328, self.arrow_right_size[0], self.arrow_right_size[1])
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

        # Garage Menu Placeholder
        self.open_garage = False
        self.garage = pygame.image.load("Assets/menu_temp.png")
        self.garage_size = self.garage.get_size()
        scale_size = (self.garage_size[0] * 3, self.garage_size[1] * 3)
        self.garage = pygame.transform.scale(self.garage, scale_size)
        self.garage_size = self.garage.get_size()
        self.garage_rect = pygame.Rect(780, 328, self.garage_size[0], self.garage_size[1])

        self.car_options = ["Assets/blue_car.png", "Assets/yellow_coupe.png", "Assets/white_cargo_truck.png", "Assets"
                                                        "/gray_van.png", "Assets/green_truck.png", "Assets/f1.png"]
        self.index = 0
        self.choice = self.car_options[self.index]
        self.chosen_car = pygame.image.load(self.choice)
        self.chosen_car_size = self.chosen_car.get_size()
        self.chosen_car_rect = pygame.Rect(892, 420, self.chosen_car_size[0], self.chosen_car_size[1])

        self.start_button = pygame.image.load("Assets/start_button.png")
        self.start_button_size = self.start_button.get_size()
        scale_size2 = (self.start_button_size[0] * 0.3, self.start_button_size[1] * 0.3)
        self.start_button = pygame.transform.scale(self.start_button, scale_size2)
        self.start_button_size = self.start_button.get_size()
        self.start_button_rect = pygame.Rect(450, 360, self.start_button_size[0], self.start_button_size[1])

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
        self.chosen_car_rect = pygame.Rect(892, 420, self.chosen_car_size[0], self.chosen_car_size[1])

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
