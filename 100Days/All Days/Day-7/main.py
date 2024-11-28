import os
import random

from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_len = len(chosen_word)
end_of_game = False
lives = 6

print(logo)

display = []
for _ in range(word_len):
    display += "_"

while end_of_game is False:
    guessed_word = input("Guess a letter: ").lower()
    os.system('cls')
    if guessed_word in display:
        print(f"You've already guessed {guessed_word}")
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guessed_word:
            display[position] = letter

    if guessed_word not in chosen_word:
        print(f"You guessed {guessed_word}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("You lose.")
            end_of_game = True
    print(f"{' '.join(display)}")

    if "_" not in display:
        print("You win.")
        end_of_game = True
    print(stages[lives])
