import pygame
from random import randint

pygame.init()

file = open('maps/{0}.txt'.format(input('map number :')),'r')

w = int( file.readline()[:-1] )
h = int( file.readline()[:-1] )

size = 10

walls = []
for line in file.readlines():
    walls.append(list(map(int,line.split())))

food_color = (255,0,0)
snake_color = (0,255,0)
wall_color = (165,42,42)
bg_color = (0,0,0)

screen = pygame.display.set_mode((w*size,h*size))

snake = [[0,20],
         [1,20]]

vx = 1
vy = 0

point = 0

while True:
    x = randint(0,w - 1)
    y = randint(0,h - 1)
    if ([x,y] not in snake) and ([x,y] not in walls):
        break
food_x = x
food_y = y

losed = False

while not losed:
    screen.fill(bg_color)
    pygame.draw.rect(screen,food_color,(food_x*size,food_y*size,size,size),0)
    for wall in walls:
        pygame.draw.rect(screen,wall_color,(wall[0]*size,wall[1]*size,size,size))
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
            if ([x,y] not in snake) and ([x,y] not in walls):
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

    if snake[0] in walls :
        print('you hit wall :-(')
        losed = True
        
    pygame.display.update()
    pygame.time.Clock().tick(20)

print('your point :',point)
pygame.quit()

file.close()
