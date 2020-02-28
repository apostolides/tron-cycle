import pygame
import sys
import time

pygame.init()
pygame.display.set_caption("Tron")

'''
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
'''

frame_resolution = width, height = 800, 600

screen = pygame.display.set_mode(frame_resolution)

# ---- Player images initialization ---- #
player_a_img = pygame.image.load("player_a.png")
player_b_img = pygame.image.load("player_b.png")


player_a_img = pygame.transform.scale(player_a_img,(10,10))
player_b_img = pygame.transform.scale(player_b_img,(10,10))

crushed = pygame.image.load("crushed.png")
crushed = pygame.transform.scale(crushed,(10,10))

player_a_rect = player_a_img.get_rect().move(100,height/2)
player_b_rect = player_b_img.get_rect().move(width-100,height/2)

# ---- Player speed, area and direction initialization ---- #
player_a_speed = [10,0]
player_b_speed = [-10,0]

player_a_direction = "right"
player_b_direction = "left"

player_a_area = []
player_b_area = []

player_a_area.append((player_a_rect.x,player_a_rect.y))
player_b_area.append((player_b_rect.x,player_b_rect.y))

# ---- Main game loop ---- #
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # ---- Key handling ---- #
            # ---- Player a movement ---- #
            if event.key == pygame.K_w and player_a_direction != "down":
                player_a_direction = "up"
                player_a_speed[0] = 0
                player_a_speed[1] = -10
            elif event.key == pygame.K_s and player_a_direction != "up":
                player_a_direction = "down"
                player_a_speed[0] = 0
                player_a_speed[1] = 10
            elif event.key == pygame.K_a and player_a_direction != "right":
                player_a_direction = "left"
                player_a_speed[0] = -10
                player_a_speed[1] = 0
            elif event.key == pygame.K_d and player_a_direction != "left":
                player_a_direction = "right"
                player_a_speed[0] = 10
                player_a_speed[1] = 0
            # ---- Player b movement ---- #
            if event.key == pygame.K_UP and player_b_direction != "down":
                player_b_direction = "up"
                player_b_speed[0] = 0
                player_b_speed[1] = -10
            elif event.key == pygame.K_DOWN and player_b_direction != "up":
                player_b_direction = "down"
                player_b_speed[0] = 0
                player_b_speed[1] = 10
            elif event.key == pygame.K_LEFT and player_b_direction != "right":
                player_b_direction = "left"
                player_b_speed[0] = -10
                player_b_speed[1] = 0
            elif event.key == pygame.K_RIGHT and player_b_direction != "left":
                player_b_direction = "right"
                player_b_speed[0] = 10
                player_b_speed[1] = 0

    player_a_rect = player_a_rect.move(player_a_speed)
    player_b_rect = player_b_rect.move(player_b_speed)


    # ---- Check for player collision ---- #
    if (player_a_rect.x,player_a_rect.y) == (player_b_rect.x,player_b_rect.y):
        print("Tied")
        screen.blit(crushed, player_a_rect)
        screen.blit(crushed, player_b_rect)
        break
    elif (player_a_rect.x,player_a_rect.y) in player_a_area or (player_a_rect.x,player_a_rect.y) in player_b_area:
        print("Player A (blue) lost")
        screen.blit(crushed, player_a_rect)
        break
    elif (player_b_rect.x,player_b_rect.y) in player_a_area or (player_b_rect.x,player_b_rect.y) in player_b_area:
        print("Player B (red) lost")
        screen.blit(crushed, player_b_rect)
        break

    player_a_area.append((player_a_rect.x,player_a_rect.y))
    player_b_area.append((player_b_rect.x,player_b_rect.y))

    # ---- Check for border collision ---- #
    if player_a_rect.left < 0 or player_a_rect.right > width or player_a_rect.top < 0 or player_a_rect.bottom > height:
        print("Player A (blue) lost")
        screen.blit(crushed, player_a_area[-2])
        break
    elif player_b_rect.left < 0 or player_b_rect.right > width or player_b_rect.top < 0 or player_b_rect.bottom > height:
        print("Player B (red) lost")
        screen.blit(crushed, player_b_area[-2])
        break

    # ---- Draw objects ---- #
    screen.blit(player_a_img, player_a_rect)
    screen.blit(player_b_img, player_b_rect)
    # ---- Show on screen ---- #
    pygame.display.update()
    time.sleep(0.04)

pygame.display.update()

# ---- Press any key to continue ---- #
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()
