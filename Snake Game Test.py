import pygame, sys

pygame.init()
screen = pygame.display.set_mode((400, 500))    #This is our Main Screen (Display Screen)
clock = pygame.time.Clock();                    #Create a clock  to fix FPS

test_surface = pygame.Surface((100,200))        #To create a Sub Screen (Screen)
test_surface.fill((0,0,255))                    #To fill our screen with a selected color
#test_rect = pygame.Rect(100,200,100,100)       #To draw a Rectangle
test_rect = test_surface.get_rect(center = (200,250))

while True:
    #Draw all our elements

    for event in pygame.event.get():            #To look for any event in the application
        if event.type == pygame.QUIT:           #If the user click exit button
            pygame.quit()                       #Then exit the applicaiton
            sys.exit(0)

    #screen.fill(pygame.Color('Red'))           #To fill the Display Screen wiht a pre-define color
    screen.fill((175,215,70))                   #To fill the Display Screen with a selected color
    
    #pygame.draw.ellipse(screen,pygame.Color('Red'),test_rect) #To Draw and fill the rectangle with color
    test_rect.right += 1
    screen.blit(test_surface,test_rect)         #To Show our screen
    
    pygame.display.update()                     #To take all the display and show it
    clock.tick(60)                              #To fix the FPS to 60