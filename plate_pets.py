import pygame
from sys import exit
from Animations import PlayAnimation

pygame.init()

#initial info and set up
width= 1000
height= 500
screen = pygame.display.set_mode((width,height)) #frame size
pygame.display.set_caption('kaykaygamegame')
clock = pygame.time.Clock()
test_font = pygame.font.Font('animations/Pixeltype.ttf', 70)


#title card
text = "special kaykay game game"
title_surf = test_font.render(text, False, 'Black' )
title_rect = title_surf.get_rect(midtop = (width/2,50))

#making ground surface
ground_surf = pygame.image.load('animations/ground.png').convert_alpha()
ground_surf = pygame.transform.scale(ground_surf, (width, ground_surf.get_height() * width // ground_surf.get_width()))
ground_rect = ground_surf.get_rect(midbottom = (width/2,height)) #top of grass is around 310

#making sky surfce
sky_surf = pygame.image.load('animations/sky.png').convert_alpha()
sky_surf = pygame.transform.scale(sky_surf, (width, sky_surf.get_height() * width // sky_surf.get_width()))
sky_rect = sky_surf.get_rect(midtop = (width/2,0)) #bottom s 370

#set up animal 
animal_size = 100
animal_surf = PlayAnimation("animations/Lion")

#animal_surf = pygame.transform.scale(animal_surf, (animal_size,animal_surf.get_height()*animal_size // animal_surf.get_width()))
#animal_rect = animal_surf.get_rect(midbottom = (250, 350))


while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit() #quits
            exit()


    #setup the backround
    screen.blit(sky_surf, sky_rect)
    screen.blit(ground_surf,ground_rect)
    screen.blit(title_surf,title_rect)
    

    #put animal 
    #screen.blit(animal_surf)
    animal_surf.update()
    animal_surf.draw(screen)

    #print(ground_rect.top)
    #print(sky_rect.bottom)

    animal_surf.update()
    pygame.display.update() #updates the display surface
    clock.tick(60) #while look shouldnt run faster then 60x per second
