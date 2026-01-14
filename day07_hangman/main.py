import random
from hangman_art import stages, logo
from hangman_words import word_list

lives = 6
print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = ["_"] * word_length
correct_letters = []
game_over = False

while not game_over:
    print(f"\n******************************** {lives}/6 LIVES LEFT ********************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed '{guess}'")
        continue

    correct_letters.append(guess)

    for i in range(word_length):
        if chosen_word[i] == guess:
            display[i] = guess

    print("Word to guess: " + " ".join(display))

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"\n******************************** IT WAS '{chosen_word}'. YOU LOSE ********************************")

    if "_" not in display:
        game_over = True
        print("\n******************************** YOU WIN ********************************")

    print(stages[lives])
