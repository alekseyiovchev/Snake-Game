import pygame, sys
from random import randrange

RES = 500
SIZE = 30

x,y = randrange(0,RES,SIZE), randrange(0,RES,SIZE)
apple = randrange(0,RES,SIZE),randrange(0,RES,SIZE)

dirs = {'W': True, 'S': True, 'A': True, 'D': True,}

length = 1 
snake = [(x,y)]
dx,dy = 0,0
score = 0
fps = 10

pygame.init()
pygame.display.set_caption('Змейка Игра')
sc = pygame.display.set_mode([RES,RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial',14,bold=True)
font_end = pygame.font.SysFont('Arial',25,bold=True) 

while True:
    sc.fill(pygame.Color('black'))
    [(pygame.draw.rect(sc,pygame.Color('green'),(i,j,SIZE - 1,SIZE - 1))) for i,j in snake]
    pygame.draw.rect(sc,pygame.Color('red'),(*apple,SIZE,SIZE))

    render_score = font_score.render(f'CЧЕТ: {score}',1,pygame.Color('orange'))
    sc.blit(render_score, (5,5))

    x += dx * SIZE
    y += dy * SIZE
    snake.append((x,y))
    snake = snake[-length:]

    if snake[-1] == apple:
        apple = randrange(0,RES,SIZE),randrange(0,RES,SIZE)
        score += 1
        length += 1
        fps += 1

    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        while True:
            sc.fill('black')
            render_end = font_end.render('Конец Игры',1,pygame.Color('red'))
            sc.blit(render_end,(200,240))
            render_score = font_score.render(f'CЧЕТ: {score}',1,pygame.Color('orange'))
            sc.blit(render_score, (240,280))
            
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx,dy = 0, -1
        dirs= {'W': True, 'S': False, 'A': True, 'D': True,}
    
    if key[pygame.K_s] and dirs['S']:
        dx,dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True,}
    
    if key[pygame.K_a] and dirs['A']:
        dx,dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D' : False,}

    if key[pygame.K_d] and dirs['D']:
        dx,dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True,}