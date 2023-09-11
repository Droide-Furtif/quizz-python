import pygame
from button import Button
import constants as C

class Menu:
    # constructeur
    def __init__(self, app):
        # get app's screen to draw on
        self.app = app
        self.screen = app.screen

        self.background_img = C.img_menu_background
        self.btn_list = [
            Button(self.screen, C.pos_menu_start, C.img_menu_start, C.img_menu_start_push, 'start'),
            Button(self.screen, C.pos_menu_regle, C.img_menu_start, C.img_menu_start_push, 'regles'),
            Button(self.screen, C.pos_menu_score, C.img_menu_start, C.img_menu_start_push, 'scores'),
            Button(self.screen, C.pos_menu_quit, C.img_menu_start, C.img_menu_start_push, 'quit'),
        ]

    # method update, appelée chaque frame (60fois par sec)
    def update(self):
        self.button_events()


    # method draw, appelée après l'update
    def draw(self):
        self.screen.blit(self.background_img, (0,0))
        for b in self.btn_list:
            b.draw()
        # start button text
        C.blit_text(self.screen, "Start", C.pos_menu_start_text, C.WIN_X, C.font_karmatic20)
        C.blit_text(self.screen, "Quitter", C.pos_menu_quit_text, C.WIN_X, C.font_karmatic20, C.RED)
        C.blit_text(self.screen, "Regles", C.pos_menu_regle_text, C.WIN_X, C.font_karmatic20)
        C.blit_text(self.screen, "Scores", C.pos_menu_score_text, C.WIN_X, C.font_karmatic20)

    def button_events(self):
        for b in self.btn_list:
            b.update()
            if b.isClicked('start'):
                self.app.set_state('Options')
            elif b.isClicked('quit'):
                if self.app.quit:
                    self.app.running = False
                    self.app.quit = False
                else:
                    self.app.quit = True
            elif b.isClicked('regles'):
                self.show_rules()
            elif b.isClicked('scores'):
                self.app.set_state('Scores')

    def show_rules(self):
        pass