# --------------------------------------------------------------------
# Player
# Contains the OPlayer and DPlayer classes used in Gridiron
# Creator: RM13-Pixel
# --------------------------------------------------------------------
import pygame


class OPlayer:
    def __init__(self, givenImg, givenX, givenY, givenSpeed, givenRoute):
        self.playerImg = givenImg
        self.playerX = givenX
        self.playerY = givenY
        self.playerSpeed = givenSpeed
        self.playerRoute = givenRoute


class DPlayer:
    def __init__(self, givenX, givenY):
        self.playerImg = pygame.image.load("pics/defense.png")
        self.playerX = givenX
        self.playerY = givenY
        self.ogX = givenX
        self.ogY = givenY
        self.playerSpeed = 0.06
