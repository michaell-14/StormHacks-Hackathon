import pygame
from sys import exit
from Animations import PlayAnimation
import tagStuff
#from tagStuff import readTag
#from tagStuff import checkMatch

pygame.init()

#initial info and set up
width= 1000
height= 500
screen = pygame.display.set_mode((width,height)) #frame size
pygame.display.set_caption('kaykaygamegame')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf', 70)


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
sky_rect = sky_surf.get_rect(midtop = (width/2,0)) #bottom's 370

#set up animal
# firstAnimal = "Lion"
# firstFood = "Banana"
# animal_surf = PlayAnimation((f"animations/{firstAnimal}"), 250, 350)
# animal_surf1 = PlayAnimation((f"animations/{firstFood}"), 250, 350)

#playing the background music
pygame.mixer.init()
pygame.mixer.music.load('this-8-bit-music-245266.mp3')
pygame.mixer.music.play(-1)
counter = 0
counter1 = 0

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit() #quits
            exit()

    #setup the backround
    screen.blit(sky_surf, sky_rect)
    screen.blit(ground_surf,ground_rect)
    screen.blit(title_surf,title_rect)
    pygame.display.update() #updates the display surface
    
    if counter == 0 :
        input1 = tagStuff.readTag()
    counter = counter + 1

    animal_surf = PlayAnimation((f"animations/{input1}"), 200, 350)
    animal_surf.draw(screen)
    

    pygame.time.wait(1000)
   
    if counter == 0 :
        input2 = tagStuff.readTag()

    counter1 = counter1 + 1
      
    food_surf = PlayAnimation((f"animations/{input2}"), 800, 370)
    food_surf.draw(screen)



    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        for sprite in animal_surf:
            sprite.rect.x -= 50
            pygame.time.wait(300)
            pygame.mixer.Sound('cartoon-jump.mp3').play()


    if key[pygame.K_RIGHT]:
        for sprite in animal_surf:
            sprite.rect.x += 50
            pygame.time.wait(300)
            pygame.mixer.Sound('cartoon-jump.mp3').play()



    for sprite in animal_surf:
        for sprite1 in food_surf:
            if sprite.rect.colliderect(sprite1.rect):
                print("Collision detected!")
                collision_detected = True
                break

    animal_surf.update()
    food_surf.update()
    
    clock.tick(60) #while look shouldnt run faster then 60x per second
