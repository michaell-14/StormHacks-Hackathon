import pygame, sys

class SpriteSheetAnimation(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, frame_width, frame_height):
        super().__init__()
        self.frames = []

        for y in range(0, sprite_sheet.get_height(), frame_height):
            for x in range(0, sprite_sheet.get_width(), frame_width):
                frame = sprite_sheet.subsurface(x, y, frame_width, frame_height)
               
                self.frames.append(frame)

        self.index = 0
        self.image = self.frames[self.index]
        
        self.rect = self.image.get_rect(midbottom = (250, 350))
        self.flip_delay = 100  # Time in milliseconds between frames
        self.last_flip_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_flip_time > self.flip_delay:
            self.index = (self.index + 1) % len(self.frames)
            self.image = self.frames[self.index]
            self.last_flip_time = current_time

def PlayAnimation(specified_animation):
    animation_type = f"{specified_animation}.png"
  
    sprite_sheet = pygame.image.load(animation_type)
    

    frame_width = int(sprite_sheet.get_width() / 2)
    frame_height = int(sprite_sheet.get_height())

    animated_sprite = SpriteSheetAnimation(sprite_sheet, frame_width, frame_height)
    all_sprites = pygame.sprite.Group(animated_sprite)
    return all_sprites

    #running = True

    #while(running):
        #for event in pygame.event.get():
            #if (event.type == pygame.QUIT):
                #running = False

        #all_sprites.update()
        #screen.fill((120,120,120))
       
        #all_sprites.draw(screen)
        #pygame.display.flip()
        #clock.tick(5)
