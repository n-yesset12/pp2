import pygame
import time

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

background = pygame.image.load("mickeyclock.jpeg")
background = pygame.transform.scale(background, (600, 600))

minute_hand = pygame.Surface((10, 120), pygame.SRCALPHA)
pygame.draw.rect(minute_hand, (0, 0, 0), (4, 0, 2, 120))  

second_hand = pygame.Surface((5, 150), pygame.SRCALPHA)
pygame.draw.rect(second_hand, (255, 0, 0), (2, 0, 2, 150))  

def rotate_hand(image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    second_angle = -seconds * 6
    minute_angle = -minutes * 6

    min_rotated, min_rect = rotate_hand(minute_hand, minute_angle, (300, 300))
    sec_rotated, sec_rect = rotate_hand(second_hand, second_angle, (300, 300))

    screen.blit(min_rotated, min_rect.topleft)
    screen.blit(sec_rotated, sec_rect.topleft)

    pygame.display.flip()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
