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

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("MailRun Game")
font = pygame.font.Font('font/Gameplay.ttf', 20)  # Fixed path
pygame.mixer.music.load('assets/running.mp3')  # Fixed path
pygame.mixer.music.play(-1)

def menu():
    image = pygame.image.load('assets/home.png')  # Fixed path
    image = pygame.transform.scale(image, (640, 480))
    while True:
        screen.blit(image, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 210 <= event.pos[0] <= 275 and 182 <= event.pos[1] <= 250:
                    game()



def game():
    image = pygame.image.load('assets/level1.png')  # Fixed path
    image = pygame.transform.scale(image, (640, 480))
    bgx = 0
    player = pygame.image.load('assets/character.png')  # Fixed path
    player = pygame.transform.rotozoom(player, 0, 0.3)
    player_y = 280
    gravity = 1
    jump_count = 0
    jump = 0
    jumpsound = pygame.mixer.Sound('assets/jump.mp3')  # Fixed path
    bee = pygame.image.load('assets/bee.png')  # Fixed path
    bee = pygame.transform.rotozoom(bee, 0, 0.3)
    crate = pygame.image.load('assets/crate.png')  # Fixed path
    crate = pygame.transform.rotozoom(crate, 0, 0.3)
    crate_x = 700
    bee_speed = 1
    bee_x = 700
    score_value = 0
    jump_limit = 0
    tolerance = 10
    collision = False
    envelopesound =  pygame.mixer.Sound('assets/paper.wav')

    # Envelope setup
    envelope = pygame.image.load('assets/envelope.png').convert_alpha()  # Fixed path
    envelope = pygame.transform.rotozoom(envelope, 0, 0.06)
    envelope_rect = envelope.get_rect()
    envelope_width = envelope_rect.width
    envelope_height = envelope_rect.height
    Spawn_Image_Event = pygame.USEREVENT + 1
    pygame.time.set_timer(Spawn_Image_Event, 10000)
    envelope_positions = []

    clock = pygame.time.Clock()  # Moved outside loop

    while True:
        # Handle events first
        def get_random_position(envelope_width, envelope_height):  # Moved outside, with params for clarity
            return (random.randint(0, 640 - envelope_width), random.randint(40, 280 - envelope_height))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if (jump_limit == 0 and (player_y >= 280 or gravity == 0)) or (jump_limit == 1 and gravity == 1) or p_rect.bottom==c_rect.top:
                        jump = 1
                        jump_limit += 1
                        jumpsound.play()
            if event.type == Spawn_Image_Event:
                new_rect = envelope.get_rect(topleft=get_random_position(envelope_width, envelope_height))
                envelope_positions.append(new_rect)

        # Clear screen (optional, but prevents artifacts)
        screen.fill((0, 0, 0))

        # Draw background
        screen.blit(image, (bgx - 640, 0))
        screen.blit(image, (bgx, 0))
        screen.blit(image, (bgx + 640, 0))

        # Draw objects
        b_rect = screen.blit(bee, (bee_x + bgx, 330))
#        b_rect = screen.blit(bee, (bee_x, 330))
        c_rect = screen.blit(crate, (crate_x, 330))
        p_rect = screen.blit(player, (50, player_y))

        # Background wrap
        if bgx <= -640:
            bgx = 0

        # Input handling
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            if p_rect.colliderect(c_rect) == 0 or player_y < 280:
                bgx -= 1
                crate_x -= 1
        if keypressed[pygame.K_LEFT]:
            bgx += 1
            crate_x += 1

        # Player physics
        if player_y < 280:
            player_y += gravity
        if jump == 1 and jump_limit < 3:
            player_y -= 4
            jump_count += 1
        if jump_count > 40:
            jump_count = 0
            jump = 0
        if player_y >= 280 or p_rect.bottom==c_rect.top:
            jump_limit = 0

        # Bee and crate movement
        bee_x -= bee_speed
        if bee_x < -50 -bgx:
            bee_x = 640 - bgx
            bee_speed = random.randint(2, 5)
         #   score_value += 1
        if crate_x < -50:
            crate_x = random.randint(700, 820)

        # Crate collision
        side_collision = p_rect.colliderect(c_rect) and abs(c_rect.top - p_rect.bottom) >= tolerance
        if keypressed[pygame.K_RIGHT]:
            if not side_collision:  # Only move if not hitting crate side
                bgx -= 1
                crate_x -= 1
        if keypressed[pygame.K_LEFT]:
            bgx += 1
            crate_x += 1
        if p_rect.colliderect(c_rect):
            if abs(c_rect.top - p_rect.bottom) < tolerance:
                gravity = 0
#                jump_count = 0
#                jump_limit = 0
#                jump = 0
                p_rect.bottom=c_rect.top

                # Check if player is still on crate
        if jump==1 or gravity == 0 and (p_rect.right <= c_rect.left or p_rect.left >= c_rect.right):
           gravity = 1  # Fall off if beyond crate edges


        # Bee collision (game over)
        if b_rect.colliderect(p_rect):
            # Optional: Show game over screen
            screen.fill((0, 0, 0))
            go_text = font.render('Game Over! Score: ' + str(score_value), True, (255, 0, 0))
            screen.blit(go_text, (screen.get_width() // 2 - 150, screen.get_height() // 2))
            pygame.display.update()
            pygame.time.wait(2000)
            return(menu())  # Now properly inside function

        # Envelope collisions (new: for scoring)
        for pos in envelope_positions[:]:
            screen.blit(envelope, (pos.x + bgx, pos.y))  # Offset x by bgx
            env_rect = envelope.get_rect(topleft=(pos.x + bgx, pos.y))
            if p_rect.colliderect(env_rect):
                envelopesound.play()
                envelope_positions.remove(pos)
                score_value += 1

        # Draw score
        text = font.render('Score: ' + str(score_value), True, (255, 255, 255))
        screen.blit(text, (30, 30))

        pygame.display.update()
        clock.tick(120)  # Limit to 60 FPS

# Start the game
menu()