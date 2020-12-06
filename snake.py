import pygame
import time
import random

class game:
    def __init__(self, screen):
        self.screen = screen
        self.background = (143, 255, 109)
        self.grid = [[0] * 48 for i in range(27)]
        self.snake = [[20,20], [20,19], [20,18]]
        self.running = True
        self.direction = (0, 1)
        self.apclock = time.perf_counter()
        self.movclock = time.perf_counter()

    def play(self):
        pygame.init()
        starttime = time.perf_counter()
        while self.running:
            self.draw()
            self.round()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            while (time.perf_counter() - starttime) < 0.01:
                pass

    def draw(self):
        self.screen.fill(self.background)
        y = 0
        x = 0
        for segment in self.snake:
            pygame.draw.rect(self.screen, (255, 255, 255), (segment[0] * 40, segment[1] * 40, 40, 40))
        for line in self.grid:
            for square in line:
                if square == 0:
                    pass
                elif square == 1:
                    pygame.draw.rect(self.screen, (255, 0, 0), (x, y, 40, 40))
                x += 40
            y += 40
            x = 0
        pygame.display.flip()

    def round(self):
        if time.perf_counter() - self.apclock > 5:
            self.grid[random.randint(0, 26)][random.randint(0, 47)] = 1
            self.apclock = time.perf_counter()
        
        if time.perf_counter() - self.movclock > 0.1:
            temp = self.snake[0]
            temp2 = None
            for i in range(len(self.snake) - 1):
                temp2 = self.snake[i + 1]
                self.snake[i + 1] = temp
                temp = temp2
            self.snake[0] = [self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1]]
            self.movclock = time.perf_counter()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction = (0, -1)
        if keys[pygame.K_s]:
            self.direction = (0, 1)
        if keys[pygame.K_a]:
            self.direction = (-1, 0)
        if keys[pygame.K_d]:
            self.direction = (1, 0)
        if self.snake[0][0] < 0 or self.snake[0][0] > 47 or self.snake[0][1] < 0 or self.snake[0][1] >= 27:
            self.running = False
        for i in range(len(self.snake) - 1):
            if self.snake[i + 1] == self.snake[0]:
                self.running = False
        try:
            if self.grid[self.snake[0][1]][self.snake[0][0]] == 1:
                self.grid[self.snake[0][1]][self.snake[0][0]] = 0
                newdirectionx = self.snake[len(self.snake) - 2][0] - self.snake[len(self.snake) - 1][0]
                newdirectiony = self.snake[len(self.snake) - 2][1] - self.snake[len(self.snake) - 1][1]
                self.snake.append([self.snake[len(self.snake) - 1][0] + newdirectionx, self.snake[len(self.snake) - 1][1] + newdirectiony])
        except(Exception):
            pass
            
        

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    pygame.display.toggle_fullscreen()
    Game = game(screen)
    Game.play()
    pygame.quit()
