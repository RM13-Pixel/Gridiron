# --------------------------------------------------------------------
# Gridiron
# A little gridiron (American) football game made using pygame
# Played using an xbox-style controller
# Creator: RM13-Pixel
# --------------------------------------------------------------------

import pygame
from pygame import joystick
import random
import player_list
import player_objects
from player import OPlayer, DPlayer

# Initialize the pygame
pygame.init()

# Initialize Controller
joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(joystick.Joystick(i))
for joystick in joysticks:
    joystick.init()

# Game Loop
running = True
snapped = False
setup = False

while running:
    if not setup:

        # 0: Left analog horizontal, 1: Left Analog Vertical, 2: Left Trigger
        # 3: Right Analog Horizontal, 4: Right Analog Vertical, 5: Right Trigger
        analog_keys = {0: 0, 1: 0, 2: 0, 3: 0, 4: -1, 5: -1}

        # Create a 800x800px screen
        screenX = 800
        screenY = 800
        screen = pygame.display.set_mode((screenX, screenY))

        # Title and Icon
        pygame.display.set_caption("Gridiron")
        icon = pygame.image.load("pics/american-football.png")
        pygame.display.set_icon(icon)

        # Players
        list_of_players = player_list.players
        players = player_objects.player_objects
        playerSize = 32
        playerX_change = 0
        playerY_change = 0
        defense = player_list.defense
        for i in range(len(list_of_players)):
            player = list_of_players[i]
            playerName = player[0]
            playerImgName = str(player[1])
            playerPosition = player[2]
            playerX = playerPosition[0]
            playerY = playerPosition[1]
            playerSpeed = player[3]
            playerImg = pygame.image.load(playerImgName)
            if playerImgName == "pics/ol.png" or playerImgName == "pics/qb.png":
                playerRoute = player[4]
            else:
                playerRoute = player_list.routes[random.randint(0, len(player_list.routes) - 1)]
            players[i] = OPlayer(playerImg, playerX, playerY, playerSpeed, playerRoute)
        thisPlayer = players[1]  # the player with the ball (starts with the center)

        # Ball
        ballImg = pygame.image.load("pics/football.png")
        ballSpeed = 0.001
        ball_state = "grounded"
        ballX = players[0].playerX
        ballY = players[0].playerY

        dead = False  # if the play is dead


        def draw(givenPlayer: OPlayer):
            screen.blit(givenPlayer.playerImg, (givenPlayer.playerX, givenPlayer.playerY))


        def run_route(givenPlayer: OPlayer):
            route = givenPlayer.playerRoute
            speed = givenPlayer.playerSpeed - 0.01
            if ((givenPlayer == players[10] and not route[6]) or (
                    givenPlayer != players[10])) and givenPlayer.playerY > (
                    player_list.scrimmageY + (2 * playerSize)):
                givenPlayer.playerX += 0
                givenPlayer.playerY += 0
            elif not (abs(givenPlayer.playerX - route[5]) < (playerSize / 2)):
                givenPlayer.oldX = givenPlayer.playerX
                givenPlayer.oldY = givenPlayer.playerY
                if (not route[6]) and (not abs(givenPlayer.playerY - route[2]) < (playerSize / 2)):  # first route part
                    givenPlayer.playerX += speed * route[0]
                    givenPlayer.playerY += speed * route[1]
                # elif abs(givenPlayer.playerY - route[2]) < (playerSize) and route[4] is not 0:
                #     # givenPlayer.playerX += (route[3]/abs(route[3])) * (playerSize)
                #     givenPlayer.playerY += (route[4]/abs(route[4])) * (playerSize)
                else:
                    route[6] = True
                    givenPlayer.playerX += speed * route[3]
                    givenPlayer.playerY += speed * route[4]


        def show_ball():
            screen.blit(ballImg, (thisPlayer.playerX, thisPlayer.playerY))


        def pass_ball(qb: OPlayer, givenReceiver: OPlayer):
            global ball_state
            global ballX
            global ballY
            global thisPlayer
            global dead

            current_x = givenReceiver.playerX
            current_y = givenReceiver.playerY

            start_x = qb.playerX
            start_y = qb.playerY
            end_x = current_x
            end_y = current_y

            x_distance = end_x - start_x
            y_distance = end_y - start_y

            ballX += x_distance * ballSpeed
            ballY += y_distance * ballSpeed

            screen.blit(ballImg, (ballX, ballY))
            if ((abs(givenReceiver.playerX - ballX) < (playerSize / 2)) and (
                    abs(givenReceiver.playerY - ballY) < (playerSize / 2))):
                ball_state = "grounded"
                thisPlayer = givenReceiver
            if ballX <= 0:
                dead = True
            elif ballX >= screenX:
                dead = True
            if ballY <= 0:
                dead = True
            elif ballY >= screenY:
                dead = True
            draw(player)


        def defend(d_player: DPlayer, o_player: OPlayer):
            global dead
            global thisPlayer
            if (abs(d_player.ogX - o_player.playerX) < (playerSize * 2) or
                    abs(d_player.ogY - o_player.playerY) < (playerSize * 2)):
                if o_player.playerX > d_player.playerX + 0:
                    d_player.playerX += d_player.playerSpeed
                else:
                    d_player.playerX -= d_player.playerSpeed
                if o_player.playerY > d_player.playerY + 32:
                    d_player.playerY += d_player.playerSpeed
                else:
                    d_player.playerY -= d_player.playerSpeed
            if o_player == thisPlayer:
                if o_player.playerX > d_player.playerX:
                    d_player.playerX += d_player.playerSpeed
                else:
                    d_player.playerX -= d_player.playerSpeed
                if o_player.playerY > d_player.playerY + 7:
                    d_player.playerY += d_player.playerSpeed
                else:
                    d_player.playerY -= d_player.playerSpeed
                if abs(o_player.playerX - d_player.playerX) < 8 and abs(o_player.playerY - d_player.playerY) < 8:
                    dead = True
                    thisPlayer = d_player


        setup = True
    if setup:
        screen.fill((93, 93, 93))

        # Background
        # screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if keystroke is pressed check whether its right or left
            if not snapped:
                # for player in players:
                #     if player.playerRoute in player_list.routes:
                #         rIndex = player_list.routes.index(player.playerRoute)
                #         routeImgName = "pics/routes/Routes-" + str(rIndex) + ".png"
                #         routeImg = pygame.image.load(routeImgName)
                #         screen.blit(routeImg, (player.playerX, player.playerY-224))
                if event.type == pygame.JOYBUTTONUP:
                    if event.button == 0:
                        snapped = True
                        thisPlayer = players[0]  # the quarterback is given the ball
                if event.type == pygame.JOYAXISMOTION:
                    analog_keys[event.axis] = event.value
                    if analog_keys[4] > 0 or analog_keys[5] > 0:  # Left or Right trigger
                        for player in players:
                            if player.playerRoute in player_list.routes:
                                rIndex = player_list.routes.index(player.playerRoute)
                                routeImgName = "pics/routes/Routes-" + str(rIndex) + ".png"
                                routeImg = pygame.image.load(routeImgName)
                                for num in range(500):
                                    screen.blit(routeImg, (player.playerX - (playerSize / 2), player.playerY - 224))
            if snapped:
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 4:  # LB
                        setup = False
                        snapped = False
                        for player in players:
                            player.playerRoute[6] = False
                        for player in defense:
                            player.playerX = player.ogX
                            player.playerY = player.ogY
                        break
                # Handles analog inputs
                if not dead and event.type == pygame.JOYAXISMOTION:
                    analog_keys[event.axis] = event.value
                    # print(analog_keys)
                    # Horizontal Analog
                    if abs(analog_keys[0]) > .4:
                        if analog_keys[0] < -.5:
                            playerX_change = -thisPlayer.playerSpeed
                        if analog_keys[0] > .5:
                            playerX_change = thisPlayer.playerSpeed
                    else:
                        playerX_change = 0
                    # Vertical Analog
                    if abs(analog_keys[1]) > .4:
                        if analog_keys[1] < -.5:
                            playerY_change = -thisPlayer.playerSpeed
                        if analog_keys[1] > .5:
                            playerY_change = thisPlayer.playerSpeed
                    else:
                        playerY_change = 0

                # Passing
                if not dead and thisPlayer == players[0]:  # only the QB can pass
                    if event.type == pygame.JOYBUTTONDOWN:
                        if event.button == 0:  # Green A
                            ballX = players[0].playerX
                            ballY = players[0].playerY
                            ball_state = "passing"
                            receiver = players[9]  # TE
                        if event.button == 1:  # Red B
                            ballX = players[0].playerX
                            ballY = players[0].playerY
                            ball_state = "passing"
                            receiver = players[6]  # WR1
                        if event.button == 3:  # Yellow Y
                            ballX = players[0].playerX
                            ballY = players[0].playerY
                            ball_state = "passing"
                            receiver = players[8]  # Slot
                        if event.button == 2:  # Blue X
                            ballX = players[0].playerX
                            ballY = players[0].playerY
                            ball_state = "passing"
                            receiver = players[7]  # WR2
                        if event.button == 5:  # Pink RB
                            ballX = players[0].playerX
                            ballY = players[0].playerY
                            ball_state = "passing"
                            receiver = players[10]  # RB
                # if thisPlayer == players[0]:  # only the QB can pass
                #     if event.type == pygame.JOYBUTTONDOWN:
                #         if event.button == 0:  # Green A
                #             thisPlayer = players[9]  # TE
                #         if event.button == 1:  # Red B
                #             thisPlayer = players[6]  # WR1
                #         if event.button == 3:  # Yellow Y
                #             thisPlayer = players[8]  # Slot
                #         if event.button == 2:  # Blue X
                #             thisPlayer = players[7]  # WR2
                #         if event.button == 5:  # Pink RB
                #             thisPlayer = players[10]  # RB

        # Ensure player is in bounds
        thisPlayer.playerX += playerX_change
        thisPlayer.playerY += playerY_change

        for player in players:
            if not dead and snapped and player != thisPlayer:
                run_route(player)
            if player.playerX <= 0:
                player.playerX = 0
            elif player.playerX >= screenX - playerSize:
                player.playerX = screenX - playerSize
            if player.playerY <= 0:
                player.playerY = 0
            elif player.playerY >= screenY - playerSize:
                player.playerY = screenY - playerSize
            draw(player)
        for idx in range(len(defense)):
            if snapped and idx < 9:
                defend(defense[idx], players[idx + 2])
            if ball_state == "grounded" and snapped and idx >= 9 and not dead:
                defend(defense[idx], thisPlayer)
            draw(defense[idx])
        draw(defense[9])
        draw(defense[10])
        if ball_state == "grounded":
            show_ball()
        else:
            pass_ball(thisPlayer, receiver)
        if dead:
            playerX_change = 0
            playerY_change = 0
        pygame.display.update()
