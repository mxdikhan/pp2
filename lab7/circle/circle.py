import pygame
white=(255,255,255)
red=(255,0,0)

x=200
y=200

clock = pygame.time.Clock()
FPS = 60

#image =pygame.image.load("head.png")
#image = pygame. transform. scale(image, (152, 187.5))
pygame.init()
screen =pygame.display.set_mode((700,600))
done =False

pygame.mixer.music.load('Loonboon.mp3')
pygame.mixer.music.play(-1)

while not done:
        clock.tick(FPS)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            y -= 20
        if pressed[pygame.K_DOWN]:
            y += 20
        if pressed[pygame.K_LEFT]:
            x -= 20
        if pressed[pygame.K_RIGHT]:
            x += 20
        if x>=700:
            x=0
        elif x<=0:
            x=700
        if y>=600:
            y=0
        elif y<=0:
            y=600
        
        screen.fill(white)

        #screen.blit(image,(x,y))
        pygame.draw.circle(screen, red, (x, y), 25)
        
        pygame.display.flip()

        