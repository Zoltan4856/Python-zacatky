import pygame

pygame.init()

sirka = 1500
vyska = 800



screen  = pygame.display.set_mode((sirka,vyska))
pygame.display.set_caption("Space invaders")

lets_continue = True

while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

pygame.quit
