import pygame,sys,random
pygame.init()
screen=pygame.display.set_mode((640,480)) 
snake=[100,100]
snake_speed=5  
food=[300,300]
food_spawn=True
score=0
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()  
    if food_spawn:
       food = [random.randint(0,590),random.randint(0,440)]
       food_spawn=False
    screen.fill((0,0,0)) 
    for position in snake:
       pygame.draw.rect(screen,(0,255,0), pygame.Rect(position[0],position[1],10,10))
       pygame.draw.rect(screen,(255,0,0), pygame.Rect(food[0],food[1],10,10))
       snake.insert(0,[snake[0][0] + snake_speed, snake[0][1]]) 
    del snake[-1]
    if snake[0] == food:
       food_spawn=True
       score +=1      
    pygame.display.update()