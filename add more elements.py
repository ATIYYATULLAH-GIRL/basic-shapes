import pygame

pygame.init()

screen=pygame.display.set_mode((500,600))
screen.fill((255,255,255))
pygame.display.set_caption("ADDING MORE ELEMENTS TO THE WINDOW")

Green=(0,35,0)
pygame.draw.circle(screen,Green,(300,300),50)
pygame.draw.circle(screen,Green,(200,200),50,3)
pygame.draw.rect(screen,Green,pygame.Rect(30,30,60,60))
pygame.draw.rect(screen,Green,pygame.Rect(20,20,40,40),40,3)
pygame.display.update()
running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()