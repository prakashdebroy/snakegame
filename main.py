import pygame
import random

pygame.init()

#colours
white = (255,255,255)
red =(255,0,0)
black =(0,0,0)

#creating window
screen_width = 900
screen_height = 600
gamewindow = pygame.display.set_mode((screen_width,screen_height))

#game title
pygame.display.set_caption("Snake Game")
pygame.display.update()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text,[x,y])

def plot_snake(gamewindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gamewindow, color, [x,y, snake_size, snake_size])

#game loop
def gameloop():
    # game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocit_y = 0
    food_x = random.randint(150, 750)
    food_y = random.randint(150, 450)
    snake_size = 20
    fps = 60
    score = 0
    snk_list = []
    snk_length = 1

    while not exit_game:
        if game_over:
            gamewindow.fill(white)
            text_screen("Game Over! Press Enter to continue",red,100,250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 5
                        velocit_y = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        velocity_x = -5
                        velocit_y = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        velocit_y = -5
                        velocity_x = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        velocit_y = 5
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocit_y

            if abs(snake_x-food_x)<21 and abs(snake_y-food_y)<21:
                score +=10

                food_x = random.randint(20, int(screen_width / 2))
                food_y = random.randint(20, int(screen_height / 2))
                snk_length += 2


            gamewindow.fill(white)
            text_screen("score: " + str(score), red, 5, 5)
            pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>(snk_length):
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True



            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True

            plot_snake(gamewindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()

gameloop()