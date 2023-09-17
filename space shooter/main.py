import pygame
import random
from pygame import mixer




pygame.init()
window = pygame.display.set_mode((500, 500))

background = pygame.image.load('galaxy.jpg')
background = pygame.transform.scale(background, (500, 500))
window.blit(background, (0, 0))
clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load('space.ogg')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()

fire = pygame.mixer.Sound('fire.mp3')
fire.set_volume(0.3)





class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if self.rect.x > -30:
                self.rect.x -= self.speed
        if keys[pygame.K_d]:
            if self.rect.x < 450:
                self.rect.x += self.speed



lost = 0
score = 0

class Enemy(GameSprite):
    def update(self):
        self.rect.y = self.rect.y + self.speed
        global lost
        
        if self.rect.y >= 500:
            self.rect.y = -50
            self.rect.x = random.randint(0, 450)
            lost += 1
            lost_sound = pygame.mixer.Sound('nooo.mp3')
            lost_sound.set_volume(0.3)
            lost_sound.play()
    
class bullet(GameSprite):
    def update(self):
        self.rect.y -=self.speed
        if self.rect.y < 0:
            self.kill()
            
            
            
 
lostLabel = pygame.image
        
bullets = pygame.sprite.Group()

hero = Player('rocket.png', 5, 400, 10, 80, 100)
enemies = pygame.sprite.Group()
for i in range(5):
    enemy1 = Enemy('ufo.png', random.randint(0, 450), random.randint(-250, -50), random.randint(1,6), 80, 50)
    enemies.add(enemy1)

font2 = pygame.font.Font(None, 36)
font3 = pygame.font.Font(None, 88)
text_win = font2.render('YOU WIN!', True, (0,255,0))
text_lose = font2.render('YOU LOSE!', True, (255,0,0))



game = True
while game:
    window.blit(background, (0, 0))
    hero.reset()
    hero.update()
    
    enemies.draw(window)
    enemies.update()
    
    bullets.draw(window)
    bullets.update()
    
    

    text = font2.render("Збито: " + str(score), 1, (255, 255, 255))
    window.blit(text, (10, 20))

    text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
    window.blit(text_lose, (10, 50))
    
    if score >= 10:
        window.blit("text_win", (110, 200))
    elif lost > 3: 
        score >= 10
        window.blit("text_lose", (110, 200))
    else:  
        enemies.update()
        hero.update()
        bullets.update()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit()

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                b1 = bullet('bullet.png', hero.rect.centerx-7, hero.rect.y, 20, 15, 20)
                bullets.add(b1)
            
    if pygame.sprite.groupcollide(bullets, enemies, True, True):
        score+=  1
        enemy1 = Enemy('ufo.png', random.randint(0, 450), random.randint(-250, -50), random.randint(1,6), 80, 50)
        enemies.add(enemy1)
    

    pygame.display.update()
    clock.tick(30)