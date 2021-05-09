import pygame
import random
import sys
pygame.init()
pygame.display.init()

s_w = 800
s_h = 600
fps = 40
win = pygame.display.set_mode((800,600))
pygame.display.set_caption(" Crazy Car ")

# Colors
white =(255,255,250)
red = (255,0,0)
green = (0,255,0)
yellow = (255,255,0)
black = (0,0,0)
blue = (0,0,245,0.8)
brown  =(240,10,150)
darkgreen=(20,120,245)
gray = (190,190,190) 


clock = pygame.time.Clock()
side_count = 0
side_jump = 7
up_jump = 8
sudden_jump = 40
car_jump = 5

img_red = pygame.image.load("red100x185_1.jpg")
img_yellow = pygame.image.load("yellow100x181_1.jpg")
img_purple = pygame.image.load("purple100x185_1.jpg")
img_green = pygame.image.load("green100x185_1.jpg")
 if red_x < 0 : if red_x < 0 :
            red_x = 0
        if red_x > s_w-100:
            red_x = s_w-100
        if red_y < 0 :
            red_y = 0
        if red_y > s_h-185:
            red_y = s_h-185

            red_x = 0
        if red_x > s_w-100:
            red_x = s_w-100
        if red_y < 0 :
            red_y = 0
        if red_y > s_h-185:
            red_y = s_h-185

font1 = pygame.font.SysFont(None, 30, bold=True, italic=False)


def gameloop():
    run = True
    loop_count = 0

    right = False
    left =  False
    up = False
    down  =  False

    play = True

    red_x = int(s_w/2) -50
    red_y = s_h + 200

    lane1_y = -400
    lane2_y = -500
    lane3_y = -50
    lane4_y = -350
    lane5_y = -600

    press_count = 0
    


    while run:

        win.fill(white)
        win.blit( img_red,(red_x,red_y) )
        loop_count += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break
        
        if red_x < 0 :
            red_x = 0
        if red_x > s_w-100:
            red_x = s_w-100
        if red_y < 0 :
            red_y = 0
        if red_y > s_h-185:
            red_y = s_h-185


        clock.tick(fps)
        pygame.display.flip()
    
    

        

gameloop()

