from pygame import *
from random import randint


win_width = 900
win_height = 500
life = 100
lost =0 
score = 0
font.init()
font2 = font.SysFont('Arial', 36)
window = display.set_mode((win_width, win_height))
display.set_caption("Shooter-game")
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))


class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

class Enemy(Gamesprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width- 80)
            self.rect.y = 0
            lost = lost + 1

class Bullet(Gamesprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()



    

        
        
ing_enemy = 'ufo.png'
player = Player('rocket.png', 200, 200, 65,65, 10)

monsters = sprite.Group()
for i in range(1, 16):
    monster = Enemy(ing_enemy, randint(80, win_width - 80), -40, 65,65, randint(1, 15))
    monsters.add(monster)

asteroids = sprite.Group()  
for i in range(1, 5):
    asteroid = Enemy('asteroid.png', randint(80, win_width - 80), -40, 65,65, randint(1, 15))
    asteroids.add(asteroid)

bullets = sprite.Group()


finish = False

game = True
clock = time.Clock()
FPS = 60

# font.init()
# font = font.Font(None, 70)
# win = font.render("YOU WIN!", True, (255, 215, 0))
# lose = font.render("YOU LOSE!", True, (180, 100, 0))



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                print("xxx")
                player.fire()
                




    if finish != True:
        player.update()



        
            
        
        window.blit(background,(0, 0))
        text = font2.render("Score: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))
        text_lose = font2.render("Missed: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        text_life = font2.render("lives: " + str(life), 1, (255, 255, 255))
        window.blit(text_life, (10, 80))
        player.reset()
        # monster.update()
        # monster.reset()
        # final.reset()
        # wall_1.draw_wall()
        # wall_2.draw_wall()
        # wall_3.draw_wall()
        # wall_4.draw_wall()


        # if sprite.collide_rect(player, monster) or\
        # sprite.collide_rect(player, wall_1) or\
        # sprite.collide_rect(player, wall_2) or\
        # sprite.collide_rect(player, wall_3):
            
        #     window.blit(lose, (200, 200))
        #     finish = True
            

        # if sprite.collide_rect(player, final):
            
        #     window.blit(win, (200, 200))
        #     finish = True
        
        monsters.update()
        monsters.draw(window)

        asteroids.update()
        asteroids.draw(window)


        bullets.update()
        bullets.draw(window)


        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score = score + 1
            monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

        if sprite.spritecollide(player, monsters, False):
            sprite.spritecollide(player, monsters, True)
            life = life -1
            monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

        if sprite.spritecollide(player, asteroids, False) :
            sprite.spritecollide(player, asteroids, True)
            life = life -1
            asteroid = Enemy('asteroid.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            asteroids.add(asteroid)
       

    

        


        


        






        







    
    display.update()
    clock.tick(FPS)
