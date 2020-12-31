import pygame
import random

pygame.init()

red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)

width = 600
height = 600

dis = pygame.display.set_mode((width,height))
pygame.display.set_caption("snake game")

box = 30            

clock = pygame.time.Clock()

score_font = pygame.font.SysFont("bahnschrift", 36)
message_font = pygame.font.SysFont("comicsansms", 28)


# print(foodx,foody)

def our_snake(snake):
    for i in range(len(snake)):
        pygame.draw.rect(dis, red, [snake[i][0],snake[i][1], box, box])

def score(s):
    value = score_font.render(f"SCORE :{s} ", True, "yellow")
    dis.blit(value, (0,0))

def message(msg):
    value = message_font.render(msg, True, 'black')
    dis.blit(value, (200,300))
    

def mainloop():

    foodx = round(random.randrange(0,width-box)/box)*box
    foody = round(random.randrange(0,height-box) / box)*box

    done = False
    close = False

    x = width // 2
    y = height // 2

    dx = 0
    dy = 0

    snakes = []
    length_of_the_snake = 1

    while not done:

        while close :
            dis.fill(red)
            message("you lost , do you want to play again ?")
            score(length_of_the_snake-1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        done = True
                        close = False 
                    if event.key == pygame.K_r:
                        mainloop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dy = -box
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = box
                    dx = 0
                elif event.key == pygame.K_LEFT:
                    dx = -box
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = box
                    dy = 0

        if x >= width or x < 0 or y >= height or y < 0:
            close = True
        dis.fill(white)
        x += dx
        y += dy
        pygame.draw.rect(dis, green, (foodx, foody, box, box))
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snakes.append(snake_head)
        if len(snakes) > length_of_the_snake:
            del snakes[0]

        for i in snakes[:-1]:
            if i == snake_head:
                close = True 

        our_snake(snakes)
        score(length_of_the_snake - 1)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0,width-box)/box)*box
            foody = round(random.randrange(0,height-box)/box)*box
            length_of_the_snake += 1
            #test is vim is working

        clock.tick(10)

mainloop()
