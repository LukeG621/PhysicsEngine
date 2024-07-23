import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 800

screen = pygame.display.set_mode([WIDTH, HEIGHT])

fps = 60
timer = pygame.time.Clock()

# game variables

gravity = 0.5
bounce_stop = 0.3
wall_thickness = 10

class Ball:
    def __init__(self, x_pos, y_pos, radius, color, mass, retention, y_speed, x_speed, id):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.color = color
        self.mass = mass
        self.retention = retention
        self.y_speed = y_speed
        self.x_speed = x_speed
        self.id = id
        self.circle = ''

    def draw(self):
        self.circle = pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)

    def check_gravity(self):
        if self.y_pos < HEIGHT - self.radius - (wall_thickness/2):
            self.y_speed += gravity

        else:
            if self.y_speed > bounce_stop:
                self.y_speed = self.y_speed * -1 * self.retention
            else:
                if abs(self.y_speed) <= bounce_stop:
                    self.y_speed = 0
        
        return self.y_speed

    def update_position(self):
        self.y_pos += self.y_speed
        self.x_pos += self.x_speed

def draw_walls():
    left = pygame.draw.line(screen, 'black', (0,0), (0, HEIGHT), wall_thickness)
    right = pygame.draw.line(screen, 'black', (WIDTH,0), (WIDTH, HEIGHT), wall_thickness)
    top = pygame.draw.line(screen, 'black', (0,0), (WIDTH, 0), wall_thickness)
    bottom = pygame.draw.line(screen, 'black', (0,HEIGHT), (WIDTH, HEIGHT), wall_thickness)
    wall_list = [left, right, top, bottom]


ball1 = Ball(50, 50, 30, 'blue', 100, .9, 0, 0, 1)
ball2 = Ball(500, 500, 50, 'green', 300, .8, 0, 0, 2)

# main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('white')

    walls = draw_walls()
    ball1.draw()
    ball2.draw()
    ball1.update_position()
    ball2.update_position()
    ball1.y_speed = ball1.check_gravity()
    ball2.y_speed = ball2.check_gravity()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()