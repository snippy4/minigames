'''
leave me alone ty
'''
import pygame
import time
import random


class ball:
    def __init__(self):
        self.pos = (960, 500)
        self.velocity = (-6,0)
        self.color = (234, 234, 234)
    def getrect(self):
        return (self.pos[0], self.pos[1], 20, -20)
        

class pong:
    def __init__(self, x):
        self.pos = (x, 540)
        self.color = (115, 98, 138)
    def getrect(self):
        return (self.pos[0], self.pos[1], 20, -100)


'''
---------------------------------
cool lines 
---------------------------------
'''
class game:
    def __init__(self, screen):
        self.running = True
        self.screen = screen
        self.background = (24, 54, 66)
        self.player1 = pong(40)
        self.player2 = pong(1880)
        self.ball = ball()

    def play(self):
        pygame.init()
        while self.running:
            self.draw()
            self.keypresses()
            starttime = time.perf_counter()
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
        pygame.draw.rect(self.screen, self.player1.color, self.player1.getrect())
        pygame.draw.rect(self.screen, self.player2.color, self.player2.getrect())
        pygame.draw.rect(self.screen, self.ball.color, self.ball.getrect())
        pygame.display.flip()

    def keypresses(self):
        keys = pygame.key.get_pressed()
        if 1920 >= self.ball.pos[0] >= 1860 and self.player2.pos[1] > self.ball.pos[1] and self.player2.pos[1] - 150 < self.ball.pos[1]:
            self.ball.velocity = (-(abs(self.ball.velocity[0])+1), round((self.ball.pos[1] - self.player2.pos[1] + 50)*0.2))
        if 0<= self.ball.pos[0] <= 60 and self.player1.pos[1] + 20 > self.ball.pos[1] and self.player1.pos[1] - 100 < self.ball.pos[1]:
            self.ball.velocity = (abs(self.ball.velocity[0])+1, round((self.ball.pos[1] - self.player1.pos[1] + 50)*0.2))

            # player 2 prediction thingy
            # this is a test
            
            posx, posy = self.ball.pos
            multiplyer = 1
            while posx < 1860:
                if self.ball.velocity[0] < 1:
                    break
                posx += self.ball.velocity[0]
                posy += multiplyer * self.ball.velocity[1]
                if posy >= 1080 or posy <= 0:
                    multiplyer *= -1
            self.player2.pos = (self.player2.pos[0], posy+random.randint(1,99))
            
        if self.ball.pos[1] >= 1080 or self.ball.pos[1] <= 0:
            self.ball.velocity = (self.ball.velocity[0], -self.ball.velocity[1])
        self.ball.pos = (self.ball.pos[0] + self.ball.velocity[0], self.ball.pos[1] + self.ball.velocity[1])
        if keys[pygame.K_w]:
            self.player1.pos = (self.player1.pos[0], self.player1.pos[1] - 15)
        if keys[pygame.K_s]:
            self.player1.pos = (self.player1.pos[0], self.player1.pos[1] + 15)
        #self.player2.pos = (self.player2.pos[0], self.ball.pos[1] + 1)

        
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    pygame.display.toggle_fullscreen()
    Game = game(screen)
    bad = False
    while not bad:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    bad = True
    Game.play()
    

pygame.quit()
