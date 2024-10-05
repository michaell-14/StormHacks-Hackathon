import pygame, sys

class SpriteSheetAnimation(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, frame_width, frame_height, pos_x, pos_y):
        super().__init__()
        self.frames = []

        for y in range(0, sprite_sheet.get_height(), frame_height):
            for x in range(0, sprite_sheet.get_width(), frame_width):
                frame = sprite_sheet.subsurface(x, y, frame_width, frame_height)
                scaled_frame = pygame.transform.scale(frame, (400,400))
                self.frames.append(scaled_frame)

        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

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
    screen = pygame.display.set_mode((800,600))

    clock = pygame.time.Clock()
    sprite_sheet = pygame.image.load(animation_type)
    
    frame_width = 50
    frame_height = 50

    animated_sprite = SpriteSheetAnimation(sprite_sheet, frame_width, frame_height, 400, 300)
    all_sprites = pygame.sprite.Group(animated_sprite)

    running = True

    while(running):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False

        all_sprites.update()
        screen.fill((120,120,120))
       
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(5)
