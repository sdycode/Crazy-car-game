import pygame
import random
import sys
pygame.init()

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

# Light colors :
light_1 = (245,235,2)
light_2 = (5,235,211)
light_3 = (245,5,222)
light_4 = (221,220,2)
light_5 = (5,211,240)
light_6 = (210,20,240)



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

font1 = pygame.font.SysFont(None, 30, bold=True, italic=False)

def text_on_screen(text,x,y,width,height,color,bgcolor):
    text_screen = font1.render(text, True, color,bgcolor)
    win.blit(text_screen,(x,y))

def car_on_lane(lane_no,image,y):
    win.blit(image,(160*(lane_no-1)+50,y) )
    pygame.display.update()

# def track(lane_no, width, height, color):
#     path = pygame.draw.rect(win, color,[160*(lane_no-1),0,width,height])
# NOT needed


def game_loop():
    
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

        pygame.draw.rect(win,gray, [160*(1-1),0,160,s_h])
        pygame.draw.rect(win,gray, [160*(2-1),0,160,s_h])
        pygame.draw.rect(win,gray, [160*(3-1),0,160,s_h])
        pygame.draw.rect(win,gray, [160*(4-1),0,160,s_h])
        pygame.draw.rect(win,gray, [160*(5-1),0,160,s_h])

        pygame.draw.rect(win,black, [160*(1-1),0,20,s_h])
        pygame.draw.rect(win,black, [160*(2-1),0,20,s_h])
        pygame.draw.rect(win,black, [160*(3-1),0,20,s_h])
        pygame.draw.rect(win,black, [160*(4-1),0,20,s_h])
        pygame.draw.rect(win,black, [160*(5-1),0,20,s_h])


        win.blit( img_red,(red_x,red_y) )
        loop_count += 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    right = True
                    left = False
                    up = False
                    down = False
                    press_count = 0
                if event.key == pygame.K_LEFT:
                    left = True
                    right = False
                    up = False
                    down = False
                    press_count = 0

                if event.key == pygame.K_UP:
                    up = True
                    down = False
                    left = False
                    right = False
                    press_count = 0

                if event.key == pygame.K_DOWN:
                    up = False
                    down = True
                    left = False
                    right = False
                    press_count = 0

                if event.key == pygame.K_SPACE:
                    right = False
                    left =  False
                    up = False
                    down  =  False
                    

            
            # For actions with multiple keys pressed
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_RIGHT] and keys[pygame.K_LALT]:
                red_x +=  sudden_jump
            if keys[pygame.K_LEFT] and keys[pygame.K_LALT]:
                red_x -= sudden_jump
            if keys[pygame.K_UP] and keys[pygame.K_LALT]:
                red_y -= sudden_jump
            if keys[pygame.K_DOWN] and keys[pygame.K_LALT]:
                red_y += sudden_jump

            #   Action for left & right click   
            if right == True:
                red_x += side_jump
            elif left == True:
                red_x -= side_jump
            else:
                red_x = red_x

            #   Action for up & down click   
            if up == True:
                red_y -= up_jump
            elif down == True:
                red_y += up_jump
            else:
                red_y = red_y
                
            # Car loop on 1st lane ( from left )
            lane1_y += car_jump
            if lane1_y > s_h+random.randint(0,400):
                lane1_y = random.randint(-800,-400)

            car_on_lane(1,img_green,lane1_y)

            # For Other lanes

            lane2_y += car_jump
            if lane2_y > s_h+random.randint(0,400):
                lane2_y = random.randint(-800,-400)

            car_on_lane(2,img_yellow,lane2_y)

            lane3_y += car_jump
            if lane3_y > s_h+random.randint(0,400):
                lane3_y = random.randint(-800,-400)
            car_on_lane(3,img_purple,lane3_y)

            lane4_y += car_jump
            if lane4_y > s_h+random.randint(0,400):
                lane4_y = random.randint(-800,-400)
            car_on_lane(4,img_green,lane4_y)

            lane5_y += car_jump
            if lane5_y > s_h+random.randint(0,400):
                lane5_y = random.randint(-800,-400)
                car_on_lane(5,img_red,lane5_y)
            
            




                
        press_count += 1

        if press_count > 20:
            right = False
            left =  False
            up = False
            down  =  False

        

        
        #   Applying boundry conditions

        if red_x < 0 :
            red_x = 0
        if red_x > s_w-100:
            red_x = s_w-100
        if red_y < 0 :
            red_y = 0
        if red_y > s_h-185:
            red_y = s_h-185

        
        #   Checking for collision



       # text_on_screen("press SPACE BAR to pause the game",210,550,200,50,black,None)
        clock.tick(fps)
        pygame.display.update()

    
    
game_loop()
quit()



