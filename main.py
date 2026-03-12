# Word Game - Lab 4

import random


# ============================================================================
# LOGIC LAYER - Pure functions, no I/O
# ============================================================================

def update_game_state(secret_word: str,
                      guessed_letters: list[str],
                      guess: str,
                      lives: int) -> tuple[list[str], int]:
    """
    Updates the game state based on the player's guess.
    
    Args:
        secret_word: The word to guess
        guessed_letters: List of previously guessed letters
        guess: The new letter being guessed
        lives: Current number of lives remaining
    
    Returns:
        A tuple of (new_guessed_letters, new_lives)
    """
    new_guessed_letters = guessed_letters + [guess]
    
    if guess.lower() in secret_word.lower():
        new_lives = lives
    else:
        new_lives = lives - 1
    
    return (new_guessed_letters, new_lives)


def get_masked_word(secret_word: str, guessed_letters: list[str]) -> str:
    """
    Returns the word with unguessed letters masked.
    
    Args:
        secret_word: The word to guess
        guessed_letters: List of guessed letters
    
    Returns:
        Masked word string (e.g., "_ A _ T _ S _")
    """
    return ' '.join(
        letter.upper() if letter.lower() in [g.lower() for g in guessed_letters] else '_'
        for letter in secret_word
    )


def is_game_won(secret_word: str, guessed_letters: list[str]) -> bool:
    """Check if all letters in the word have been guessed."""
    return all(letter.lower() in [g.lower() for g in guessed_letters] for letter in secret_word)


def is_game_lost(lives: int) -> bool:
    """Check if player has run out of lives."""
    return lives <= 0


def select_random_word(word_list: list[str]) -> str:
    """Select a random word from the list."""
    return random.choice(word_list)


# ============================================================================
# UI LAYER - Handles all input/output
# ============================================================================

def display_game_state(masked_word: str, guessed_letters: list[str], lives: int):
    """Display current game state."""
    print("\n" + "="*50)
    print(f"Word: {masked_word}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    print(f"Lives remaining: {lives}")
    print("="*50)


def get_player_guess() -> str:
    """Get a valid single letter guess from player."""
    guess = input("\nGuess a letter: ").strip()
    return guess


def display_win_message(secret_word: str):
    """Display win message."""
    print(f"\n🎉 Congratulations! You won! The word was: {secret_word.upper()}")


def display_lose_message(secret_word: str):
    """Display lose message."""
    print(f"\n💀 Game Over! The word was: {secret_word.upper()}")


def ask_play_again() -> bool:
    """Ask if player wants to play again."""
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
    """Main entry point with replay support."""
    word_list = ["python", "javascript", "programming", "computer", "algorithm", 
                 "function", "variable", "database", "network", "software"]
    
    play_again = True
    while play_again:
        play_game(word_list, max_lives=6)
        play_again = ask_play_again()
    
    print("\n👋 Thanks for playing!")


if __name__ == "__main__":
    main()
