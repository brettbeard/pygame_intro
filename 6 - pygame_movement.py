import pygame

#define constants
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
speed = [2, 2]

pygame.init()  # start pygame

# create a display screen: 400x400 pixels
size = width, height = 400, 400
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pygame movement")

done = False #we're not done displaying

# draw the background
screen.fill(WHITE)

ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

loop_count = 0
while not done:

    for event in pygame.event.get(): #check the events list
        if event.type == pygame.QUIT: #if the user clicks the X
            done = True #now we're done displaying

    if loop_count % 5000 == 0 :
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(BLACK)
        screen.blit(ball, ballrect)
        pygame.display.flip()

    loop_count = loop_count + 1


    # update
    #pygame.display.update()

pygame.quit()