import pygame
import random

atoms=[]
window_size = 400
pygame.init()
window = pygame.display.set_mode((window_size, window_size))
clock = pygame.time.Clock()
FPS = 0


def draw(surface, x, y, color, size):
    for i in range(0, size):
        pygame.draw.line(surface, color, (x, y-1), (x, y+2), abs(size))
               
def atom(x, y, c):
    return {"x": x, "y": y, "vx": 0, "vy": 0, "color": c}

def randomxy():
    return round(random.random()*window_size + 1)

def create(number, color):
    group = []
    for i in range(number):
        group.append(atom(randomxy(), randomxy(), color))
        atoms.append((group[i]))
    return group

def rule(atoms1, atoms2, g):
    for i in range(len(atoms1)):
        fx = 0
        fy = 0
        for j in range(len(atoms2)):
            a = atoms1[i]
            b = atoms2[j]
            dx = a["x"] - b["x"]
            dy = a["y"] - b["y"]
            d = (dx*dx + dy*dy)**0.5
            if( d > 0 and d < 80):
                F = g/d
                fx += F*dx
                fy += F*dy
        a["vx"] = (a["vx"] + fx)*0.5
        a["vy"] = (a["vy"] + fy)*0.5
        a["x"] += a["vx"]
        a["y"] += a["vy"]
        if(a["x"] <= 0 or a["x"] >= window_size):
            a["vx"] *=-1
        if(a["y"] <= 0 or a["y"] >= window_size):
            a["vy"] *=-1        


yellow = create(100, "yellow")
red = create(100, "red")
green = create(100, "green")

while True:
    window.fill(0)
    rule(red, red, 1)
    rule(red, yellow, -0.15)
    rule(yellow, yellow, -0.1)
    rule(green, yellow,3)
    rule(green, red, -0.5)
    rule(green, green, 1)

    for i in range(len(atoms)):
        draw(window,  atoms[i]["x"], atoms[i]["y"], atoms[i]["color"], 3)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.set_caption("Life! FPS: " + str(int(clock.get_fps())))
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
exit()
