# --------------------------------------------------------------------
# Player Objects
# Contains blank player objects to be altered later
# Creator: RM13-Pixel
# --------------------------------------------------------------------
import pygame

from player import OPlayer

img = pygame.image.load("pics/blank.png")
qb = OPlayer(img, 400, 400, 0.5, "none")
c = OPlayer(img, 400, 400, 0.5, "none")
lg = OPlayer(img, 400, 400, 0.5, "none")
rg = OPlayer(img, 400, 400, 0.5, "none")
lt = OPlayer(img, 400, 400, 0.5, "none")
rt = OPlayer(img, 400, 400, 0.5, "none")
b = OPlayer(img, 400, 400, 0.5, "none")
x = OPlayer(img, 400, 400, 0.5, "none")
y = OPlayer(img, 400, 400, 0.5, "none")
a = OPlayer(img, 400, 400, 0.5, "none")
rb = OPlayer(img, 400, 400, 0.5, "none")

player_objects = [qb,
                  c,
                  lg,
                  rg,
                  lt,
                  rt,
                  b,
                  x,
                  y,
                  a,
                  rb]
