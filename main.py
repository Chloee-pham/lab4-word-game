# Word Game - Lab 4

import random


# ============================================================================
# LOGIC LAYER - Pure functions, no I/O
# ============================================================================

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


# ============================================================================
# UI LAYER - Handles all input/output
# ============================================================================

def display_game_state(masked_word: str, guessed_letters: list[str], lives: int):
    print("\n" + "="*50)
    print(f"Word: {masked_word}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    print(f"Lives remaining: {lives}")
    print("="*50)


def get_player_guess() -> str:
    guess = input("\nGuess a letter: ").strip()
    return guess


def display_win_message(secret_word: str):
    print(f"\n🎉 Congratulations! You won! The word was: {secret_word.upper()}")


def display_lose_message(secret_word: str):
    print(f"\n💀 Game Over! The word was: {secret_word.upper()}")


def ask_play_again() -> bool:
    response = input("\nPlay again? (y/n): ").strip().lower()
    return response == 'y'


# ============================================================================
# GAME LOOP
# ============================================================================

def play_game(word_list: list[str], max_lives: int = 6):
    """Play one round of the game."""
    secret_word = select_random_word(word_list)
    guessed_letters = []
    lives = max_lives
    
    print("\n🎮 Welcome to Word Guess Game!")
    
    # Game loop - continues until win or lose
    game_over = False
    while not game_over:
        masked_word = get_masked_word(secret_word, guessed_letters)
        display_game_state(masked_word, guessed_letters, lives)
        
        guess = get_player_guess()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter.")
            continue
        
        if guess.lower() in [g.lower() for g in guessed_letters]:
            print("⚠️  You already guessed that letter!")
            continue
        
        # Update game state
        guessed_letters, lives = update_game_state(secret_word, guessed_letters, guess, lives)
        
        # Check win/lose conditions
        if is_game_won(secret_word, guessed_letters):
            display_win_message(secret_word)
            game_over = True
        elif is_game_lost(lives):
            display_lose_message(secret_word)
            game_over = True


def main():
    word_list = ["python", "javascript", "programming", "computer", "algorithm", 
                 "function", "variable", "database", "network", "software"]
    
    play_again = True
    while play_again:
        play_game(word_list, max_lives=6)
        play_again = ask_play_again()
    
    print("\n👋 Thanks for playing!")


if __name__ == "__main__":
    main()
