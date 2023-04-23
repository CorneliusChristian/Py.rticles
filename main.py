import pygame
pygame.init()
screen = pygame.display.set_mode([700, 700] )

sands = []
states = []
mouseispressed = False
fps = 0
size = 10
k = -1
pygame.font.init()
my_font = pygame.font.SysFont('sans-serif', 30)

rot = screen.get_width() / size
def drawall(canvas, list):
    for i in list:
        pygame.draw.rect(canvas, "#ffe381", ((i[0] * size, i[1] * size), (size, size)))
def bottom(sand):
    return [sand[0],  sand[1]+1]
def left(sand):
    return [sand[0] - 1,  sand[1] + 1]
def leftr(sand):
    return [sand[0] - 1,  sand[1]]
def right(sand):
    return [sand[0] + 1,  sand[1] + 1]
def rightr(sand):
    return [sand[0] + 1,  sand[1]]
running = 1
clock = pygame.time.Clock()
pygame.event.set_allowed([pygame.QUIT, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP])
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseispressed = True
        if event.type == pygame.MOUSEBUTTONUP:  
            mouseispressed = False
    if mouseispressed:
            if [int(pygame.mouse.get_pos()[0] / size), int(pygame.mouse.get_pos()[1] / size)] not in sands:
                sands.append([int(pygame.mouse.get_pos()[0] / size), int(pygame.mouse.get_pos()[1] / size)])
                states.append([True, 0])
    screen.fill((0,0,0))
    for i in range(len(sands)):
        if True == True:
            particle = sands[i]
            k *= -1
            if not bottom(particle) in sands:
                particle[1] += 1
            else:
                if k == -1 and left(particle) not in sands and left(particle)[0] >= 0:
                    particle[0] -= 1
                    particle[1] += 1
                if k == 1 and right(particle) not in sands and right(particle)[0] < rot:
                    particle[1] += 1
                    particle[0] += 1
            if particle[1] > rot:
                particle[1] -= 1
            if bottom(particle) in sands and left(particle) in sands and right(particle) in sands:
                states[i][1] += 1
            if states[i][1] > 3:
                states[i][0] = False
    drawall(screen, sands)
    clock.tick()
    text_surface = my_font.render(str(int(clock.get_fps()))+", "+str(len(sands)), False, (255, 255, 255))
    screen.blit(text_surface, (10,10))
    if k == 1:
        pygame.display.update()
pygame.quit()
