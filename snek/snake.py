import random
import pygame
import sys

# global variables
WIDTH = 24
HEIGHT = 24
SIZE = 20
SCREEN_WIDTH = WIDTH * SIZE
SCREEN_HEIGHT = HEIGHT * SIZE

DIR = {
    'u' : (0, -1), # north is -y
    'd' : (0, 1),
    'l' : (-1,0),
    'r' : (1,0)
}


class Snake(object):
    l = 1
    body = [(WIDTH // 2 + 1, HEIGHT // 2),(WIDTH // 2, HEIGHT // 2)]
    direction = 'r'
    dead = False

    def __init__(self):
        pass
    
    def get_color(self, i):
        hc = (40,50,100)
        tc = (90,130,255)
        return tuple(map(lambda x,y: (x * (self.l - i) + y * i ) / self.l, hc, tc))

    def get_head(self):
        return self.body[0]

    def turn(self, dir):
        # TODO: See section 3, "Turning the snake".
        self.direction = dir
        pass

    def collision(self, x, y):
        # TODO: See section 2, "Collisions", and section 4, "Self Collisions"
        if x > 23 or x < 0 or y > 23 or y < 0:
            return True
        for i in range(len(self.body)):
            for j in range(0, i):
                if self.body[i] == self.body[j]:
                    return True
        pass
    
    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self):
        # TODO: See section 1, "Move the snake!". You will be revisiting this section a few times.
        if self.l > (len(self.body) - 1):
            self.body.append(tuple(map(lambda x,y:x-y, self.body[len(self.body)-1], DIR[self.direction])))
        for i in range(len(self.body)-1, 0, -1):
            self.body[i] = self.body[i-1]
        self.body[0] = tuple(map(lambda x,y:x+y, self.body[0], DIR[self.direction]))

        print(self.body)

        if self.collision(self.body[0][0], self.body[0][1]):
            self.kill()
                
        pass

    def kill(self):
        # TODO: See section 11, "Try again!"
        #Implements feature #11

        for i in range (len(self.body)-1, 1, -1):
            self.body.pop()

        self.body = [(WIDTH // 2 + 1, HEIGHT // 2),(WIDTH // 2, HEIGHT // 2)]
        print(self.body)
        self.l = 1
        self.dead = True

    def draw(self, surface):
        for i in range(len(self.body)):
            p = self.body[i]
            pos = (p[0] * SIZE, p[1] * SIZE)
            r = pygame.Rect(pos, (SIZE, SIZE))
            pygame.draw.rect(surface, self.get_color(i), r)

    def handle_keypress(self, k):
        if k == pygame.K_UP:
            self.turn('u')
        if k == pygame.K_DOWN:
            self.turn('d')
        if k == pygame.K_LEFT:
            self.turn('l')
        if k == pygame.K_RIGHT:
            self.turn('r')
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type != pygame.KEYDOWN:
                continue
            self.handle_keypress(event.key)
    
    def wait_for_key(self):
        # TODO: see section 10, "wait for user input".
        pass


# returns an integer between 0 and n, inclusive.
def rand_int(n):
    return random.randint(0, n)

class Apple(object):
    position = (10,10)
    color = (233, 70, 29)
    def __init__(self):
        self.place([])

    def place(self, snake):
        # TODO: see section 6, "moving the apple".
        if snake != []:
            while(True):
                x = rand_int(23)
                y = rand_int(23)
                p = snake.body[0]
                if x!= p[0] and y!= p[1]:
                    self.position = (x, y)
                    break
        pass

    def draw(self, surface):
        pos = (self.position[0] * SIZE, self.position[1] * SIZE)
        r = pygame.Rect(pos, (SIZE, SIZE))
        pygame.draw.rect(surface, self.color, r)

def draw_grid(surface):
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            r = pygame.Rect((x * SIZE, y * SIZE), (SIZE, SIZE))
            color = (169,215,81) if (x+y) % 2 == 0 else (162,208,73)
            pygame.draw.rect(surface, color, r)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    snake = Snake()
    apple = Apple()

    score = 0
    difficulty = 4.0

    while True:
        # TODO: see section 9, "incremental difficulty".
        # Implements feature #9
        clock.tick(difficulty + 0.5 * score)
        snake.check_events()
        draw_grid(surface)        
        snake.move()
        snake.draw(surface)
        apple.draw(surface)
        # TODO: see section 5, "Eating the Apple".
        if snake.get_head() == apple.position:
            score += 1
            snake.l += 1
            apple.place(snake)

        screen.blit(surface, (0,0))
        # TODO: see section 8, "Display the Score"
        score_font = pygame.font.Font(None, 30) 
        score_surf = score_font.render("Score: " + str(score), 1, (255, 255, 255))
        score_pos = (12, 12)
        screen.blit(score_surf, score_pos)

        pygame.display.update()
        if snake.dead:
            score = 0
            #pygame.quit()
            #sys.exit(0)
            snake.dead = False

if __name__ == "__main__":
    main()