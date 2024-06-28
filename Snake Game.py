import pygame, sys, random, ctypes
from pygame.math import Vector2

class SNAKE:

    def __init__(self):

        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False

        #To upload the sanke in the code

        #Head
        self.head_up = pygame.image.load('Graphics/Snake/Head/Snake Head Up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/Snake/Head/Snake Head Down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/Snake/Head/Snake Head Right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/Snake/Head/Snake Head Left.png').convert_alpha()

        #Tail
        self.tail_up = pygame.image.load('Graphics/Snake/Tail/Snake Tail Up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/Snake/Tail/Snake Tail Down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/Snake/Tail/Snake Tail Right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/Snake/Tail/Snake Tail Left.png').convert_alpha()

        #Body
        self.body_vertical = pygame.image.load('Graphics/Snake/Body/Snake Body Vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/Snake/Body/Snake Body Horizontal.png').convert_alpha()

        #Curves
        self.body_tr = pygame.image.load('Graphics/Snake/Curves/Snake Curve Up - Right.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/Snake/Curves/Snake Curve Left - Up.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/Snake/Curves/Snake Curve Right - Down.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/Snake/Curves/Snake Curve Down - Left.png').convert_alpha()

        #To Set a Sound For The Crunch (Eating The Apple)
        self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')

    def draw_sanke(self):

        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            
            #We need a rect for positioning
            #Create a rectangle
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            #The face directon
            if index == 0 :
                screen.blit(self.head, block_rect)

            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)

            else:
                pervious_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block

                if pervious_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)

                elif pervious_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)

                else:
                    if pervious_block.x == -1 and next_block.y == -1 or pervious_block.y == -1 and next_block.x == -1 :
                        screen.blit(self.body_tl, block_rect)

                    elif pervious_block.x == -1 and next_block.y == 1 or pervious_block.y == 1 and next_block.x == -1 :
                        screen.blit(self.body_bl, block_rect)

                    elif pervious_block.x == 1 and next_block.y == -1 or pervious_block.y == -1 and next_block.x == 1 :
                        screen.blit(self.body_tr, block_rect)

                    elif pervious_block.x == 1 and next_block.y == 1 or pervious_block.y == 1 and next_block.x == 1 :
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]

        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    def update_tail_graphics(self):

        #tail_relation = self.body[1] - self.body[0]

        #if tail_relation == Vector2(1,0): self.tail = self.tail_right
        #elif tail_relation == Vector2(-1,0): self.tail = self.tail_left
        #elif tail_relation == Vector2(0,1): self.tail = self.tail_down
        #elif tail_relation == Vector2(0,-1): self.tail = self.tail_up

        #Or

        tail_relation = self.body[-2] - self.body[-1]

        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

    def move_snake(self):

        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False    

        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)

class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_Fruit(self):
        #Create a rectangle
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        
        #Draw the rectangle
        #pygame.draw.rect(screen, (126,166,114), fruit_rect)

        #Draw the apple
        screen.blit(apple, fruit_rect)

    def randomize(self):
        #To draw the position of the Fruit
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:

    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def draw_elements(self):
        
        #Draw the grass
        self.draw_grass()

        #To draw the Fruit and Snake
        self.fruit.draw_Fruit()
        self.snake.draw_sanke()

        #To draw the score
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            #Reposition the fruit
            self.fruit.randomize()

            #Add another block to the snake
            self.snake.add_block()

            #To Play The Crunch Sound
            self.snake.play_crunch_sound()

        #To make sure the apple doesnt appear on the snake body
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        score = str(len(self.snake.body) - 3)

        #Check if snake is outside of the screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            ctypes.windll.user32.MessageBoxW(0, "Your Score: " + score, "Game Over", 0)
            self.game_over()

        #Check if the snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
                
                
    def game_over(self):
        
        #Then exit the applicaiton
        #pygame.quit()

        #Then Exit the Environment
        #sys.exit(0)

        self.snake.reset()

    def draw_grass(self):

        grass_color = (167, 209, 61)

        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:

                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:

                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):

        #To draw & operates the score itself
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56,74,12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        
        #To add an apple next to the score
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        
        #To create the background
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 10, apple_rect.height)

        #To Draw Rectangle
        pygame.draw.rect(screen, (167,209,61), bg_rect)
        #To Draw Score
        screen.blit(score_surface, score_rect)
        #To Draw The Apple
        screen.blit(apple, apple_rect)
        #To Draw The Frame
        pygame.draw.rect(screen, (56,74,12), bg_rect, 2)

        return


    def update(self):

        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

pygame.display.set_caption('Snake Game')

programIcon = pygame.image.load('Graphics/Icon.png')
pygame.display.set_icon(programIcon)

cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))    #This is our Main Screen (Display Screen)

#Create a clock  to fix FPS
clock = pygame.time.Clock();

#To upload the apple in the code
apple = pygame.image.load('Graphics/apple.png').convert_alpha()

#To set a font in the game
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 120)

main_game = MAIN()

while True:

    #Draw all our elements
    for event in pygame.event.get():            #To look for any event in the application
        if event.type == pygame.QUIT:           #If the user click exit button
            pygame.quit()                       #Then Exit the applicaiton
            sys.exit(0)                         #Then Exit the Environment
        
        if event.type == SCREEN_UPDATE:
            main_game.update()
        
        #To define the controls
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if main_game.snake.direction.y != 1 :
                    main_game.snake.direction = Vector2(0,-1)

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if main_game.snake.direction.y != -1 :
                    main_game.snake.direction = Vector2(0,1)

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if main_game.snake.direction.x != -1 :
                    main_game.snake.direction = Vector2(1,0)

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if main_game.snake.direction.x != 1 :
                    main_game.snake.direction = Vector2(-1,0)



    #screen.fill(pygame.Color('Red'))           #To fill the Display Screen wiht a pre-define color
    screen.fill((175,215,70))                   #To fill the Display Screen with a selected color
    
    #To draw the Fruit and Snake
    main_game.draw_elements()
    
    #To take all the display and show it
    pygame.display.update()   
    
    #To fix the FPS to 60
    clock.tick(120)