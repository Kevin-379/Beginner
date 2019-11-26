# Creating an empty screen that can be closed
import pygame


def main():
    # initializing pygame
    pygame.init()

    # loading and setting logo and title
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("First pygame")

    # creating a screen
    screen = pygame.display.set_mode((240, 180))
    running = True

    while running:
        for event in pygame.event.get():
            # adding option to quit anytime
            if event.type == pygame.QUIT:
                running = False


main()
