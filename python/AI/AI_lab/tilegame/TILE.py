# import numpy as np
# import cv2
# from numpy.core.numeric import False_
# from numpy.lib.twodim_base import triu_indices_from
import pygame
import random,time

pygame.init()


class creat_tiles(pygame.sprite.Sprite):



    def tile_decor(self,img1,x1,y1,w,h,t_num):
        cropped=pygame.Surface((180,180))
        cropped.blit(img1,(10,10),(x1,y1,w,h))
        return cropped
 

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        img=pygame.image.load('tilegame\center.jpeg')
        img=pygame.transform.scale(img,(480,480))


        t1 = self.tile_decor(img,0,0,160,160,1)
        t2 = self.tile_decor(img,160,0,160,160,2)#
        t3 = self.tile_decor(img,320,0,160,160,3)
        t4 = self.tile_decor(img,0,160,160,160,4)#
        t5 = self.tile_decor(img,160,160,160,160,5)#
        t6 = self.tile_decor(img,320,160,160,160,6)#
        t7 = self.tile_decor(img,0,320,160,160,7)
        t8 = self.tile_decor(img,160,320,160,160,8)
   
        # blank tile
        t9= pygame.transform.scale(pygame.image.load('tilegame\\blacktile.png'),(180,180)) 

        self.tiles=[(t1,1),(t2,2),(t3,3),(t4,4),(t5,5),(t6,6),(t7,7),(t8,8)]
        random.shuffle(self.tiles)

        self.tiles.insert(4,(t9,9))



Tile= creat_tiles()
tiles=Tile.tiles



# display background
bg = pygame.image.load('tilegame\\bg.jpg')
bg=pygame.transform.scale(bg,(600,600))

win=pygame.image.load('tilegame\yw.png')
win=pygame.transform.scale(win,(600,600))




# Displaying Screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 650
screen= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Tiles')


#function to  print tile
def placetiles(tiles):
    position=[(15,65), (210,65) ,(405,65), (15,260),(210,260),(405,260),(15,455),(210,455),(405,455)]
    for i in range(9):
        screen.blit(tiles[i][0],position[i])
    

def isfinalstate(tiles):
    i=1
    for tile in tiles:
        if(tile[1]!=i):
            return False
        i+=1
    return True


def beep():
    soundObj = pygame.mixer.Sound('tilegame/move_effect.wav')
    soundObj.play()
   



x=y=1

run= True
while run:
    #background
    screen.blit(bg,(0,50))
    placetiles(tiles)



    # if the player reaches the final state then player wins and stop the game
    if(isfinalstate(tiles)):

        
        screen.blit(win,(0,50))
        pygame.display.update()
        pygame.time.wait(10000)
        run= False
    

    # #< ----------if key pressed then move the tile-------->
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT] and x > 0:
       
    #     tiles[3*y+x],tiles[3*y+x-1]=tiles[3*y+x-1],tiles[3*y+x]
    #     x-=1
      
    # if keys[pygame.K_RIGHT] and x < 2 :
        
    #     tiles[3*y+x],tiles[3*y+x+1]=tiles[3*y+x+1],tiles[3*y+x]
    #     x+=1
  
     
    # if keys[pygame.K_UP] and y > 0:
         
    #     tiles[3*y+x],tiles[3*y+x-3]=tiles[3*y+x-3],tiles[3*y+x]
    #     y-=1
  
    # if keys[pygame.K_DOWN] and y < 2:
        
    #     tiles[3*y+x],tiles[3*y+x+3]=tiles[3*y+x+3],tiles[3*y+x]
    #     y+=1



    
    # pygame.time.wait(100)



    
    for event in pygame.event.get():


        # using different function for above work
        if event.type==pygame.KEYDOWN:
        
            if event.key==pygame.K_LEFT  and x > 0:    
                beep()
                tiles[3*y+x],tiles[3*y+x-1]=tiles[3*y+x-1],tiles[3*y+x]
                x-=1
            
            if event.key==pygame.K_RIGHT and x < 2 :
                beep()
                tiles[3*y+x],tiles[3*y+x+1]=tiles[3*y+x+1],tiles[3*y+x]
                x+=1
        
            
            if event.key==pygame.K_UP and y > 0:
                beep()
                tiles[3*y+x],tiles[3*y+x-3]=tiles[3*y+x-3],tiles[3*y+x]
                y-=1
        
            if event.key==pygame.K_DOWN and y < 2:
                beep()
                tiles[3*y+x],tiles[3*y+x+3]=tiles[3*y+x+3],tiles[3*y+x]
                y+=1

        if event.type==pygame.QUIT:
            run=False

    pygame.display.update()