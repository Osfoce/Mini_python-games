# Osfoce 
import time
import pygame
import numpy as np

BG_COLOR = (10, 10, 10)  
GRID_COLOR = (40, 40, 40)  
DIE_COLOR = (170, 170, 170) 
ALIVE_COLOR =(255, 255,255)  
pygame.display.set_caption("Conway's Game of life")

def update(screen, cells, size, Gen = False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))  

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = BG_COLOR if cells[row,  col] == 0 else ALIVE_COLOR

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if Gen:
                    color = DIE_COLOR
            elif 2 <= alive <= 3:
                updated_cells[row, col] =1
                if Gen:
                    color = ALIVE_COLOR

        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if Gen:
                    color = ALIVE_COLOR

        pygame.draw.rect(screen, color, (col * size, row * size, size -1, size -1))

    return updated_cells


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    cells = np.zeros((80, 80))
    screen.fill(GRID_COLOR)
    update(screen, cells, 10)

   # pygame.display.flip()
    pygame.display.update()

    running = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10)
                pygame.display.update()

        screen.fill(GRID_COLOR)

        if running:
            cells = update(screen, cells, 10, Gen=True)
            pygame.display.update()

        time.sleep(0.001)

if __name__ == '__main__':
    main()
             
