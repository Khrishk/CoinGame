import pygame
import biased_flipper
import unbiased_flipper
import random


WIDTH, HEIGHT = 500, 500
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Coin Flipper")
BLUE = (137, 207, 240)
FPS = 60

flip_once_img = pygame.image.load('Assets/flip_once_button.png').convert_alpha()
flip_five_img = pygame.image.load('Assets/flip_five_times_button.png').convert_alpha()
heads_coin_img = pygame.image.load('Assets/Heads-removebg-preview.png').convert_alpha()
tails_coin_img = pygame.image.load('Assets/Tails-removebg-preview.png').convert_alpha()

#button class
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
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouserover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

once_button = Button(50, 400, flip_once_img, 2)
five_button = Button(300, 400, flip_five_img, 2)

def draw_window():
    screen.fill(BLUE)
    if once_button.draw():
        unbiased_flip_once()
    if five_button.draw():
        unbiased_flip_five()
    pygame.display.update()

def display_heads():
    screen.blit(heads_coin_img, (200, 200))

def unbiased_flip_once():
    recordList = []
    heads = 0
    tails = 0
    for i in range(1):
        flip = random.randint(0, 1)
        if flip == 0:
            display_heads()
            screen.blit(heads_coin_img, (200, 200))
            recordList.append("Heads")
            heads += 1
        else:
            print("Tails")
            recordList.append("Tails")
            tails += 1
    print(str(recordList))

def unbiased_flip_five():
    recordList = []
    heads = 0
    tails = 0
    for i in range(5):
        flip = random.randint(0, 1)
        if flip == 0:
            print("Heads")
            recordList.append("Heads")
            heads += 1
        else:
            print("Tails")
            recordList.append("Tails")
            tails += 1
    print(str(recordList))

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
    main()
