import pygame
import sys
import time

pygame.init()
frame_resolution = width, height = 800, 600
bg_color = 0, 0, 0 # Black background

screen = pygame.display.set_mode(frame_resolution)

# ---- Player initialization ---- #
player_a_img = pygame.image.load("player_a.png")
player_b_img = pygame.image.load("player_b.png")

player_a_img = pygame.transform.scale(player_a_img,(10,10))
player_b_img = pygame.transform.scale(player_b_img,(10,10))

player_a_speed = [1,0]
player_b_speed = [-1,0]

player_a_rect = player_a_img.get_rect().move(100,height/2)
player_b_rect = player_b_img.get_rect().move(width-100,height/2)

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
            if event.key == pygame.K_w:
                player_a_speed[0] = 0
                player_a_speed[1] = -1
            if event.key == pygame.K_s:
                player_a_speed[0] = 0
                player_a_speed[1] = 1
            if event.key == pygame.K_a:
                player_a_speed[0] = -1
                player_a_speed[1] = 0
            if event.key == pygame.K_d:
                player_a_speed[0] = 1
                player_a_speed[1] = 0
            # ---- Player b movement ---- #
            if event.key == pygame.K_UP:
                player_b_speed[0] = 0
                player_b_speed[1] = -1
            if event.key == pygame.K_DOWN:
                player_b_speed[0] = 0
                player_b_speed[1] = 1
            if event.key == pygame.K_LEFT:
                player_b_speed[0] = -1
                player_b_speed[1] = 0
            if event.key == pygame.K_RIGHT:
                player_b_speed[0] = 1
                player_b_speed[1] = 0

    player_a_rect = player_a_rect.move(player_a_speed)
    player_b_rect = player_b_rect.move(player_b_speed)


    # ---- Check for player collision ---- #
    if (player_a_rect.x,player_a_rect.y) == (player_b_rect.x,player_b_rect.y):
        print("Tie")
        break
    elif (player_a_rect.x,player_a_rect.y) in player_a_area or (player_a_rect.x,player_a_rect.y) in player_b_area:
        print("Player A (blue) lost")
        break
    elif (player_b_rect.x,player_b_rect.y) in player_a_area or (player_b_rect.x,player_b_rect.y) in player_b_area:
        print("Player B (red) lost")
        break

    player_a_area.append((player_a_rect.x,player_a_rect.y))
    player_b_area.append((player_b_rect.x,player_b_rect.y))

    # ---- Check for border collision ---- #
    if player_a_rect.left < 1 or player_a_rect.right > width-1 or player_a_rect.top < 1 or player_a_rect.bottom > height-1:
        print("Player A (blue) lost")
        break
    elif player_b_rect.left < 1 or player_b_rect.right > width-1 or player_b_rect.top < 1 or player_b_rect.bottom > height-1:
        print("Player B (red) lost")
        break

    # ---- Draw objects ---- #
    screen.blit(player_a_img, player_a_rect)
    screen.blit(player_b_img, player_b_rect)
    # ---- Show on screen ---- #
    pygame.display.update()
    time.sleep(0.005)
