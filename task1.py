import random
word_list = ["apple", "banana", "grape", "orange", "mango"]

secret_word = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

display_word = ["_" for _ in secret_word]

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

while incorrect_guesses < max_guesses and "_" in display_word:
    print("Word:", " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! You have {max_guesses - incorrect_guesses} tries left.\n")

if "_" not in display_word:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("Sorry, you've run out of guesses. The word was:", secret_word)
