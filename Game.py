#BRIANNA'S TEST
#BRIANNA'S TEST
#BRIANNA'S TEST
#BRIANNA'S TEST
#BRIANNA'S TEST
#BRIANNA'S TEST
import pygame
import random
pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("MailRun Game")
font = pygame.font.Font('font\Gameplay.ttf', 20)
pygame.mixer.music.load('assets\\running.mp3')
pygame.mixer.music.play()   #tells the program to play the music once it loads
def menu():
    image=pygame.image.load('assets\home.png')
    image=pygame.transform.scale(image,(640,480))
    while True:
        screen.blit(image,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(210,275) and event.pos[1] in range(182,250):#x1,x2 y1,y2
                    game()



def game():
    image = pygame.image.load('assets\level1.png')
    image = pygame.transform.scale(image, (640, 480))
    bgx = 0
    player = pygame.image.load('assets\character.png')
    player =pygame.transform.rotozoom(player,0,0.3)
    player_y= 280
    gravity = 1
    jump_count = 0
    jump =0
    jumpsound = pygame.mixer.Sound('assets\jump.mp3')
    bee = pygame.image.load('assets\\bee.png')
    bee = pygame.transform.rotozoom(bee,0,0.3)
    crate = pygame.image.load('assets\crate.png')
    crate = pygame.transform.rotozoom(crate,0,0.3)
    crate_x= 700
    bee_speed=2
    bee_x= 700
    score_value = 0
    jump_limit=0
    tolerance=10
    collision = False
    envelope = pygame.image.load('assets\envelope.png')
    envelope = pygame.transform.rotozoom(envelope, 0, 0.3)

    while True:
        screen.blit(image, (bgx-640, 0)) #these 3 lines makes the screen scroll
        screen.blit(image, (bgx, 0))
        screen.blit(image, (bgx+640, 0))
#        bgx=bgx-1 #this makes it auto scroll, which I disable so that you use arrow keys to scroll left or right.
        b_rect = screen.blit(bee, (bee_x, 330))
        c_rect = screen.blit(crate, (crate_x, 330))
        p_rect = screen.blit(player, (50, player_y))
        if bgx <= -640:
           bgx=0
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:

            if p_rect.colliderect(c_rect)==0 or player_y<280:#checks for collision between player and crate, if there is, then no movement, if player jumps so there is no collision, then continue to allow movement.

                bgx = bgx - 1 #This scrolls the screen right by subtracting it's X location value by 1
                crate_x= crate_x -1


        if keypressed[pygame.K_LEFT]:
            bgx = bgx + 1  #this scrolls the screen left by adding 1 to the x location value
            crate_x=crate_x +1


        if player_y < 280:
            player_y += gravity
        if jump == 1 and jump_limit<3:
            player_y = player_y-4
            jump_count+=1
            #print(jump_limit)
        if jump_count > 40: #these set of code prevents unlimited jumps in the air
            jump_count = 0
            jump = 0
        if player_y==280: #When player reaches ground, it resets jump limit to allow jumps again.
            jump_limit=0






#        crate_x= random.randint(300, 640)
        bee_x -= bee_speed
        if bee_x<-50:
#            crate_x=700
            bee_x = random.randint(700,820)
            bee_speed = random.randint(2,4)
            score_value+=1
        if crate_x<-50:
            crate_x = random.randint(700,820)

        #    score_value+=1
        if p_rect.colliderect(c_rect):  #This section allows player to jump on top of the crate, and jump off of it.

            if abs(c_rect.top - p_rect.bottom) < tolerance:
                gravity=0
                jump_count=0
                p_rect.bottom = 330
                if jump==1 or keypressed[pygame.K_LEFT] or keypressed[pygame.K_RIGHT]:
                    gravity=1
                    bgx = 0



        if b_rect.colliderect(p_rect):  # when the Bee collides with the player the game ends and 'return' to menu
            return


        text = font.render('Score: ' + str(score_value), True, 'white')
        screen.blit(text, (30,30))

#        else:
#            return



#        if c_rect.colliderect(p_rect):
 #          return

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
#            keypressed = pygame.key.get_pressed()
#            if keypressed[pygame.K_RIGHT]:
#                bgx = bgx - 20
#            if keypressed[pygame.K_LEFT]:
#                bgx = bgx + 20
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
#                    print("jump")
                    jump =1
                    jump_limit+=1 # allows only double jump
                    pygame.mixer.Sound.play(jumpsound)

#The following is to generate a random object that the player can collect

envelope_rect = envelope.get_rect()
envelope_width = envelope_rect.width
envelope_height = envelope_rect.height

def get_random_position():
    x = random.randint(0, 640 - envelope_width)
    y = random.randint(0, 480 - envelope_height)
    return x,y

envelope_positions = []

Spawn_Image_Event = pygame.USEREVENT+1
pygame.time.set_timer(Spawn_Image_Event, 10000)
for event in pygame.event.get():
    if event.type == Spawn_Image_Event:
        new_rect = envelope.get_rect(topleft=get_random_position)
        envelope_positions.append(new_rect)
for pos in envelope_positions:
    screen.blit(envelope, pos)



 #                   score_value+=1

#            font = pygame.font.Font('freesansbold.tff', 30)
#            text = font.render('Score: ' + str(score_value), True, 'white')
#            screen.blit(text, (700,30))

menu()


