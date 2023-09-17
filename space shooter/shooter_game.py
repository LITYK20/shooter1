import pygame

pygame.init()
window = pygame.display.set_mode((500, 500))

background = pygame.image.load('galaxy.jpg')
background = pygame.transform.scale(background, (500, 500))
window.blit(background, (0, 0))
clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load('space.ogg')
pygame.mixer.music.set_volume(0.3)
# pygame.mixer.music.play()

fire = pygame.mixer.Sound('fire.ogg')
fire.set_volume(0.3)
# kick.play()


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed

        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed


class Enemy(GameSprite):
    def update(self):
        ...



game = True
while game:
    window.blit(background, (0, 0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit()

    pygame.display.update()
    clock.tick(60)
