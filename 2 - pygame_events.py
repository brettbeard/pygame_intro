import pygame

pygame.init()  # start pygame

# create a display screen: 400x400 pixels
screen = pygame.display.set_mode((400, 400))

"""BEGIN code added"""
done = False #we're not done displaying

while not done:
    for event in pygame.event.get(): #check the events list
        if event.type == pygame.QUIT: #if the user clicks the X
            done = True #now we're done displaying

"""END code added"""

pygame.quit()