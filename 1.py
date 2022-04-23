import pygame, random
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
y = 215
g = 0
verh = False
def Ptichka():
    global y
    global g
    global verh
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_UP] and g < 0:
        verh = True
        g = 3
        verh == False
    else:
        g = g - 0.05
    y = y - g
    pygame.draw.rect(screen, [223, 223, 223], [20, int(y), 50, 50], 0)
mas_stolby = []
mas_stolby_y = []
for i in range(4):
    mas_stolby.append(200+200*i)
    mas_stolby_y.append(random.randint(50, 250))
def Stolby():
    for i in range(4):
        mas_stolby[i] = mas_stolby[i] - 1
        
        surf = pygame.Surface((50, mas_stolby_y[i]))
        surf.fill((223, 223, 223))
        screen.blit(surf, (mas_stolby[i], 0))

        surf = pygame.Surface((50, 640))
        surf.fill((223, 223, 223))
        screen.blit(surf, (mas_stolby[i], 200+mas_stolby_y[i]))

        if mas_stolby[i] == -50:
            mas_stolby.pop(0)
            mas_stolby_y.pop(0)
            mas_stolby.append(750)
            mas_stolby_y.append(random.randint(50, 250))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill([0, 0, 0])
    Ptichka()
    Stolby()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
