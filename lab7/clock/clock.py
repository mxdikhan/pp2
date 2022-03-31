import datetime
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
image=pygame.image.load("mickeyclock.jpeg")
image = pygame.transform.scale(image, (800, 600))
done = False

def blitRotate(screen, image, pos, origin, angle):

    # offset from pivot to center
    image_rect = image.get_rect(topleft = (pos[0] - origin[0], pos[1]-origin[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    screen.blit(rotated_image, rotated_image_rect)


clock=pygame.time.Clock()
#pic of hands
minute = pygame.image.load("righthand1.png")
minute = pygame.transform.scale(minute,(300,220)) 

second = pygame.image.load("lefthand1.png")
second = pygame.transform.scale(second,(290,220)) 


angle=0

while not done:
        time_min=datetime.datetime.now().minute/60*360
        time_sec=datetime.datetime.now().second/60*360
        screen.blit(image,(0,0))
        
        #screen.blit(minute,(400,190))
        #screen.blit(second,(260,190))
        
        blitRotate(screen,minute,(400,300),(150,110),-time_min+55)
        blitRotate(screen,second,(400,300),(145,110),-time_sec-45)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        clock.tick(60)
        pygame.display.flip()
        pygame.display.update()