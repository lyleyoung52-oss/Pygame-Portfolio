import pygame, random

pygame.init()
time1 = 0
WIDTH, HEIGHT = 1000, 650
grey = (128, 128, 128)
black = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("bouncing ball!")
fps = 80
screen.fill(grey)
sfx = pygame.mixer.Sound('clang.wav')
ball_speed = [3, 3]
Norm = pygame.image.load("Magus.png")
Up = pygame.image.load("Magus_U.png")
Down = pygame.image.load("Magus_D.png")
Left = pygame.image.load("Magus_L.png")
Right = pygame.image.load("Magus_R.png")
Norm_x_pos = 63 
Norm_y_pos = 543
position_x = []
position_y = " "
X2_pos = Norm_x_pos
Y2_pos = Norm_y_pos
music = pygame.mixer.Sound('Anaconda.mp3')
music.set_volume(0.2)
music.play(-1, 0)

#define a ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("ball.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        global Ball_1
        Ball_1 = self.rect
        
    #move ball
    def update(self, speed, w, h):
        self.rect = self.rect.move(speed)
        if self.rect.left < 0 or self.rect.right > w:
            ball_speed[0] = -ball_speed[0]
        if self.rect.top < 0 or self.rect.bottom > h:
            ball_speed[1] = -ball_speed[1]

    def collision(self):
        if self.rect.collidepoint(self.rect.topleft or self.rect.topright):
            ball_speed[0] *= -1 
            sfx.play()
        elif self.rect.collidepoint(self.rect.bottomleft or self.rect.bottomright):
            ball_speed[0] *= -1 
            sfx.play()
        else:
            ball_speed[1] *= -1
            sfx.play()

#Define a crate class
class Crate(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        #define our image
        self.image = pygame.image.load("crate1.png")
        #get rect for crate
        self.rect = self.image.get_rect()
        #position the image
        self.rect.topleft = (x,y)
        global Crate_1
        Crate_1 = self.rect

    def remove_crate(self):
        self.kill()

#create Magus Sprite
class Magus(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Magus.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    #move Magus
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.rect.y = self.rect.y + 1 
            self.image = pygame.image.load("Magus_D.png")
        elif keys[pygame.K_UP]:
            self.rect.y = self.rect.y - 1
            self.image = pygame.image.load("Magus_U.png")
        elif keys[pygame.K_RIGHT] or (keys[pygame.K_UP] and keys[pygame.K_RIGHT]):
            self.rect.x = self.rect.x + 1
            self.image = pygame.image.load("Magus_R.png")
        elif keys[pygame.K_LEFT] or (keys[pygame.K_DOWN] and keys[pygame.K_LEFT]):
            self.rect.x = self.rect.x - 1
            self.image = pygame.image.load("Magus_L.png")
        else:
            self.image = pygame.image.load("Magus.png")

    def stop(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.rect.y = self.rect.y - 2 
            self.image = pygame.image.load("Magus_D.png")
        elif keys[pygame.K_UP]:
            self.rect.y = self.rect.y + 2
            self.image = pygame.image.load("Magus_U.png")     
        elif keys[pygame.K_RIGHT] or (keys[pygame.K_UP] and keys[pygame.K_RIGHT]):
            self.rect.x = self.rect.x - 2
            self.image = pygame.image.load("Magus_R.png")
        elif keys[pygame.K_LEFT] or (keys[pygame.K_DOWN] and keys[pygame.K_LEFT]):
            self.rect.x = self.rect.x + 2
            self.image = pygame.image.load("Magus_L.png")

    def set_boundry(self, w, h):
        if self.rect.left < 0 or self.rect.right > WIDTH:
            Magus.stop(self)
        elif self.rect.top < 0 or self.rect.bottom > HEIGHT:
            Magus.stop(self)
        

def timer_update():
    global time1, time2
    time1 += 1
    time2 = int(time1 / 80)

#create a crate group
Crate_group = pygame.sprite.Group()
crates_list = []

#create ball
ball_group = pygame.sprite.Group()
ball_sprite = Ball(0, 0)
ball_group.add(ball_sprite)

#Create Magus
Sprite_group = pygame.sprite.Group()
Magus_sprite = Magus(Norm_x_pos, Norm_y_pos)
Sprite_group.add(Magus_sprite)

for i in range(7):
    crates = Crate(random.randrange(0, WIDTH), random.randrange(0, HEIGHT))
    crates_list.append(crates.rect[0:4])
    Crate_group.add(crates)
    crate_sprite = crates_list[i]

program_running = True

print("""Avoid the ball for as long as possible!

          Use the crates for cover!""")
while program_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill(grey)
    #draw magus
    Sprite_group.draw(screen)
    Sprite_group.update()
    timer_update()
    #Draw crates
    Crate_group.draw(screen)
    #draw ball
    ball_group.draw(screen)
    ball_group.update(ball_speed, WIDTH, HEIGHT)
    Magus.set_boundry(Magus_sprite, WIDTH, HEIGHT)
    if pygame.sprite.spritecollide(ball_sprite, Crate_group, False):
        Ball.collision(ball_sprite)
        if Ball_1.colliderect(Crate_1):
            print(Crate_1)        
        #Crate.remove_crate(Crate_group)
    elif pygame.sprite.spritecollide(Magus_sprite, Crate_group, False):
        Magus.stop(Magus_sprite)
    elif pygame.sprite.spritecollide(ball_sprite, Sprite_group, False):
        program_running = False
        print("Game Over, you lasted ", time2, " seconds")
        pygame.quit()

    pygame.display.flip()
    clock.tick(fps)
