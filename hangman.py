import random

# Predefined list of 5 words
words = ["apple", "house", "tiger", "green", "chair"]

# Randomly select a word from the list
secret_word = random.choice(words)
guessed_letters = []
attempts_left = 6

# Create a display with underscores for each letter
display_word = ["_"] * len(secret_word)

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect attempts.\n")

# Game loop
while attempts_left > 0 and "_" in display_word:
    print("Word:", " ".join(display_word))
    print(f"Guessed Letters: {', '.join(guessed_letters)}")
    print(f"Attempts Left: {attempts_left}")
    
    guess = input("Enter a letter: ").lower()

    # Input validation
    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("🔁 You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        print("❌ Wrong guess.\n")
        attempts_left -= 1

# Result
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game Over! The word was:", secret_word)