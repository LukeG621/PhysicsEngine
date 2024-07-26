import pygame
import sys
pygame.init()

WIDTH = 800
HEIGHT = 600

pygame.font.init()
font = pygame.font.SysFont(None, 55)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

# I don't have all of these games done yet. The hardest will easilt be a visualized vector field
options = ['Mass-Spring Oscillator', 'Gravity', 'Friction', 'Visualized Vector Field']
choice = 0

def boot_massSpring():
    import MassSpringOscillator
    MassSpringOscillator.main()

def boot_gravity():
    import Gravity
    Gravity.main()

def boot_friction():
    import friction
    friction.main()

def boot_vecFieldVisualized():
    import vecField
    vecField.main()

def exit():
    pygame.quit()
    sys.exit()

def menuInput():
    global choice
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                choice = (choice + 1) % len(options)
            elif event.key == pygame.K_UP:
                choice = (choice - 1) % len(options)
            elif event.key == pygame.K_RETURN:
                run_choice()

def run_choice():
    if choice == 0:
        boot_massSpring()
    elif choice == 1:
        boot_gravity()
    elif choice == 2:
        boot_friction()
    elif choice == 3:
        boot_vecFieldVisualized()
    else:
        exit()

def drawMenu():
    screen.fill((0,0,0))
    for i, option in enumerate(options):
        if i == choice:
            color = ((80,208,255))
        else:
            color = ((200,200,200))
        text_surface = font.render(f"{i+1}. {option}", True, color)
        text_rect = text_surface.get_rect(center=(WIDTH/2, HEIGHT/2 + i * 60))
        screen.blit(text_surface, text_rect)
    pygame.display.flip()

def main():
    while True:
        menuInput()
        drawMenu()
if __name__ == "__main__":
    main()