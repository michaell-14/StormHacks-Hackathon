import pygame, sys

class SpriteSheetAnimation(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, frame_width, frame_height, pos_x, pos_y):
        super().__init__()
        self.frames = []

        for y in range(0, sprite_sheet.get_height(), frame_height):
            for x in range(0, sprite_sheet.get_width(), frame_width):
                frame = sprite_sheet.subsurface(x, y, frame_width, frame_height)
                scaled_frame = pygame.transform.scale(frame, (200, 172))
                self.frames.append(scaled_frame)

        self.index = 0
        self.image = self.frames[self.index]
        
        self.rect = self.image.get_rect(midbottom = (pos_x, pos_y))
        self.flip_delay = 500  # Time in milliseconds between frames
        self.last_flip_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_flip_time > self.flip_delay:
            self.index = (self.index + 1) % len(self.frames)
            self.image = self.frames[self.index]
            self.last_flip_time = current_time

    


def PlayAnimation(specified_animation, pos_x, pos_y):
    animation_type = f"{specified_animation}.png"
  
    sprite_sheet = pygame.image.load(animation_type)
    

    frame_width = 50
    frame_height = int(sprite_sheet.get_height())

    animated_sprite = SpriteSheetAnimation(sprite_sheet, frame_width, frame_height, pos_x, pos_y)
    all_sprites = pygame.sprite.Group(animated_sprite)

    return all_sprites


