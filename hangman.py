import pygame
import sys
import random

pygame.init()

# Screen dimensions and colors
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36
LINE_WIDTH = 5

# Setup the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# Fonts
font = pygame.font.Font(None, FONT_SIZE)
small_font = pygame.font.Font(None, FONT_SIZE // 2)

# Word categories and words
WORD_CATEGORIES = {
    "Programming": ["PYTHON", "JAVA", "JAVASCRIPT", "HTML", "CSS"],
    "Games": ["HANGMAN", "TETRIS", "PACMAN", "CHESS", "GO"],
    "Animals": ["ELEPHANT", "GIRAFFE", "KANGAROO", "ZEBRA", "TIGER"]
}

def get_word(category):
    if category not in WORD_CATEGORIES:
        raise ValueError("Category not found.")
    return random.choice(WORD_CATEGORIES[category]).upper()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def draw_hangman(attempts):
    pygame.draw.line(screen, BLACK, (100, 500), (300, 500), LINE_WIDTH)  # Base
    pygame.draw.line(screen, BLACK, (150, 500), (150, 100), LINE_WIDTH)  # Pole
    pygame.draw.line(screen, BLACK, (150, 100), (250, 100), LINE_WIDTH)  # Beam
    pygame.draw.line(screen, BLACK, (250, 100), (250, 150), LINE_WIDTH)  # Rope

    if attempts >= 1:
        pygame.draw.circle(screen, BLACK, (250, 180), 30, LINE_WIDTH)  # Head
    if attempts >= 2:
        pygame.draw.line(screen, BLACK, (250, 210), (250, 300), LINE_WIDTH)  # Body
    if attempts >= 3:
        pygame.draw.line(screen, BLACK, (250, 300), (220, 380), LINE_WIDTH)  # Left leg
    if attempts >= 4:
        pygame.draw.line(screen, BLACK, (250, 300), (280, 380), LINE_WIDTH)  # Right leg
    if attempts >= 5:
        pygame.draw.line(screen, BLACK, (220, 250), (280, 250), LINE_WIDTH)  # Left arm
    if attempts >= 6:
        pygame.draw.line(screen, BLACK, (250, 250), (250, 300), LINE_WIDTH)  # Right arm

def hangman_game():
    category = random.choice(list(WORD_CATEGORIES.keys()))
    word = get_word(category)
    guessed_letters = set()
    max_attempts = 6
    attempts = 0
    revealed_word = ["_"] * len(word)

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_RETURN:
                    return

                letter = pygame.key.name(event.key).upper()
                if len(letter) == 1 and letter.isalpha():
                    if letter in word:
                        for index, char in enumerate(word):
                            if char == letter:
                                revealed_word[index] = letter
                    else:
                        if letter not in guessed_letters:
                            guessed_letters.add(letter)
                            attempts += 1

        draw_hangman(attempts)
        draw_text(" ".join(revealed_word), font, BLACK, screen, WIDTH // 2, HEIGHT // 2)
        draw_text("Attempts Left: {}".format(max_attempts - attempts), small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 50)

        if "_" not in revealed_word:
            draw_text("You Win!", font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 100)
            pygame.display.flip()
            pygame.time.wait(2000)  # Wait for 2 seconds
            return
        elif attempts >= max_attempts:
            draw_text("Game Over! The word was: {}".format(word), font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 100)
            pygame.display.flip()
            pygame.time.wait(2000)  # Wait for 2 seconds
            return

        pygame.display.flip()

def main_menu():
    while True:
        screen.fill(WHITE)
        draw_text("Hangman Game", font, BLACK, screen, WIDTH // 2, HEIGHT // 2 - 50)
        draw_text("Press ENTER to Start", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2)
        draw_text("Press ESC to Quit", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_RETURN:
                    hangman_game()

        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
