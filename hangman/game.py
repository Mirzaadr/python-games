import pygame
import random

# initialize game
pygame.init()

# set up the screen
WIDTH, HEIGTH = 800, 650
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Hangman - Guess the Movie Game")

# Define colors and fonts
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

font = pygame.font.Font(None, 30)
font_inst = pygame.font.Font(None, 20)


def main():
  # read list of movie name from txt file
  with open("words.txt", "r") as file:
    words = file.readlines()

  word = random.choice(words).strip().upper()

  guessed_letters = set()
  incorrect_guesses = 0
  running = True

  while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.KEYDOWN:
        if event.key >= pygame.K_a and event.key <= pygame.K_z:
          letter = chr(event.key).upper()
          if letter not in guessed_letters:
            guessed_letters.add(letter)
            if letter not in word:
              incorrect_guesses += 1
    
    # Draw word
    display_word = ""
    for char in word:
      if char == " ":
        display_word += " "
      elif char in guessed_letters:
        display_word += char + " "
      else:
        display_word += "_ "
    
    text = font.render(display_word, True, WHITE)
    screen.blit(text, (30, 50))
    if (guessed_letters):
      text_guessed = font_inst.render("GUessed - " + str(guessed_letters), True, RED)
      screen.blit(text_guessed, (30, 575))
    
    # Draw hangman
    if incorrect_guesses > 0:
      pygame.draw.circle(screen, WHITE, (400, 200), 40) # Head
    if incorrect_guesses > 1:
      pygame.draw.line(screen, WHITE, (400, 240), (400, 400), 3) # Body
    if incorrect_guesses > 2:
      pygame.draw.line(screen, WHITE, (400, 280), (300, 340), 3) # Left Arm
    if incorrect_guesses > 3:
      pygame.draw.line(screen, WHITE, (400, 280), (500, 340), 3) # RIght Arm
    if incorrect_guesses > 4:
      pygame.draw.line(screen, WHITE, (400, 400), (300, 500), 3) # Left Leg
    if incorrect_guesses > 5:
      pygame.draw.line(screen, WHITE, (400, 400), (500, 500), 3) # Right Leg
    if incorrect_guesses > 6:
      # Hanging stand
      pygame.draw.line(screen, WHITE, (200, 100), (500, 100), 10)
      pygame.draw.line(screen, WHITE, (400, 100), (400, 200), 10)
      pygame.draw.line(screen, WHITE, (200, 100), (200, 550), 10)
      pygame.draw.line(screen, WHITE, (100, 550), (550, 550), 10)
    
    # win or loss
    if incorrect_guesses >= 7:
      text = font.render("You Lose! The word was: " + word, True, RED)
      screen.blit(text, (30, 600))
    elif all(char in guessed_letters or char == " " for char in word):
      text = font.render("You Win!", True, GREEN)
      screen.blit(text, (50, 600))
    pygame.display.update()
  
  pygame.quit()


if __name__ == "__main__":
  main()

