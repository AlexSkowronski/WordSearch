from assets.helper import *
import random

if __name__ == "__main__":
    """1. Load in full bank of words to choose from"""
    WORD_BANK_URL = "https://www.mit.edu/~ecprice/wordlist.10000"
    FULL_WORD_BANK = get_word_bank(WORD_BANK_URL)

    """2. Prompt user to choose a width and height of grid, after choosing how many words they wish to be in the word-search"""
    NUMBER_OF_WORDS = input("How many words would you like in the word-search? Please enter an integer: ")
    while not check_valid_entry_integer(NUMBER_OF_WORDS):
        NUMBER_OF_WORDS = input(f"Your input \"{NUMBER_OF_WORDS}\" is not an integer, please try again!")
    NUMBER_OF_WORDS = int(NUMBER_OF_WORDS)

    BANK = pick_random_words(FULL_WORD_BANK, NUMBER_OF_WORDS)
    
    GRID_WIDTH = input("Please enter a width for the word-search grid as an integer:")
    while not check_valid_entry_integer(GRID_WIDTH):
        GRID_WIDTH = input(f"Your input \"{GRID_WIDTH}\" is not an integer, please try again!")
    GRID_WIDTH = int(GRID_WIDTH)

    GRID_HEIGHT = input("Please enter a height for the word-search grid as an integer:")
    while not check_valid_entry_integer(GRID_HEIGHT):
        GRID_HEIGHT = input(f"Your input \"{GRID_HEIGHT}\" is not an integer, please try again!")
    GRID_HEIGHT = int(GRID_HEIGHT)

    """3. Initialise grid and copy of bank of words to find"""
    game = create_empty_grid(GRID_WIDTH, GRID_HEIGHT)
    SAVED_BANK = []

    """4. Loop over bank of words till empty"""
    attempts = 0
    attempt_limit = 100
    while BANK and attempts < attempt_limit:
        """4a. Choose a position on the grid"""
        position = pick_random_square(GRID_WIDTH, GRID_HEIGHT)

        """4b. Check how many squares up, down, left and right of current position are empty string values"""
        squares_usable = check_available_squares(game, position, GRID_WIDTH, GRID_HEIGHT)

        """4c. Check to see if current word selected can fit in any of these directions"""
        valid_directions = fit_word_check(BANK[-1], squares_usable)

        """4d. Checks if list of valid direction is non-empty, chooses random direction, pushes word into word-search grid, removes word from current queue, appends removed word to saved bank, repeats.
        If no directions are available, repeats from 4a to find a new square and so on"""
        if valid_directions:
            chosen_direction = random.choice(valid_directions)
            populate_word(BANK[-1], chosen_direction, game, position)
            SAVED_BANK.append(BANK.pop())
        attempts += 1
    if not SAVED_BANK:
        print("I'm sorry, the chosen width and height could not fit the words, please restart and try again :(")
    else:
        """5. Fill rest of spaces with random letters and prints word-search with bank of words to look for"""
        fill_rest(game)
        display_game(game, SAVED_BANK)

