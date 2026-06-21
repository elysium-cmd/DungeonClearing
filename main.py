import pygame
from constants import *
from sprites import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Dungeon Clearing")
        self.clock = pygame.time.Clock()
        self.running = True

        self.playerX = 5
        self.playerY = 9

        # map start
        self.grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.grid[self.playerY][self.playerX] = 1

        # groups
        self.all_sprites = pygame.sprite.Group()

        # load
        self.populateGrid()

    def populateGrid(self):
        # initial position
        x = 0
        y = 0

        for row in self.grid:
            for spot in row:
                if spot == 0:
                    GridBlock((x, y), self.all_sprites, "grey")
                elif spot == 1:
                    GridBlock((x, y), self.all_sprites, "black")
                x += 46
            x = 0
            y += 46

    def run(self):
        while self.running:
            # delta time
            dt = self.clock.tick(FRAMERATE) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and self.playerX > 0:
                self.grid[self.playerY][self.playerX] = 0
                self.playerX -= 1
                self.grid[self.playerY][self.playerX] = 1
            if keys[pygame.K_d] and self.playerX < 10:
                self.grid[self.playerY][self.playerX] = 0
                self.playerX += 1
                self.grid[self.playerY][self.playerX] = 1
            if keys[pygame.K_w] and self.playerY > 0:
                self.grid[self.playerY][self.playerX] = 0
                self.playerY -= 1
                self.grid[self.playerY][self.playerX] = 1
            if keys[pygame.K_s] and self.playerY < 9:
                self.grid[self.playerY][self.playerX] = 0
                self.playerY += 1
                self.grid[self.playerY][self.playerX] = 1

            # update
            self.populateGrid()
            self.all_sprites.update()

            # draw
            self.screen.fill("black")
            self.all_sprites.draw(self.screen)

            pygame.display.flip()
        pygame.quit()


def main():
    pygame.init()

if __name__ == "__main__":
    game = Game()
    game.run()
