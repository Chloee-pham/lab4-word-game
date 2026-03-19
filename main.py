# Word Game - Lab 4

import random
import string
import time


# LOGIC LAYER - Pure functions, no I/O

def update_game_state(secret_word: str,
                      guessed_letters: list[str],
                      guess: str,
                      lives: int) -> tuple[list[str], int]:
    new_guessed_letters = guessed_letters + [guess]

    if guess.lower() in secret_word.lower():
        new_lives = lives
    else:
        new_lives = lives - 1

    return (new_guessed_letters, new_lives)


def get_masked_word(secret_word: str, guessed_letters: list[str]) -> str:
    return ' '.join(
        letter.upper() if letter.lower() in [g.lower() for g in guessed_letters] else '_'
        for letter in secret_word
    )


def is_game_won(secret_word: str, guessed_letters: list[str]) -> bool:
    return all(letter.lower() in [g.lower() for g in guessed_letters] for letter in secret_word)


def is_game_lost(lives: int) -> bool:
    return lives <= 0


def select_random_word(word_list: list[str]) -> str:
    return random.choice(word_list)


def auto_guess(guessed_letters: list[str]) -> str:
    """Auto player picks a random letter that hasn't been guessed yet."""
    available = [c for c in string.ascii_lowercase if c not in [g.lower() for g in guessed_letters]]
    return random.choice(available)


# UI LAYER - Handles all input/output

def display_game_state(masked_word: str, guessed_letters: list[str], lives: int):
    print("\n" + "="*50)
    print(f"Word: {masked_word}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    print(f"Lives remaining: {lives}")
    print("="*50)


def get_player_guess() -> str:
    guess = input("\nGuess a letter: ").strip()
    return guess


def display_win_message(secret_word: str, auto_mode: bool = False):
    who = "Auto Player" if auto_mode else "You"
    print(f"\n🎉 {who} won! The word was: {secret_word.upper()}")


def display_lose_message(secret_word: str, auto_mode: bool = False):
    who = "Auto Player" if auto_mode else "You"
    print(f"\n💀 {who} lost! The word was: {secret_word.upper()}")


def ask_game_mode() -> str:
    """Ask user to choose game mode."""
    print("\n🎮 Word Guess Game!")
    print("1. Play manually")
    print("2. Auto Play (watch the computer play)")
    print("3. Quit")
    choice = input("\nChoose mode (1/2/3): ").strip()
    return choice


# GAME LOOP

def play_game(word_list: list[str], auto_play: bool = False, max_lives: int = 6):
    """Play one round of the game."""
    secret_word = select_random_word(word_list)
    guessed_letters = []
    lives = max_lives

    mode_label = "🤖 Auto Play" if auto_play else "🎮 Manual Play"
    print(f"\n{mode_label} - Start!")

    game_over = False
    while not game_over:
        masked_word = get_masked_word(secret_word, guessed_letters)
        display_game_state(masked_word, guessed_letters, lives)

        if auto_play:
            guess = auto_guess(guessed_letters)
            print(f"\n🤖 Auto Player guesses: {guess}")
            time.sleep(0.8)
        else:
            guess = get_player_guess()

            if len(guess) != 1 or not guess.isalpha():
                print("❌ Please enter a single letter.")
                continue

            if guess.lower() in [g.lower() for g in guessed_letters]:
                print("⚠️  You already guessed that letter!")
                continue

        guessed_letters, lives = update_game_state(secret_word, guessed_letters, guess, lives)

        if is_game_won(secret_word, guessed_letters):
            masked_word = get_masked_word(secret_word, guessed_letters)
            display_game_state(masked_word, guessed_letters, lives)
            display_win_message(secret_word, auto_play)
            game_over = True
        elif is_game_lost(lives):
            display_lose_message(secret_word, auto_play)
            game_over = True


def main():
    word_list = ["python", "javascript", "programming", "computer", "algorithm",
                 "function", "variable", "database", "network", "software"]

    running = True
    while running:
        choice = ask_game_mode()

        if choice == "1":
            play_game(word_list, auto_play=False)
        elif choice == "2":
            play_game(word_list, auto_play=True)
        elif choice == "3":
            running = False
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

    print("\n👋 Thanks for playing!")


if __name__ == "__main__":
    main()
