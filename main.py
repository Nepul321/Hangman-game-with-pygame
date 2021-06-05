import pygame
import math
import random

#pygame, math, random


pygame.init()

width, height = 800, 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman game!")

RADIUS = 20
GAP = 15
letters = []
startx = round((width - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

letter_font = pygame.font.SysFont('comicsans', 40)
word_font = pygame.font.SysFont('comicsans', 60)

images = []

for i in range(7):
    image = pygame.image.load("Images/" + "hangman" + str(i) + ".png")
    images.append(image)

hangman_status = 0
words = ["DOG", "CAT", "GAMES","SKYPE", "GEOGRAPHY", "HISTORY", "DIAMOND", "RUBY", "HELLO", "NEPUL", "AMAZON", "MICROSOFT", "APPLE", "MACBOOK", "DESKTOP", "YOUTUBE", "WINDOWS", "BINAYA", "PANCHAL", "PINIDI", "POOJAN", "TESLA", "KOTHTHU", "BALLA"]
word = random.choice(words)
guessed = []

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

fps = 60
clock = pygame.time.Clock()
run = True

def draw():
    win.fill(WHITE)

    display_word = ""

    for letter in word:
        if letter in guessed:
            display_word += letter + ""
        else:
            display_word += "_ "
        text = word_font.render(display_word, 1, BLACK)
        win.blit(text, (50, 100))

    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = letter_font.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (375, 1))
    pygame.display.update()

def display_message(message):
    win.fill(WHITE)
    text = word_font.render(message, 1, BLACK)
    win.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(1000)


while run:
    clock.tick(fps)

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
           m_x, m_y = pygame.mouse.get_pos()
           for letter in letters:
               x, y, ltr, visible = letter
               if visible:
                   dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                   if dis < RADIUS:
                         letter[3] = False
                         guessed.append(ltr)
                         if ltr not in word:
                              hangman_status += 1

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    if won:
        display_message("You won!!")
        break

    if hangman_status == 6:
        display_message("You lost!!")
        break


pygame.quit()
