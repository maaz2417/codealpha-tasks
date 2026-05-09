import random

def play_hangman():
    words = ["python", "keyboard", "mountain", "science", "coding"]
    target_word = random.choice(words)
    
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_attempts:
        display_word = ""
        for letter in target_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {display_word.strip()}")
        print(f"Attempts remaining: {max_attempts - incorrect_guesses}")
        print(f"Guessed so far: {', '.join(guessed_letters)}")

        if "_" not in display_word:
            print(f"Congratulations! You guessed the word: {target_word}")
            break
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)
        if guess in target_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not there.")
    if incorrect_guesses == max_attempts:
        print(f"\nGame Over! You've run out of attempts.")
        print(f"The word was: {target_word}")

if __name__ == "__main__":
    play_hangman()