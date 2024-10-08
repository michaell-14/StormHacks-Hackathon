import pygame
from sys import exit
from Animations import PlayAnimation
import tagStuff
from tagStuff import checkMatch
import time
import sys

pygame.init()

#initial info and set up
width= 1000
height= 500
screen = pygame.display.set_mode((width,height)) #frame size
pygame.display.set_caption('Plate Pets')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf', 70)

animal = ''
food = ''
#title card
text = "Plate Pets"
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

animal_tag = tagStuff.readTag()

if animal_tag not in ["lion", "bunny", "monkey"]:
    sys.stderr.write('Invalid animal tag\n')

animal_surf = PlayAnimation((f"animations/{animal_tag}"), 250, 350)
animal_happy_surf = PlayAnimation((f"animations/{animal_tag}_h"), 700, 350)
animal_sad_surf = PlayAnimation(f"animations/{animal_tag}_s", 700, 350)

time.sleep(2)

food_tag = tagStuff.readTag()

if food_tag not in ["banana", "meat", "carrot"]:
    sys.stderr.write('Invalid food tag\n')

food_surf = PlayAnimation((f"animations/{food_tag}"), 800, 350)
eating_food_surf = PlayAnimation(f"animations/{food_tag}_eat", 800, 350)

pygame.mixer.init()
pygame.mixer.music.load('this-8-bit-music-245266.mp3')
pygame.mixer.music.play(-1)
eaten = False
sad = False

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit() #quits
            exit()

    key = pygame.key.get_pressed()
    #setup the backround
    screen.blit(sky_surf, sky_rect)
    screen.blit(ground_surf,ground_rect)
    screen.blit(title_surf,title_rect)
   
    if (not eaten and not sad):
        animal_surf.draw(screen)
    if eaten:
        animal_happy_surf.draw(screen)
    if (not eaten and sad):
        animal_sad_surf.draw(screen)
        

    if (not eaten):   
        food_surf.draw(screen)
    if eaten:
        eating_food_surf.draw(screen)
        

    if key[pygame.K_LEFT]:
        for sprite in animal_surf:
            sprite.rect.x -= 50
            pygame.time.wait(300)
            
    if key[pygame.K_RIGHT]:
 
        for sprite in animal_surf:
            sprite.rect.x += 50
            pygame.time.wait(300)
            
    for sprite in animal_surf:
        for sprite1 in food_surf:
            if (sprite.rect.colliderect(sprite1.rect)):
                #print("Collision detected!")                       
                check = checkMatch(animal_tag, food_tag)
                if check == True:
                    eaten = True
                elif check == False:
                    sad = True

           
   

    animal_surf.update()
    food_surf.update()
    eating_food_surf.update()
    animal_happy_surf.update()
    animal_sad_surf.update()
    pygame.display.update() #updates the display surface
    clock.tick(30) #while look shouldnt run faster then 60x per second
