import pygame, json

class game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.background = (115, 205, 255)
        self.playerpos = (24, 16)
        self.grid = [[-1] * 48 for i in range(27)]
        self.levels = {}
        self.wallsprite = pygame.image.load('sprites/thin ice wall.png')
        self.pufflesprite = pygame.image.load('sprites/thin ice puffle.png')

    def play(self):
        self.loadlevel()
        while self.running:
            self.draw()
            self.round()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    # yes this is badly made
                    if event.key == pygame.K_w:
                        if self.grid[self.playerpos[1] - 1][self.playerpos[0]] == 99:
                            continue
                        self.grid[self.playerpos[1]][self.playerpos[0]] -= 1
                        self.playerpos = (self.playerpos[0], self.playerpos[1] - 1)
                    if event.key == pygame.K_s:
                        if self.grid[self.playerpos[1] + 1][self.playerpos[0]] == 99:
                            continue
                        self.grid[self.playerpos[1]][self.playerpos[0]] -= 1
                        self.playerpos = (self.playerpos[0], self.playerpos[1] + 1)
                    if event.key == pygame.K_a:
                        if self.grid[self.playerpos[1]][self.playerpos[0] - 1] == 99:
                            continue
                        self.grid[self.playerpos[1]][self.playerpos[0]] -= 1
                        self.playerpos = (self.playerpos[0] - 1, self.playerpos[1])
                    if event.key == pygame.K_d:
                        if self.grid[self.playerpos[1]][self.playerpos[0] + 1] == 99:
                            continue
                        self.grid[self.playerpos[1]][self.playerpos[0]] -= 1
                        self.playerpos = (self.playerpos[0] + 1, self.playerpos[1])

    
    def draw(self):
        self.screen.fill((0,0,0))
        x = 0
        y = 0
        for row in self.grid:
            for tile in row:
                if tile == 0:
                    pygame.draw.rect(self.screen, self.background, (x * 40, y * 40, 40, 40))
                elif tile == 1:
                    pygame.draw.rect(self.screen, (217, 241, 255), (x * 40, y * 40, 40, 40))
                elif tile == 99:
                    self.screen.blit(self.wallsprite, (x * 40, y * 40))
                elif tile == 2:
                    pygame.draw.rect(self.screen, (200, 200, 250), (x * 40, y * 40, 40, 40))
                x += 1
            x = 0
            y += 1
        self.screen.blit(self.pufflesprite, (self.playerpos[0] * 40, self.playerpos[1] * 40, 40, 40))
        pygame.display.flip()
    
    def round(self):
        if self.grid[self.playerpos[1]][self.playerpos[0]] == 0:
            self.running = False

    def levelmaker(self):
        activeblock = None
        while self.running:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == pygame.K_1:
                        activeblock = 1
                    elif event.key == pygame.K_2:
                        activeblock = 2
                    elif event.key == pygame.K_0:
                        activeblock = 99
                    elif event.key == pygame.K_p:
                        self.play()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.grid[int(event.pos[1] / 40)][int(event.pos[0] / 40)] = activeblock
        pygame.quit()
        levelname = input()
        with open(f'{levelname}.lvl', 'a') as f:
            f.write(json.dumps(self.grid))
        
    def loadlevel(self):
        with open('test lvl.lvl', 'r') as f:
            self.grid = json.loads(f.read())



if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    pygame.display.toggle_fullscreen()
    Game = game(screen)
    Game.play()
