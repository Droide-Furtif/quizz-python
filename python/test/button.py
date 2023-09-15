import pygame
import constants as C

class Button:
    def __init__(self, screen, pos, img, pushed_img=C.img_reponse_bleu_push, name="", permapushed = False):
        self.screen = screen
        self.x = pos[0]
        self.y = pos[1]
        self.name = name
        self.clickedOnce = False

        # load images
        self.unpushed_img = img
        self.pushed_img = pushed_img

        # initialise width et height selon la taille de l'image
        self.w = self.unpushed_img.get_width()
        self.h = self.unpushed_img.get_height()

        self.pushed = False
        self.t = 0
        self.permapushed = permapushed
        self.visible = True
    def update(self):
        # button press 'animation', button stay pushed for 0.5s (30frames)
        if self.visible:
            if self.pushed: self.t += 1
            if self.t > 30 and not self.permapushed:
                self.pushed = False
                self.t = 0

    def draw(self):
        if self.visible:
            if self.pushed:
                self.screen.blit(self.pushed_img, (self.x, self.y))
            else:
                self.screen.blit(self.unpushed_img, (self.x, self.y))

    def checkForClick(self):
        x, y = pygame.mouse.get_pos()
        return x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h

    def isClicked(self, name=""):
        if name == "":
            pass
        else:
            if self.name != name:
                return False
        # if pressed, return true once and change clickedOnce to false until not pressed anymore
        if pygame.mouse.get_pressed()[0]:
            if self.checkForClick():
                if not self.clickedOnce:
                    self.clickedOnce = True
                    self.pushed = True
                    return True
                else:
                    return False
        else:
            self.clickedOnce = False
            return False

    def change_color(self, color):
        self.unpushed_img = pygame.image.load(f"img/boutons/questions/rep_nopush_{color}.png")
        self.pushed_img = pygame.image.load(f"img/boutons/questions/rep_push_{color}.png")
        
    def change_image(self, image1, image2):
        self.unpushed_img = image1
        self.pushed_img = image2