import pygame

class Led():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load("led.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.imagelight = pygame.image.load("light.png")
        self.rectlight = self.imagelight.get_rect()
        self.rectlight.x = x + 20
        self.rectlight.y = y - 15
        self.active = False

    def showLed(self):
        self.screen.blit(self.image, self.rect)
        if self.active == True:
            self.showLight()

    def showLight(self):
        self.screen.blit(self.imagelight, self.rectlight)

class Arrow():
    def __init__(self, screen, image, IA, side, x, y):
        self.screen = screen
        self.image = pygame.image.load(image)
        self.NA = pygame.image.load(image)
        self.IA = pygame.image.load(IA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.side = side
        self.active = False

    def show(self):
        self.screen.blit(self.image, self.rect)

    def setactive(self):
        self.active = True
        self.image = self.IA

    def setnonactive(self):
        self.image = self.NA
        self.active = False


class Terminator():
    def __init__(self, led, led2, led3, led4, la, la2, la3, la4):
        self.led00 = led3
        self.led10 = led4
        self.led01 = led
        self.led11 = led2
        self.arrowL = la
        self.arrowR = la2
        self.arrowU = la3
        self.arrowD = la4
        self.x = 0
        self.y = 0
        self.pressedUp = False
        self.pressedDown = False
        self.pressedRight = False
        self.pressedLeft = False



    def actionled(self):
        if self.x == 0 and self.y == 0:
            self.led00.active = not self.led00.active
        if self.x == 1 and self.y == 0:
            self.led10.active = not self.led10.active
        if self.x == 0 and self.y == 1:
            self.led01.active = not self.led01.active
        if self.x == 1 and self.y == 1:
            self.led11.active = not self.led11.active

    def positionchange(self, x, y):

        self.x += x
        self.y += y
        self.actionled()
        if self.x < -1:
            self.x = -1
        if self.x > 2:
            self.x = 2
        if self.y < -1:
            self.y = -1
        if self.y > 2:
            self.y = 2

