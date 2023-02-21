"""
    Would like to create a game of 'word-search',
    Generates a random M x N grid with random letter of the english alphabet
    Create a list of words that would want to put into the grid in a random order
    Fills in the rest of the grid with random letters
    For simplicity, only do horizontal and vertical (no diagonal)
    And no overlap between words

    How to assign a word onto grid:
    - Pick random square
    - Pick a word
    - Find length of word
    - Check length of squares left, right, above and below of random square picked
    - If length of word less than or equal to length of squares in direction
    - Choose random between viable directions
    - Assign letters of word along direction
    - If not pick another square
    - Repeat until possible
    - 
"""

import numpy as np
import random

# Use Dictionary in refactor
# Shuffle words everytime
bank_of_words = [
    "BENEFIT",
    "PEACE",
    "CLARITY",
    "GROWTH",
    "BALANCE",
    "BEAUTY",
    "CENTRE",
    "GENEROSITY",
    "CHEERFULNESS"
]

# Use ASCII when refactoring
list_letters = [
    "A", "B", "C", "D", "E",
    "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z"
]

GRID_WIDTH = 14
GRID_HEIGHT = 14

def create_empty_grid(height, width):
    return np.zeros((height, width), dtype = str)

def pick_random_square(nested_array):
    height = len(nested_array)
    width = len(nested_array[0])
    x_comp = random.randint(0, width - 1)
    y_comp = random.randint(0, height - 1)
    return {
        "x-index": x_comp,
        "y-index": y_comp
    }

def check_available_squares(grid, position):
    direction_spaces = {
        "up": 1,
        "down": 1,
        "left": 1,
        "right": 1,
    }
    original_x_index = position["x-index"]
    original_y_index = position["y-index"]
    grid_width = len(grid[0])
    grid_height = len(grid)
    original_origin = grid[original_y_index][original_x_index]

    # Up
    origin = original_origin
    x_index = original_x_index
    y_index = original_y_index
    while origin == '':
        if y_index > 0:
            direction_spaces["up"] += 1
            y_index -= 1
            origin = grid[y_index][x_index]
        else:
            break

    # Down
    origin = original_origin
    x_index = original_x_index
    y_index = original_y_index
    while origin == '':
        if y_index < grid_height - 1:
            direction_spaces["down"] += 1
            y_index += 1
            origin = grid[y_index][x_index]
        else:
            break

    # Left
    origin = original_origin
    x_index = original_x_index
    y_index = original_y_index
    while origin == '':
        if x_index > 0:
            direction_spaces["left"] += 1
            x_index -= 1
            origin = grid[y_index][x_index]
        else:
            break

    # Right
    origin = original_origin
    x_index = original_x_index
    y_index = original_y_index
    while origin == '':
        if x_index < grid_width - 1:
            direction_spaces["right"] += 1
            x_index += 1
            origin = grid[y_index][x_index]
        else:
            break

    print("")
    
    return direction_spaces

def fit_word_check(word:str, space_dictionary:dict):
    length_of_word = len(word)
    valid_direction = [lengths[0] for lengths in space_dictionary.items() if lengths[1] >= length_of_word]
    return valid_direction

def populate_word(word:str, direction, grid, square_position:dict):
    match direction:
        case 'up':
            for index, letter in enumerate(word):
                grid[square_position["y-index"] - index][square_position["x-index"]] = letter
        case 'down':
            for index, letter in enumerate(word):
                grid[square_position["y-index"] + index][square_position["x-index"]] = letter
        case 'left':
            for index, letter in enumerate(word):
                grid[square_position["y-index"]][square_position["x-index"] - index] = letter
        case 'right':
            for index, letter in enumerate(word):
                grid[square_position["y-index"]][square_position["x-index"] + index] = letter
    pass

def fill_rest(grid: list):
    for row_index, row_list in enumerate(game):
        grid[row_index] = [random.choice(list_letters) if x == '' else x for x in row_list]
    pass

if __name__ == "__main__":

    # Initialise Empty Grid
    game = create_empty_grid(GRID_HEIGHT, GRID_WIDTH)
    print(game)
    # Populate grid, looping over all words in word bank
    while bank_of_words:

        # Choose random square on grid
        position = pick_random_square(game)
        # print({
        #     "x-coordinate": position["x-index"] + 1,
        #     "y-coordinate": position["y-index"] + 1,
        # })

        # Check how many squares up, down, left and right of position are empty string values
        squares_usable = check_available_squares(game, position)
        #print(squares_usable)

        # Check to see if word can fit in any of these directions
        valid_directions = fit_word_check(bank_of_words[-1], squares_usable)
        #print(valid_directions)

        if valid_directions:
            # Choose random direction
            chosen_direction = random.choice(valid_directions)
            # print({
            #     "direction-selected": chosen_direction,
            #     }, '\n')

            populate_word(bank_of_words[-1], chosen_direction, game, position)
            bank_of_words.pop()
        else:
            print("Could not fit word")

    # Fill rest of spaces with random letters
    fill_rest(game)

    print(game)

