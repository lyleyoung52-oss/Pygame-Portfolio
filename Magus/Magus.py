import pygame, pickle, shelve

pygame.init()

clock = pygame.time.Clock()

Background = pygame.image.load("magus_background.jpg")
Norm = pygame.image.load("Magus.png")
Up = pygame.image.load("Magus_U.png")
Down = pygame.image.load("Magus_D.png")
Left = pygame.image.load("Magus_L.png")
Right = pygame.image.load("Magus_R.png")
Norm_x_pos = 270 
Norm_y_pos = 210 

#Background2 = pygame.image.load("magus_background2.jpg")
#size = (600, 420)
#Background2.get_size()

position_x = []
position_y = " "

#Dead_Zones = [(range(11, 14), 159), (range(32, 134), 126), (range(142, 394), 69), (range(407, 502), 142), (range(522, 580), 162)]

#Dead_Zones_y = 
#Dead_Zones_x = [11, 14, 32, 134, 142, 394, 407, 502, 522, 580]

#ranges_1 = [range(11, 13), range(32, 134), range(142, 394), range(407, 502), range(522, 580)]
#ranges_2 = [159, 126, 69, 142, 162]

#Dead_Zones = [(ranges_1[0],ranges_2[0]), (ranges_1[1],ranges_2[1]), (ranges_1[2],ranges_2[2]), (ranges_1[3],ranges_2[3]), (ranges_1[4],ranges_2[4])]

Background_rect = Background.get_rect()
size = (600, 420)
Background.get_size()
screen = pygame.display.set_mode(size)

#loud music and sound fx
music = pygame.mixer.Sound('mag.mp3')

music.play()

X2_pos = Norm_x_pos
Y2_pos = Norm_y_pos

program_running = True
print("""
        The Magus Experience.
        
        Ever wanted to play Chrono Trigger without the hassle of
        having to play as any of the less cool characters? And perhaps you 
        don't want to take Magus out on an adventure, maybe you just want to 
        chill in his pad? Well, at last, now you can with: The Magus Experience!

        """)

while program_running:
    clock.tick(60)
    screen.blit(Background, Background_rect)
    count = 0
    
    
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_running = False
    
    keys = pygame.key.get_pressed()

    def draw_image(screen, image, x, y):
        r = image.get_rect()
        r.x = x
        r.y = y
        screen.blit(image, r)
        
        
    if keys[pygame.K_ESCAPE]:
        program_running = False  
    elif keys[pygame.K_DOWN]:
        Norm_y_pos = Norm_y_pos + 1 
        draw_image(screen, Down, Norm_x_pos, Norm_y_pos)
    elif keys[pygame.K_UP]:
        Norm_y_pos = Norm_y_pos - 1
        draw_image(screen, Up, Norm_x_pos, Norm_y_pos)        
    elif keys[pygame.K_RIGHT] or (keys[pygame.K_UP] and keys[pygame.K_RIGHT]):
        #print(Norm_x_pos, Norm_y_pos)
        Norm_x_pos = Norm_x_pos + 1
        draw_image(screen, Right, Norm_x_pos, Norm_y_pos)
    elif keys[pygame.K_LEFT] or (keys[pygame.K_DOWN] and keys[pygame.K_LEFT]):
        #print(Norm_x_pos, Norm_y_pos)
        Norm_x_pos = Norm_x_pos - 1
        draw_image(screen, Left, Norm_x_pos, Norm_y_pos)
        #print(Norm_y_pos)
    else:
        Norm_rectangle = Norm.get_rect()
        Norm_rectangle.x = Norm_x_pos
        Norm_rectangle.y = Norm_y_pos
        screen.blit(Norm, Norm_rectangle)
    
    #if #(Norm_x_pos in range(Dead_Zones_X[1][0], Dead_Zones_X[1][1])) and (Norm_y_pos < int(Dead_Zones_Y[0])):
        #count += 1
        #Norm_x_pos += count
        #print("Top one here:", Norm_x_pos, Norm_y_pos)
    #if #(Norm_x_pos in range(Dead_Zones_X[0][0], Dead_Zones_X[0][1])) and (Norm_y_pos < int(Dead_Zones_Y[3])):
        #count += 1
        #Norm_x_pos += count
        #print("Bottom one here:", Norm_x_pos, Norm_y_pos)
    if Norm_x_pos < -10 or Norm_x_pos > 586: 
        Norm_x_pos = Norm_x_pos % Norm_x_pos 
    if Norm_y_pos < -10 or Norm_y_pos > 389:
        Norm_y_pos = Norm_y_pos % Norm_y_pos
    #if Norm_y_pos > 389:        
        #count += -1
        #Norm_y_pos = 389 % Norm_y_pos
    #if Norm_x_pos > 586:
        #count -= 1
        #Norm_x_pos = 586 % Norm_x_pos
           
            
                        
    
        
    pygame.display.flip()
    pygame.display.update()

print("Goodbye")
pygame.quit()
