import pygame
from sys import exit

pygame.init()

width= 800
height= 400
screen = pygame.display.set_mode((width,height)) #frame size
pygame.display.set_caption('kaykaygamegame')
clock = pygame.time.Clock()


ground_surf = pygame.image.load('animations/ground.png').convert_alpha()
ground_surf = pygame.transform.scale(ground_surf, (800, ground_surf.get_height() * 800 // ground_surf.get_width()))

ground_rect = ground_surf.get_rect(center = (400,200))


#sky_surf


while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit() #quits
            exit()

    screen.blit(ground_surf,ground_rect)
    


    

    pygame.display.update() #updates the display surface
    clock.tick(60) #while look shouldnt run faster then 60x per second
