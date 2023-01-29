import pygame
from random import randrange as rnd


WIDTH, HEIGHT = 1200, 800
fps = 60


lynx_w = 330
lynx_h = 35
lynx_speed = 15
lynx = pygame.Rect(WIDTH // 2 - lynx_w // 2, HEIGHT - lynx_h - 10, lynx_w, lynx_h)

# ppo = ball
ppo_radius = 20
ppo_speed = 10
ppo_rect = int(ppo_radius * 2 ** 0.5)
ppo = pygame.Rect(rnd(ppo_rect, WIDTH - ppo_rect), HEIGHT // 2, ppo_rect, ppo_rect)
dx, dy = 1, -1


block_list = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(10) for j in range(4)]


pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


img = pygame.image.load('backggound.png').convert()


def detect_collision(dx, dy, ppo, rect):
    if dx > 0:
        delta_x = ppo.right - rect.left
    else:
        delta_x = rect.right - ppo.left
    if dy > 0:
        delta_y = ppo.bottom - rect.top
    else:
        delta_y = rect.bottom - ppo.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.blit(img, (0, 0))

    [pygame.draw.rect(sc, color_list[color], block) for color, block in enumerate(block_list)]
    pygame.draw.rect(sc, pygame.Color('white'), lynx)
    pygame.draw.circle(sc,pygame.Color('white'), ppo.center, ppo_radius)


    ppo.x += ppo_speed * dx
    ppo.y += ppo_speed * dy


    if ppo.centerx < ppo_radius or ppo.centerx > WIDTH - ppo_radius:
        dx = -dx


    if ppo.centery < ppo_radius:
        dy = -dy


    if ppo.colliderect(lynx) and dy > 0:
        dx, dy = detect_collision(dx, dy, ppo, lynx)


    hit_index = ppo.collidelist(block_list)
    if hit_index != -1:
        hit_rect = block_list.pop(hit_index)
        hit_color = color_list.pop(hit_index)
        dx, dy = detect_collision(dx, dy, ppo, hit_rect)


    if ppo.bottom > HEIGHT:
        print('ППО не працює:(')
        exit()
    elif not len(block_list):
        print('ППО ПРАЦЮЄ!!!')
        exit()


    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and lynx.left > 0:
        lynx.left -= lynx_speed
    if key[pygame.K_RIGHT] and lynx.right < WIDTH:
        lynx.right += lynx_speed


    pygame.display.flip()
    clock.tick(fps)