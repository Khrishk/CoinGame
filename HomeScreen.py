import pygame
import biased_flipper
import unbiased_flipper
import random

WIDTH, HEIGHT = 500, 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Coin Flipper")
BLUE = (137, 207, 240)
white = (255, 255, 255)

FPS = 60

flip_once_img = pygame.image.load('Assets/flip_once_button.png').convert_alpha()
flip_five_img = pygame.image.load('Assets/flip_five_times_button.png').convert_alpha()
biased_button_img = pygame.image.load('Assets/biased_button_img.png').convert_alpha()
unbiased_button_img = pygame.image.load('Assets/unbiased_button_img.png').convert_alpha()
heads_coin_img = pygame.image.load('Assets/Heads-removebg-preview.png').convert_alpha()
tails_coin_img = pygame.image.load('Assets/Tails-removebg-preview.png').convert_alpha()
game_over_img = pygame.image.load('Assets/GameOver_img.png').convert_alpha()

font = pygame.font.SysFont("Arial", 36)

show_heads = False
show_tails = False


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
biased_button = Button(50, 500, biased_button_img, 2)
unbiased_button = Button(300, 500, unbiased_button_img, 2)
restart_button = Button(0, 0, game_over_img, 2)


def count_heads():
    global heads
    heads += 1



def count_tails():
    global tails
    tails += 1

def count_score():
    global score
    score += 1

def count_health(num):
    global health, restartstate

    if (health - num) <= 0:
        restartstate = True
    else:
        health -= num


def clicked_restart():
    global score, health, restartstate
    restartstate = False
    score = 0
    health = 100
    decide_coin()



def display_counter(heads, tails, score):
    txttails = font.render("Tails: " + str(tails), True, white)
    txtheads = font.render("Heads: " + str(heads), True, white)
    txtscore = font.render("Score: " + str(score), True, white)
    txthealth = font.render("Health: " + str(health), True, white)
    screen.blit(txttails, (250, 20))
    screen.blit(txtheads, (10, 20))
    screen.blit(txtscore, (10, 100))
    screen.blit(txthealth, (250, 100))


def display_coin(coin):
    if coin == "heads":
        screen.blit(heads_coin_img, (200, 200))
    elif coin == "tails":
        screen.blit(tails_coin_img, (200, 200))
    else:
        pass

def display_restart(bool):
    if bool:
        if restart_button.draw():
            clicked_restart()
    else:
        pass


def decide_coin():
    reset_counter()
    rando = random.randint(0, 1)
    global coin_bias
    global coinstate
    if rando == 0:
        coin_bias = True
    else:
        coin_bias = False

    coinstate = "null"


def reset_counter():
    global heads, tails, score

    heads = 0
    tails = 0



def draw_window():
    global heads, tails, coinstate, score, health, restartstate
    screen.fill(BLUE)

    if once_button.draw():
        count_health(2)
        if coin_bias:
            biased_flip_once()
        else:
            unbiased_flip_once()
    if five_button.draw():
        count_health(10)
        if coin_bias:
            biased_flip_five()
        else:
            unbiased_flip_five()
    if biased_button.draw():
        clicked_biased()
    if unbiased_button.draw():
       clicked_unbiased()


    display_counter(heads, tails, score)
    display_coin(coinstate)
    display_restart(restartstate)
    pygame.display.update()


def clicked_biased():
    global coinstate, health
    coinstate = "none"
    decide_coin()

    if coin_bias:
        count_score()
        count_health(-10)
    else:
        count_health(10)

def clicked_unbiased():
    global coinstate, health
    coinstate = "none"
    decide_coin()

    if coin_bias:
        count_health(10)
    else:
        count_score()
        count_health(-10)




def biased_flip_once():
    global tails, heads, coinstate
    for i in range(1):
        flip = random.random()
        if flip < 0.65:
            coinstate = "heads"

            count_heads()
        else:
            coinstate = "tails"

            count_tails()


def biased_flip_five():
    global tails, heads, coinstate
    for i in range(5):
        flip = random.random()
        if flip < 0.65:
            coinstate = "heads"

            count_heads()
        else:
            coinstate = "tails"

            count_tails()


def unbiased_flip_once():
    global tails, heads, coinstate
    for i in range(1):
        flip = random.randint(0, 1)
        if flip == 0:
            coinstate = "heads"

            count_heads()
        else:
            coinstate = "tails"

            count_tails()


def unbiased_flip_five():
    global tails, heads, coinstate
    for i in range(5):
        flip = random.randint(0, 1)
        if flip == 0:
            coinstate = "heads"

            count_heads()
        else:
            coinstate = "tails"

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
    restartstate = False
    score = 0
    health = 100
    decide_coin()
    main()