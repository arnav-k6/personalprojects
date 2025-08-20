import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 48)

max_attempts = 5
word_bank = ["zebra", "dog", "elephant", "mammoth",
             "cheetah", "mouse", "chicken", "goose"]

def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return "".join(word_list)

def draw_text(surface, text, x, y, color=BLACK, center=False):
    """Draw text on the screen."""
    render = FONT.render(text, True, color)
    rect = render.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    surface.blit(render, rect)

def play_game():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Word Scramble Game")

    clock = pygame.time.Clock()

    score = 0
    running = True

    while running:
        word = random.choice(word_bank)
        scrambled = scramble_word(word)
        attempts = max_attempts
        guess = ""
        message = ""

        round_active = True
        while round_active:
            screen.fill(WHITE)

            draw_text(screen, f"Scrambled: {scrambled}", WIDTH//2, 100, center=True)
            draw_text(screen, f"Your Guess: {guess}", WIDTH//2, 200, center=True)
            draw_text(screen, f"Attempts left: {attempts}", WIDTH//2, 300, center=True)
            draw_text(screen, f"Score: {score}", WIDTH//2, 400, center=True)
            draw_text(screen, message, WIDTH//2, 500, (200, 0, 0), center=True)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if guess.lower() == word.lower():
                            message = "Correct!"
                            score += 10
                            round_active = False
                        else:
                            attempts -= 1
                            if attempts == 0:
                                message = f"Out of attempts! Word was: {word}"
                                round_active = False
                            else:
                                message = "Wrong! Try again."
                        guess = ""
                    elif event.key == pygame.K_BACKSPACE:
                        guess = guess[:-1]
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    else:
                        guess += event.unicode

            clock.tick(30)

        pygame.time.delay(2000)

        if attempts == 0:
            screen.fill(WHITE)
            draw_text(screen, f"Game Over! Final Score: {score}", WIDTH//2, HEIGHT//2 - 50, center=True)
            draw_text(screen, "Press Y to play again or N to quit.", WIDTH//2, HEIGHT//2 + 50, center=True)
            pygame.display.flip()

            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            score = 0
                            waiting = False
                        elif event.key == pygame.K_n:
                            pygame.quit()
                            sys.exit()
                clock.tick(30)

play_game()
