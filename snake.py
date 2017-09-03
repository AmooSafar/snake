import pygame
from random import randint

pygame.init()

w = 40
h = 40
size = 10

food_color = (255,0,0)
snake_color = (0,255,0)
bg_color = (0,0,0)

screen = pygame.display.set_mode((w*size,h*size))

snake = [[0,20],
         [1,20]]

vx = 1
vy = 0

point = 0

food_x = 20
food_y = 20

losed = False

while not losed:
    screen.fill(bg_color)
    pygame.draw.rect(screen,food_color,(food_x*size,food_y*size,size,size),0)
    for body in snake:
        pygame.draw.rect(screen,snake_color,(body[0]*size,body[1]*size,size,size),0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            losed = True
            print('you left the game :-(')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and vx != 0:
                vx = 0
                vy = -1
            if event.key == pygame.K_s and vx != 0:
                vx = 0
                vy = 1
            if event.key == pygame.K_a and vy != 0:
                vx = -1
                vy = 0
            if event.key == pygame.K_d and vy != 0:
                vx = 1
                vy = 0

    if [food_x,food_y] == snake[0]:
        point += 1
        while True:
            x = randint(0,w - 1)
            y = randint(0,h - 1)
            if [x,y] not in snake:
                break
        food_x = x
        food_y = y
        
    else:
        snake.pop()

    snake.insert(0,[snake[0][0]+vx,snake[0][1]+vy])

    if snake[0] in snake[1:]:
        print('you eat your body :-(')
        losed = True
        
    if snake[0][0] < 0 or snake[0][0] > w:
        print('you hit wall :-(')
        losed = True
        
    if snake[0][1] < 0 or snake[0][1] > h:
        print('you hit wall :-(')
        losed = True

    pygame.display.update()
    pygame.time.Clock().tick(10)


print('your point :',point)
pygame.quit()
