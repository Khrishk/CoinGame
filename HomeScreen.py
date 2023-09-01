import pygame
import biased_flipper
import unbiased_flipper
import random

WIDTH, HEIGHT = 500, 500
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Coin Flipper")
BLUE = (137, 207, 240)
white=(255,255,255)

FPS = 60

flip_once_img = pygame.image.load('Assets/flip_once_button.png').convert_alpha()
flip_five_img = pygame.image.load('Assets/flip_five_times_button.png').convert_alpha()
heads_coin_img = pygame.image.load('Assets/Heads-removebg-preview.png').convert_alpha()
tails_coin_img = pygame.image.load('Assets/Tails-removebg-preview.png').convert_alpha()

font = pygame.font.SysFont("Arial", 36)



show_heads = False
show_tails = False
screen.fill(BLUE)

# button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouserover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


once_button = Button(50, 400, flip_once_img, 2)
five_button = Button(300, 400, flip_five_img, 2)

def count_heads():
    global heads
    heads += 1
    txtheads = font.render("Heads: " + str(heads), True, white)
    screen.blit(txtheads, (10, 20))

def count_tails():
    global tails
    tails += 1
    txttails = font.render("Tails: " + str(tails), True, white)
    screen.blit(txttails, (250, 20))
def decide_coin():

        rando = random.randint(0, 1)
        global coin_bias
        if rando == 0:
            coin_bias = True
        else:
            coin_bias = False
        print(coin_bias)

def reset_counter():
    global heads, tails

    heads = 0
    tails = 0

def draw_window():
    if once_button.draw():
        if coin_bias:
            biased_flip_once()
        else:
            unbiased_flip_once()
    if five_button.draw():
        if coin_bias:
            biased_flip_five()
        else:
            unbiased_flip_five()
    pygame.display.update()

def biased_flip_once():
    global tails, heads
    for i in range(1):
        flip = random.random()
        if flip < 0.65:
            screen.blit(heads_coin_img, (200, 200))
            count_heads()
        else:
            screen.blit(tails_coin_img, (200, 200))
            count_tails()

def biased_flip_five():
    global tails, heads
    for i in range(5):
        flip = random.random()
        if flip < 0.65:
            screen.blit(heads_coin_img, (200, 200))
            count_heads()
            print(heads)
        else:
            screen.blit(tails_coin_img, (200, 200))
            count_tails()

def unbiased_flip_once():
    global tails, heads
    for i in range(1):
        flip = random.randint(0, 1)
        if flip == 0:
            screen.blit(heads_coin_img, (200, 200))
            count_heads()
        else:
            screen.blit(tails_coin_img, (200, 200))
            count_tails()


def unbiased_flip_five():
    global tails, heads
    for i in range(5):
        flip = random.randint(0, 1)
        if flip == 0:
            screen.blit(heads_coin_img, (200, 200))
            count_heads()
        else:
            screen.blit(tails_coin_img, (200, 200))
            count_tails()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()
    pygame.quit()

if __name__ == "__main__":
    decide_coin()
    reset_counter()
    main()


