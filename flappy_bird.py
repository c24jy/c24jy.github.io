import pygame
import sys
import random
import os

DISPLAY_SIZE = [288, 512]

pygame.init()

screen = pygame.display.set_mode(DISPLAY_SIZE)
clock = pygame.time.Clock()

bg_surface = pygame.image.load("assets/background-day.png")
floor_surface = pygame.image.load("assets/base.png")
bird_surface = pygame.image.load("assets/yellow.png")
bird_surface = pygame.transform.scale(bird_surface, [49, 35])
bird_rect = bird_surface.get_rect(center=(40, 206))
pipe_surface = pygame.image.load("assets/pipe-green.png")
flipped_pipe_surface = pygame.image.load("assets/pipe-upside-down.png")
message_surface = pygame.image.load("assets/message.png")

score_font = pygame.font.Font("assets/04B_19 (1).TTF", 30) #font size
pipes = [] #this will store the pipe rectangles

time_to_spawn_pipe = pygame.USEREVENT
#every 1500 ms, pygame will know it's time to spawn a pipe
pygame.time.set_timer(time_to_spawn_pipe, 1500)

time_to_increase_score = pygame.USEREVENT
#every 1500 ms, pygame will know it's time to increase the score
pygame.time.set_timer(time_to_increase_score, 2500)

floor_x_coord = 0
bird_y_coord = 206
bird_acceleration = 2
score = 0

dead = True

def bird_collided():
    for pipe in pipes:
        if bird_rect.colliderect(pipe.move(0, -500)) or bird_rect.colliderect(pipe) or bird_rect.centery < 0 or bird_rect.centery > 400:
            return True
    return False



# x in this function is the x coor of the floor
def draw_floor():
    screen.blit(floor_surface, [floor_x_coord, 450])
    screen.blit(floor_surface, [floor_x_coord + 336, 450])

def spawn_pipe():
    height = random.choice([550, 475,  400])
    new_pipe_rect = pipe_surface.get_rect(center=(500,height))
    pipes.append(new_pipe_rect)

def draw_pipes():
    for rect in pipes:
        screen.blit(pipe_surface, rect)
        screen.blit(flipped_pipe_surface, rect.move(0, -500))

def move_pipes(): #shift all pipes to the left a bit
    for pipe in pipes:
        pipe.centerx -= 3

def only_on_screen(old_pipes):
    new_pipes = []
    for pipe in old_pipes:
        if pipe.right > 0:
            new_pipes.append(pipe)
    return new_pipes

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_acceleration = -5
                if dead:
                    dead = False

        if event.type == time_to_spawn_pipe and not dead:
            spawn_pipe()

        if event.type == time_to_increase_score and not dead:
            os.popen("afplay sound/sfx_point.wav")
            score += 1

    if bird_collided():
        pipes.clear()
        bird_rect = bird_surface.get_rect(center=(40, 206))
        dead = True
        score = 0

    screen.blit(bg_surface, [0, 0])

    if dead:
        #show "get ready screen"
        screen.blit(message_surface, [50, 100])

        floor_x_coord -= 1

        if floor_x_coord + 336 <= 0:
            floor_x_coord = 0
            print("floor reset!")

    else:
        screen.blit(bird_surface, bird_rect)
        bird_rect.centery += bird_acceleration
        bird_acceleration += 0.2
        draw_pipes()

        move_pipes()
        pipes = only_on_screen(pipes) #ensure pipes list only contain pipes on screen
        #pipes is now only on screen pipes

    draw_floor()

    floor_x_coord -= 1

    if floor_x_coord + 336 <= 0:
        floor_x_coord = 0
        print("floor reset!")

    score_surface = score_font.render("Score: " + str(score), False, (255, 255, 255))
    screen.blit(score_surface, [65, 20])

    pygame.display.update()
    clock.tick(120)


