import random

word_list = ['red', 'green', 'blue']

chosen_word = random.choice(word_list)
print(f"The solution: {chosen_word}")
word_length = len(chosen_word)
display = []
lives = 6
for _ in range(word_length):
    display += "_"
print(display)
end_of_game = False
while not end_of_game:
    guess = input("guess a letter : ").lower()
    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")

    if "_" not in display:
        print("You win!")