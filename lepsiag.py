import random
import pygame
GRAVITY=0.04
SIRKA = 400
VYSKA = 400
VELKOST = 30
bullkit=[]
ACCEL_Y=0.1
ACCEL_X=0.07
poziciar = random.randint(0, 350)
somarina=[]

for m in range(poziciar,poziciar+50):
    somarina.append(m)
def random():
    poziciar = random.randint(0, 350)

def stvorec(x, y):
    return pygame.Rect(int(x) , int(y) , VELKOST, VELKOST)

def plocha():
    return pygame.Rect(poziciar, VYSKA-5, 50,5 )
def volny_pad():
    color = (0, 0, 255)
    rychlost_y = 0.0
    konec=0
    rychlost_x = 0.0
    pos_x=SIRKA/2-VELKOST/2
    pos_y=VYSKA-VELKOST
    screen = pygame.display.set_mode((SIRKA, VYSKA))
    my_font=pygame.font.SysFont("Arial",25)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            rychlost_y +=ACCEL_Y
        if pressed[pygame.K_RIGHT] and konec==0:
            rychlost_x += ACCEL_X
        if pressed[pygame.K_LEFT] and konec==0:
            rychlost_x -= ACCEL_X

        # if pressed[pygame.K_2]:
        #     rychlost = 2.0
        #
        #
        # if pressed[pygame.K_3]:
        #     rychlost = 3.0
        #
        # if pressed[pygame.K_4]:
        #     rychlost = 4.0


        pos_x += rychlost_x
        pos_y-=rychlost_y
        rychlost_y-=GRAVITY
        if pos_y>=VYSKA-VELKOST-1 and int(rychlost_y)<-1:
            print("Ši še rozbil")
            color=(255,0,0)
            rychlost_x=0
            rychlost_y=0
            konec=1
        if konec==1:
            text_surface = my_font.render("ROZBITY ŠI", False, (255, 127, 0))
            screen.blit(text_surface, (0, 0))
            pos_y=VYSKA-VELKOST
            pos_x=pos_x
            rychlost_x = 0
            rychlost_y = 0
        if pos_y > VYSKA-VELKOST:
            pos_y=VYSKA-VELKOST
            rychlost_y=0
            rychlost_x/=1.2
        if pos_y <= 0:
            rychlost_y=-0.2
            pos_y=0
        if pos_x <=0 :
            pos_x = 0
            rychlost_x =0
        if pos_x>=SIRKA-VELKOST:
            rychlost_x -= rychlost_x+1

            pos_x=SIRKA-VELKOST
        if pos_x >= poziciar-50 and pos_x <poziciar+50 and pos_y>365:
            pos_y=365
            rychlost_y=0
            konec=1
            print("Výhra")
            break






        screen.fill((0,0,0))
        text_surface=my_font.render(f"SPEED X:{rychlost_x:6.1f} Y:{rychlost_y:6.1f}",False,(255,127,0))
        screen.blit(text_surface,(0,0))
        pygame.draw.rect(screen,color,stvorec(pos_x,pos_y))
        pygame.draw.rect(screen, (255,255,255), plocha())
        pygame.display.flip()
        clock.tick(60)


def main():
    pygame.init()
    pygame.font.init()
    volny_pad()
    pygame.quit()


main()