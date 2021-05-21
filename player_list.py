# --------------------------------------------------------------------
# Player List
# Contains player positions, player routes, offensive player attributes,
# and defensive players
# Creator: RM13-Pixel
# --------------------------------------------------------------------
from player import OPlayer, DPlayer

screenX = 800
screenY = 800
playerSize = 32

# positions to line up
qbX = (screenX / 2) - (playerSize / 2)
qbY = (screenY / 1.25) - (playerSize / 2)
scrimmageY = qbY - playerSize
offY = qbY

cX = qbX
lgX = qbX - playerSize
rgX = qbX + playerSize
ltX = qbX - (2 * playerSize)
rtX = qbX + (2 * playerSize)
rightWrX = screenX - (4 * playerSize)  # the far right side
leftWrX = (3 * playerSize)  # the far left side
leftSlotX = (leftWrX + ltX) / 2  # between the wr2 and lt
rightSlotX = (rightWrX + rtX) / 2
teX = rtX + playerSize
rbX = qbX
rbY = qbY + (2 * playerSize)

# route tuples = (Xspeed, Yspeed, Ychange, newXspeed, newYspeed, Xstop, changed)
none = [0, 0, scrimmageY, 0, 0, 0, False]
guard = [0, 0, scrimmageY + (playerSize / 2), 0, 1, 0, False]
tackle = [0, 0, scrimmageY + playerSize, 0, 1, 0, False]

leftFlat = [0, -1, scrimmageY - (4 * playerSize), -1, 0, 2 * playerSize, False]
leftSlant = [0, -1, scrimmageY - (2 * playerSize), 1, -0.75, rightSlotX, False]
leftComeback = [0, -1, scrimmageY - (5 * playerSize), -1, 0.75, 2 * playerSize, False]
leftCurl = [0, -1, scrimmageY - (5 * playerSize), 1, 0.75, ltX, False]
leftOut = [0, -1, scrimmageY - (5 * playerSize), -1, 0, 2 * playerSize, False]
leftDig = [0, -1, scrimmageY - (5 * playerSize), 1, 0, rightSlotX, False]
leftCorner = [0, -1, scrimmageY - (5 * playerSize), -1, -0.75, 2 * playerSize, False]
leftPost = [0, -1, scrimmageY - (5 * playerSize), 1, -0.75, rightWrX, False]
leftWheel = [-1, -0.5, scrimmageY, 0, -1, 0, False]

rightFlat = [0, -1, scrimmageY - (4 * playerSize), 1, 0, screenX - 2 * playerSize, False]
rightSlant = [0, -1, scrimmageY - (2 * playerSize), -1, 1, leftSlotX, False]
rightComeback = [0, -1, scrimmageY - (5 * playerSize), 1, 0.75, screenX - 2 * playerSize, False]
rightCurl = [0, -1, scrimmageY - (5 * playerSize), -1, 0.75, rtX, False]
rightOut = [0, -1, scrimmageY - (5 * playerSize), 1, 0, screenX - 2 * playerSize, False]
rightDig = [0, -1, scrimmageY - (5 * playerSize), -1, 0, leftSlotX, False]
rightCorner = [0, -1, scrimmageY - (5 * playerSize), 1, -0.75, screenX - 2 * playerSize, False]
rightPost = [0, -1, scrimmageY - (5 * playerSize), -1, -0.75, leftWrX, False]
rightWheel = [1, -0.5, scrimmageY, 0, -1, 0, False]

fade = [0, -1, scrimmageY - (5 * playerSize), 0, -1, 0, False]

routes = [leftFlat,
          leftSlant,
          leftComeback,
          leftCurl,
          leftOut,
          leftDig,
          leftCorner,
          leftPost,
          leftWheel,
          rightFlat,
          rightSlant,
          rightComeback,
          rightCurl,
          rightOut,
          rightDig,
          rightCorner,
          rightPost,
          rightWheel,
          fade]
# singleback deuce slot
players = [("qb", "pics/qb.png", (qbX, qbY), 0.075, none),
           ("c", "pics/ol.png", (cX, scrimmageY), 0.03, none),  # Offensive Line
           ("lg", "pics/ol.png", (lgX, scrimmageY), 0.03, guard),
           ("rg", "pics/ol.png", (rgX, scrimmageY), 0.03, guard),
           ("lt", "pics/ol.png", (ltX, scrimmageY), 0.03, tackle),
           ("rt", "pics/ol.png", (rtX, scrimmageY), 0.03, tackle),
           ("wr1", "pics/redB.png", (rightWrX, scrimmageY), 0.09, rightDig),  # Skill positions
           ("wr2", "pics/blueX.png", (leftWrX, scrimmageY), 0.085, leftComeback),
           ("slot", "pics/yellowY.png", (leftSlotX, offY), 0.085, leftCurl),
           ("te", "pics/greenA.png", (teX, offY), 0.08, rightPost),
           ("rb", "pics/pinkRB.png", (rbX, rbY), 0.09, rightWheel)
           ]

# cX = qbX
# lgX = qbX - playerSize
# rgX = qbX + playerSize
# ltX = qbX - (2 * playerSize)
# rtX = qbX + (2 * playerSize)
# rightWrX = screenX - (4 * playerSize)  # the far right side
# leftWrX = (3 * playerSize)  # the far left side
# leftSlotX = (leftWrX + ltX) / 2  # between the wr2 and lt
# rightSlotX = (rightWrX + rtX) / 2
# teX = rtX + playerSize
# rbX = qbX
# rbY = qbY + (2 * playerSize)

# players = [("qb", "pics/qb.png", (qbX, qbY), 0.075, none),
#            ("c", "pics/ol.png", (cX, scrimmageY), 0.03, none),  # Offensive Line
#            ("lg", "pics/ol.png", (lgX, scrimmageY), 0.03, guard),
#            ("rg", "pics/ol.png", (rgX, scrimmageY), 0.03, guard),
#            ("lt", "pics/ol.png", (ltX, scrimmageY), 0.03, tackle),
#            ("rt", "pics/ol.png", (rtX, scrimmageY), 0.03, tackle),
#            ("wr1", "pics/redB.png", (rightWrX, scrimmageY), 0.09, rightDig),  # Skill positions
#            ("wr2", "pics/blueX.png", (leftWrX, scrimmageY), 0.085, leftComeback),
#            ("slot", "pics/yellowY.png", (leftSlotX, offY), 0.085, leftCurl),
#            ("te", "pics/greenA.png", (teX, offY), 0.08, rightPost),
#            ("rb", "pics/pinkRB.png", (rbX, rbY), 0.09, rightWheel)
#            ]

defense = [DPlayer(lgX, scrimmageY - playerSize),  # Dline
           DPlayer(rgX, scrimmageY - playerSize),
           DPlayer(ltX - (playerSize / 2), scrimmageY - playerSize),
           DPlayer(rtX + (playerSize / 2), scrimmageY - playerSize),
           DPlayer(rightWrX, scrimmageY - playerSize),  # Corners
           DPlayer(leftWrX, scrimmageY - playerSize),
           DPlayer(leftSlotX, scrimmageY - (3 * playerSize)),  # Linebackers
           DPlayer(teX, scrimmageY - (3 * playerSize)),
           DPlayer(cX, scrimmageY - (4 * playerSize)),
           DPlayer(rgX, scrimmageY - (7 * playerSize)),  # Safeties
           DPlayer(lgX, scrimmageY - (6 * playerSize)),
           ]
