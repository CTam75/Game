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
pygame.mixer.music.play()
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


    while True:
        screen.blit(image, (bgx-640, 0)) #these 3 lines makes the screen scroll
        screen.blit(image, (bgx, 0))
        screen.blit(image, (bgx+640, 0))
#        bgx=bgx-1
        b_rect = screen.blit(bee, (bee_x, 330))
        c_rect = screen.blit(crate, (crate_x, 330))
        p_rect = screen.blit(player, (50, player_y))
        if bgx <= -640:
           bgx=0
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:

            if p_rect.colliderect(c_rect)==0 or player_y<280:#checks for collision between player and crate, if there is, then no movement, if player jumps so there is no collision, then continue to allow movement.

                bgx = bgx - 1
                crate_x= crate_x -1


        if keypressed[pygame.K_LEFT]:
            bgx = bgx + 1
            crate_x=crate_x +1


        if player_y < 280:
            player_y += gravity
        if jump == 1 and jump_limit<3:
            player_y = player_y-4
            jump_count+=1
            #print(jump_limit)
        if jump_count > 40:
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
 #           print(c_rect)
            if abs(c_rect.top - p_rect.bottom) < tolerance:
                gravity=0
                jump_count=0
                p_rect.bottom = 330
            if jump==1:
                gravity=1
#        if p_rect.colliderect(c_rect):
#            if abs(c_rect.left - p_rect.right) < tolerance:
 #               bgx = 0



        if b_rect.colliderect(p_rect):
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



 #                   score_value+=1

#            font = pygame.font.Font('freesansbold.tff', 30)
#            text = font.render('Score: ' + str(score_value), True, 'white')
#            screen.blit(text, (700,30))

menu()


