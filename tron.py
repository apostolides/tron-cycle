import pygame
import sys
import time

pygame.init()
frame_resolution = width, height = 800, 600
bg_color = 0, 0, 0 # Black

screen = pygame.display.set_mode(frame_resolution)

player_a_x = 20
player_b_x = width - 20
player_a_y = player_b_y = height/2

player_a_img = pygame.image.load("player_a.png")
player_b_img = pygame.image.load("player_b.png")

player_a_speed = [1,0]
player_b_speed = [-1,0]

player_a_rect = player_a_img.get_rect()
player_b_rect = player_b_img.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # ---- Key handling ---- #
            #print(pygame.key.name(event.key))
            # ---- player a movement ---- #
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
            # ---- player b movement ---- #
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

    #screen.fill(bg_color)
    screen.blit(player_a_img, player_a_rect)
    screen.blit(player_b_img, player_b_rect)

    pygame.display.update()
    time.sleep(0.01)
