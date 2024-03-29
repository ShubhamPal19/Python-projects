import pygame
pygame.init()

class Soldier(pygame.sprite.Sprite):

    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('C:/Users/SHUBHAM/Desktop/datascience/python/python/pygame/Shooter_game_using_python/Game/img/player/Idle/0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH*0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Shooter')


player=Soldier(200,200,0.1)

run = True
while run:

    screen.blit(player.image,player.rect)

    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()
