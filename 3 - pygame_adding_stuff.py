import pygame

#define constants
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()  # start pygame

# create a display screen: 400x400 pixels
screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption("Brett's game")

done = False #we're not done displaying

while not done:

    for event in pygame.event.get(): #check the events list
        if event.type == pygame.QUIT: #if the user clicks the X
            done = True #now we're done displaying

    # draw the background
    screen.fill(WHITE)
    pygame.display.update()

pygame.quit()