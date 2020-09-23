import pygame

class Settings():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 140, 50)

        self.def_box_size = (100, 30)

        self.color_inact = (255, 255, 255)
        self.color_active = (200, 200, 200)

        self.dr_button_color = (199, 178, 20)
        self.p_button_color = (20, 53, 199)
        self.do_button_color = (184, 27, 9)

        self.font = pygame.font.Font(None, 25)
