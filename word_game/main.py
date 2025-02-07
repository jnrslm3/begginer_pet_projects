import random

game_title = "Word Guess"

word_bank = []

with open ('words.txt', 'r') as word_file:
    for word in word_file:
        word_bank.append(word.rstrip().lower())

word_to_guess = random.choice(word_bank)

misplaced_guesses = []
incorrect_guesses = []
max_turns = 5
turns_taken = 0

print("Welcome to", game_title)
print("The word has", len(word_to_guess), "letters.")
print("You have", max_turns - turns_taken, "turns left.")

while turns_taken < max_turns:
    user_input = input('Enter a word: ').lower()

    if len(user_input) != len(word_to_guess) or not user_input.isalpha():
        print("Please enter 5-letter word.")
        continue

    index = 0
    for i in user_input:
        if i == word_to_guess[index]:
            print(i, end=" ")
            if i in misplaced_guesses:
                misplaced_guesses.remove(i)
        elif i in word_to_guess:
            if i not in misplaced_guesses:
                misplaced_guesses.append(i)
            print("_", end=" ")
        else:
            if i not in incorrect_guesses:
                incorrect_guesses.append(i)
            print("_", end=" ")
        index += 1


    print("Misplaced letters: ", misplaced_guesses)
    print("Incorrect letters: ", incorrect_guesses)
    turns_taken += 1

    if user_input == word_to_guess:
        print("Congratulations, you win!")
        break

    if turns_taken == max_turns:
        print("Sorry, you lost. The word was", word_to_guess)
        break

    print("You have", max_turns - turns_taken, "turns left.")


