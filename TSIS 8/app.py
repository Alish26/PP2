from random import randint
import pygame
import time


class Apple:
    x = 0
    y = 0
    step = 20
 
    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step
 
    def draw(self, surface):
        pygame.draw.rect(surface, (105, 135, 240), pygame.Rect(self.x, self.y, 20, 20))
 
 
class Player:
    x = [0]
    y = [0]
    step = 20
    direction = 0
    length = 3
 
    updateCountMax = 2
    updateCount = 0
 
    def __init__(self, length):
       self.length = length
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)
 
       # initial positions, no collision.
       self.x[1] = 1*20
       self.x[2] = 2*20
 
    def update(self):
 
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
 
            # update previous positions
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
 
            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step
 
            self.updateCount = 0
 
 
    def moveRight(self):
        self.direction = 0
 
    def moveLeft(self):
        self.direction = 1
 
    def moveUp(self):
        self.direction = 2
 
    def moveDown(self):
        self.direction = 3 
 
    def draw(self, surface):
        for i in range(0,self.length):
            pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(self.x[i], self.y[i], 19, 19))
 
class Game:
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False

class Wall:
    x = []
    y = []
    def __init__(self, level):
        if level:
            f = open("levels/level{0}.txt".format(level))
            row = -1
            for i in f:
                row += 1
                for j in range(len(i)):
                    if(i[j] == '#'):
                        self.x.append(j * 20)
                        self.y.append(row * 20)

    def draw(self, screen):
        for i in range(len(self.x)):
            pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(self.x[i], self.y[i], 20, 20))
class App:
 
    windowWidth = 800
    windowHeight = 600
    player = 0
    apple = 0
    wall = 0
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.game = Game()
        self.player = Player(3) 
        self.apple = Apple(5,5)
        self.wall = Wall(1)

 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight))
 
        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
 
    def on_event(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self._running = False
    
    def game_over(self):
        my_font = pygame.font.SysFont('times new roman', 90)
        game_over_surface = my_font.render('Game Over', True, (255, 0, 0))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (800/2, 600/4)
        self._display_surf.fill((0, 0, 0))
        self._display_surf.blit(game_over_surface, game_over_rect)
        pygame.display.flip()

    def on_loop(self):
        self.player.update()
 
        # with apple?
        for i in range(0,self.player.length):
            if self.game.isCollision(self.apple.x,self.apple.y,self.player.x[i], self.player.y[i],2):
                self.apple.x = randint(2,30) * 20
                self.apple.y = randint(2,20) * 20
                self.player.length = self.player.length + 1

 
 
        # with itself?
        for i in range(2,self.player.length):
            if self.game.isCollision(self.player.x[0],self.player.y[0],self.player.x[i], self.player.y[i],2):
                self.game_over()
                time.sleep(3)
                exit(0)
            
        # with wall?
        for i in range(len(self.wall.x)):
            if self.game.isCollision(self.player.x[0], self.player.y[0], self.wall.x[i], self.wall.y[i], 2):
                self.game_over()
                time.sleep(3)
                exit(0)

 
 
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.player.draw(self._display_surf)
        self.apple.draw(self._display_surf)
        self.wall.draw(self._display_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
    
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
 
            if (keys[pygame.K_RIGHT]):
                self.player.moveRight()
 
            if (keys[pygame.K_LEFT]):
                self.player.moveLeft()
 
            if (keys[pygame.K_UP]):
                self.player.moveUp()
 
            if (keys[pygame.K_DOWN]):
                self.player.moveDown()
 
            if (keys[pygame.K_ESCAPE]):
                self._running = False

            self.on_event(pygame.event.get())
            self.on_loop()
            self.on_render()

            time.sleep (50.0 / 1000.0);
        self.on_cleanup()


if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()