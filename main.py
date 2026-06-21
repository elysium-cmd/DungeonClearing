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

        # groups
        self.all_sprites = pygame.sprite.Group()

        # load
        self.grid()

    def grid(self):
        # initial position
        x = 0
        y = 0
        grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

        for row in grid:
            for spot in row:
                if spot == 0:
                    GridBlock((x, y), self.all_sprites)
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
            # update
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
