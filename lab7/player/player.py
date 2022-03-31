from random import randint
import pygame

white=(255,255,255)
black=(0,0,0)

x = randint(0, 5) 

music_list=["boggie_wonderland.mp3","loonboon.mp3","reflection.mp3","vamp_anthem.mp3","ArthasMySon.mp3","PeaceSells.mp3"]


pygame.init()
screen =pygame.display.set_mode((200,212))

image=pygame.image.load("stop.png")

done =False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

                pressed = pygame.key.get_pressed()
                if  pressed[pygame.K_SPACE]:
                    pygame.mixer.music.load(music_list[x])
                    pygame.mixer.music.play(0)
            
                if pressed[pygame.K_p]:
                    pygame.mixer.music.pause()
                if pressed[pygame.K_u]:
                    pygame.mixer.music.unpause()
                if pressed[pygame.K_LEFT]:
                    x-=1
                    if x<0:
                        x=5
                        pygame.mixer.music.load(music_list[x])
                        pygame.mixer.music.play(0)
                    else:
                        pygame.mixer.music.load(music_list[x])
                        pygame.mixer.music.play(0)
                if pressed[pygame.K_RIGHT]:
                    x+=1
                    if x>5:
                        x=0
                        pygame.mixer.music.load(music_list[x])
                        pygame.mixer.music.play(0)
                    else:
                        pygame.mixer.music.load(music_list[x])
                        pygame.mixer.music.play(0)
        screen.fill(white)
        screen.blit(image, (0,0))
        
        pygame.display.flip()