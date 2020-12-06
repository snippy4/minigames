import pygame
import random
import time

class Ball:
    def __init__(self, pos):
        self.pos = pos
        self.velocity = (0, -2)
        self.color = (45, 255, 45)
    def getrect(self):
        return (self.pos[0], self.pos[1], 10, 10)

class brick:
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
    def getrect(self):
        return (self.pos[0], self.pos[1], 96, 20)
        
class Paddle:
    def __init__(self):
        self.pos = (500, 1060)
        self.color = (255, 255, 255)
    def getrect(self):
        return (self.pos[0], self.pos[1], 96, 20)

class game:
    def __init__(self, screen):
        self.running = True
        self.screen = screen
        self.background = (3, 17, 18)
        self.bricks = []
        self.paddle = Paddle()
        self.ball = Ball((500, 800))

    def play(self):
        pygame.init()
        self.setupgame()
        while self.running:
            starttime = time.perf_counter()
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
        pygame.draw.rect(self.screen, self.ball.color, self.ball.getrect())
        pygame.draw.rect(self.screen, self.paddle.color, self.paddle.getrect())
        for block in self.bricks:
            pygame.draw.rect(self.screen, block.color, block.getrect())
        pygame.display.flip()

    def setupgame(self):
        x = 0
        y = 100
        colors = [(231, 237, 109), (212, 85, 205), (64, 238, 247)]
        while y <= 600:
            while x <= 1824:
                color = colors[random.randint(0,2)]
                self.bricks.append(brick((color), (x, y)))
                x += 120
            y += 30
            x = 0

    def round(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.paddle.pos = (self.paddle.pos[0] - 5, self.paddle.pos[1])
        if keys[pygame.K_d]:
            self.paddle.pos = (self.paddle.pos[0] + 5, self.paddle.pos[1])
        self.ball.pos = (self.ball.pos[0] + self.ball.velocity[0], self.ball.pos[1] + self.ball.velocity[1])
        if self.ball.pos[1]  <= 600:
            for block in self.bricks:
                if self.collides(self.ball.getrect(), block.getrect()):
                    self.bricks.remove(block)
                    self.ball.velocity = (self.ball.velocity[0], -self.ball.velocity[1])
        if self.collides(self.ball.getrect(), self.paddle.getrect()):
            self.ball.velocity = (round((self.ball.pos[0] - self.paddle.pos[0] - 50)*0.1), -2)
            if self.ball.velocity[0] == 0:
                self.ball.velocity = (1, self.ball.velocity[1])
        if 0 >= self.ball.pos[0] or self.ball.pos[0] >= 1920:
            self.ball.velocity = (-self.ball.velocity[0], self.ball.velocity[1])
        if self.ball.pos[1] <= 0:
            self.ball.velocity = (self.ball.velocity[0], -self.ball.velocity[1])
               
    def collides(self, rect1, rect2):
        if rect1[0] < rect2[0] + rect2[2] and rect1[0] + rect1[2] > rect2[0] and rect1[1] < rect2[1] + rect2[3] and rect1[1] + rect1[3] > rect2[1]:
            return True
        return False
            
if __name__ == "__main__":
    while True:
        pygame.init()
        screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        pygame.display.toggle_fullscreen()
        Game = game(screen)
        Game.play()
        pygame.quit()
    
