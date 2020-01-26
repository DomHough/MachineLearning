import pygame
pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

class Car():
    def __init__(self):
        self.angle = 0
        self.width = 25
        self.height = 50

class Sensors():
    def __init__(self, car):
        self.length = 50

    def sensorPosition(self, angle, Car):
        x = math.cos(math.radians(angle + Car.angle)) * self.length
        y = math.sin(math.radians(angle + Car.angle)) * self.length
        return x, y

    def update():
        x, y = sensorPosition(-90, Car)
        frontsensor = pygame.draw.line(dislay, blue, car.rect.topmiddle, (x, y))
        x, y = sensorPosition(-110, Car)
        frontsensor = pygame.draw.line(dislay, blue, car.rect.topmiddle, (x, y))
        x, y = sensorPosition(-135, Car)
        frontsensor = pygame.draw.line(dislay, blue, car.rect.topleft, (x, y))
        x, y = sensorPosition(-180, Car)
        frontsensor = pygame.draw.line(dislay, blue, car.rect.topleft, (x, y))
        x, y = sensorPosition(-70, Car)
        frontsensor = pygame.draw.line(dislay, blue, car.rect.topmiddle, (x, y))
        x, y = sensorPosition(-45, Car)
        frontsensor = pygame.draw.line(dislay, blue, car.rect.topright, (x, y))
        x, y = sensorPosition(0, Car)
        frontsensor = pygame.draw.line(dislay, blue, car.rect.topright, (x, y))
        x, y = sensorPosition(90, Car)
        frontsensor = pygame.draw.line(dislay, blue, car.rect.bottommiddle, (x, y))
        x, y = sensorPosition(135, Car)
        frontsensor = pygame.draw.line(dislay, blue, car.rect.bottomleft, (x, y))
        x, y = sensorPosition(45, Car)
        frontsensor = pygame.draw.line(dislay, blue, car.rect.bottomright, (x, y))

display = pygame.display.set_mode((800, 800))
pygame.display.set_caption('CarAI')
clock = pygame.time.Clock()

running = True

while running == True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display.fill(white)
    car = pygame.Rect(375, 375, 50, 50)
    pygame.draw.rect(display, red, car)
    pygame.draw.line(display, blue, (400, 375), (300, 0))
    pygame.display.update()
