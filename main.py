import sys

import pygame

from resource import *


def noarrowsactive():
    mohamed.pressedUp = False
    mohamed.pressedDown = False
    mohamed.pressedRight = False
    mohamed.pressedLeft = False
    la.setnonactive()
    la2.setnonactive()
    la3.setnonactive()
    la4.setnonactive()


screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Led Control")
pygame.display.set_icon(pygame.image.load("led.png"))
led1 = Led(screen, 250, 100)
led2 = Led(screen, 500, 100)
led3 = Led(screen, 250, 300)
led4 = Led(screen, 500, 300)
la = Arrow(screen, "L.png", "L2.png", "Left", 20, 400)
la2 = Arrow(screen, "R.png", "R2.png", "Right", 150, 400)
la3 = Arrow(screen, "U.png", "U2.png", "Up", 95, 320)
la4 = Arrow(screen, "D.png", "D2.png", "Down", 95, 460)

mohamed = Terminator(led1, led2, led3, led4, la, la2, la3, la4)

while 1 == 1:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                noarrowsactive()
                la.setactive()
                if mohamed.pressedLeft == False:
                    mohamed.positionchange(-1, 0)
                    mohamed.pressedLeft = True
            elif event.key == pygame.K_RIGHT:
                noarrowsactive()
                la2.setactive()
                if mohamed.pressedRight == False:
                    mohamed.positionchange(1, 0)
                    mohamed.pressedRight = True
            elif event.key == pygame.K_UP:
                noarrowsactive()
                la3.setactive()
                if mohamed.pressedUp == False:
                    mohamed.positionchange(0, 1)
                    mohamed.pressedUp = True
            elif event.key == pygame.K_DOWN:
                noarrowsactive()
                la4.setactive()
                if mohamed.pressedDown == False:
                    mohamed.positionchange(0, -1)
                    mohamed.pressedDown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                mohamed.pressedLeft = False
                la.setnonactive()
            if event.key == pygame.K_RIGHT:
                mohamed.pressedRight = False
                la2.setnonactive()
            if event.key == pygame.K_UP:
                mohamed.pressedUp = False
                la3.setnonactive()
            if event.key == pygame.K_DOWN:
                mohamed.pressedDown = False
                la4.setnonactive()



    led1.showLed()
    led2.showLed()
    led3.showLed()
    led4.showLed()
    la.show()
    la2.show()
    la3.show()
    la4.show()
    print(mohamed.y)
    pygame.display.flip()


#добавить еще три светодид\ода и еще 3 стрелочки
#сохранить стрелки во втором цвете(Pixilart.com)
#внутри     for event in pygame.event.get():   добавить обработку нажатия и расжатия стрелок(pass)