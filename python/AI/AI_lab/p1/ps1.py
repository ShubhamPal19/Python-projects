import pygame



pygame.init()
SCREEN_HEIGHT=600
SCREEN_WIDTH=600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


x = 30
y = 30
rect_size=50
is_blue = False
run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
    
        if event.type== pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
    
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and y>0: y -=0.5
    elif key[pygame.K_DOWN] and y<SCREEN_HEIGHT-rect_size: y +=0.5
    elif key[pygame.K_LEFT] and x>0: x -=0.5
    elif key[pygame.K_RIGHT] and x< SCREEN_WIDTH-rect_size : x +=0.5
    

    if is_blue:
        color = (0,128,255)
    
    else:
        color = (255,100,0)
    
    pygame.draw.rect(screen,color,pygame.Rect(int(x),int(y),rect_size,rect_size))
    # pygame.display.update()
    pygame.display.flip()