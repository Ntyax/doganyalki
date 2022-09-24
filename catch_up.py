from pygame import *

#створи вікно гри
WIDTH = 700
HEIGHT = 500
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Catch Up")

#задай фон сцени
bg = transform.scale(image.load("background.png"), (WIDTH, HEIGHT))

#створи 2 спрайти та розмісти їх на сцені
run = True
clock = time.Clock()
FPS = 60

sprite1 = transform.scale(image.load("sprite1.png"), (100, 100)) 
sprite2 = transform.scale(image.load("sprite2.png"), (100, 100)) 

x1 = 100
y1 = 300

x2 = 400
y2 = 300


step = 5

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False


    keys = key.get_pressed()
    if keys[K_UP] and y2>0 :
        y2 -= step
    if keys[K_DOWN]:
        y2 += step
    if keys[K_LEFT]:
        x2 -= step
    if keys[K_RIGHT]:
        x2 += step

    if keys[K_w]:
        y1 -= step
    if keys[K_s]:
        y1 += step
    if keys[K_a]:
        x1 -= step
    if keys[K_d]:
        x1 += step




    window.blit(bg, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    display.update()
    clock.tick(FPS)



#оброби подію «клік за кнопкою "Закрити вікно"»