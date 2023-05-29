import pygame
from PIL import Image
from sys import exit

# To-Do List
# Give bottom wall more space
# Remove elements of map to rects
# Animate Character
# Make classes
# Organize assets

pygame.init()

screen = pygame.display.set_mode((512, 512)) # width, height
pygame.display.set_caption('Roguelike')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

test_surface = pygame.image.load('map.png').convert()
# text_surface = test_font.render("Sussy Baka", False, 'Red').convert()

char_surface = pygame.image.load('tile000.png').convert()
char_rect = char_surface.get_rect(center = (116, 86))

left_wall = pygame.image.load('leftwall.png').convert()
left_rect = left_wall.get_rect(topleft = (0, 0))

top_wall = pygame.image.load('Topwall.png').convert()
top_rect = top_wall.get_rect(topleft = (8, 0))

right_wall = pygame.image.load('rightwall.png').convert()
right_rect = right_wall.get_rect(topleft = (504, 0))

bot_wall = pygame.image.load('realbotwall.png').convert()
bot_rect = bot_wall.get_rect(topleft = (8, 478))

walls = [left_rect, top_rect, right_rect, bot_rect]

speed = 5

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pressed = pygame.key.get_pressed()
    # if pressed[pygame.K_w]:
    #    print("w is pressed")
    # if pressed[pygame.K_s]:
    #    print("s is pressed")

    screen.blit(test_surface, (0, 0))

    screen.blit(char_surface, char_rect)
    screen.blit(left_wall, left_rect)
    screen.blit(top_wall, top_rect)
    screen.blit(right_wall, right_rect)
    screen.blit(bot_wall, bot_rect)
    # char_rect.left -= 1

    if pressed[pygame.K_a]:
       char_rect.left -= speed
    if pressed[pygame.K_d]:
       char_rect.right += speed
    if pressed[pygame.K_w]:
        char_rect.top -= speed
    if pressed[pygame.K_s]:
        char_rect.bottom += speed

    for wall in walls:
        if char_rect.colliderect(left_rect):
            char_rect.left = left_rect.right
        if char_rect.colliderect(right_rect):
            char_rect.right = right_rect.left
        if char_rect.colliderect(top_rect):
            char_rect.top = top_rect.bottom
        if char_rect.colliderect(bot_rect):
            char_rect.bottom = bot_rect.top

    # print(char_rect.center)

    # print(char_rect.x, char_rect.y)

    pygame.display.update()
    clock.tick(60)
