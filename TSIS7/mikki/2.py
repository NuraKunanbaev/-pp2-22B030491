import pygame
from datetime import datetime

pygame.init()
W, H = 800, 800
x = W//2
y = H//2
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((W, H))

mickey = pygame.image.load("TSIS7/mikki/main.png")
leftHand = pygame.image.load("TSIS7/mikki/left-hand.png")
rightHand = pygame.image.load("TSIS7/mikki/right-hand.png")
mickeyRect = mickey.get_rect()
def blitRotateCenter(screen, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = center).center)
    screen.blit(rotated_image, new_rect)
langle = 90
rangle = 90
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    minute = datetime.now().minute
    second = datetime.now().second
    if second >= 60:
        rangle += -(6) 
    langle = -(second * 6 - 2)

    sc.fill(WHITE)
    sc.blit(mickey, (x, y))
    sc.blit(mickey, mickeyRect)
    
    blitRotateCenter(sc, leftHand, (x,y), langle) 
    blitRotateCenter(sc, rightHand, (x,y), rangle)
    pygame.display.update()