import requests
import random
import numpy as np
import string

def get_word_bank(url:str) -> list:
    """Pull list of usable words from remote dictionary"""
    try:
        response = requests.get(url)
        return response.content.splitlines()
    except Exception as e:
        print(e)

def pick_random_words(bank:list, number_of_words:int) -> list:
    """Pick X number of words at random from available bank of words, converts from bytes string to string and uppercase all letter"""
    list_of_words = [random.choice(bank).decode("utf-8").upper() for i in range(number_of_words)]
    return list_of_words

def check_valid_entry_integer(user_input:str) -> bool:
    """Check if user input (as an integer) is divisible by 1, then flag as True, converse returns False"""
    try:
        if int(user_input)%1 == 0:
            return True
        else:
            return False
    except Exception as e:
        print(e)

def create_empty_grid(width:int, height:int) -> list:
    """Initialise height by width nested list with empty strings"""
    return np.zeros((height, width), dtype = str)

def pick_random_square(width:int, height:int) -> dict:
    """Returns dictionary of a random pair of indices given a set height and width"""
    x_comp = random.randint(0, width - 1)
    y_comp = random.randint(0, height - 1)
    return {
        "x-index": x_comp,
        "y-index": y_comp
    }

def check_available_squares(grid:list, position:dict, width:int, height:int) -> dict:
    """Initially at a given square,, regardless of direction you have one square available, being that square you are on"""
    direction_spaces = {
        "up": 1,
        "down": 1,
        "left": 1,
        "right": 1,
    }
    """Keeping track of the starting point"""
    origin_x, origin_y = position["x-index"], position["y-index"]
    origin = grid[origin_y][origin_x]

    """Traverse Up"""
    """Take current position to start at the origin and change as it traverses. Resets current position back to origin per direction"""
    curr_position = origin
    x_index = origin_x
    y_index = origin_y
    """Essentially counts how many empty strings in a particular direction, stops at edge of grid"""
    while curr_position == '':
        if y_index > 0:
            direction_spaces["up"] += 1
            y_index -= 1
            curr_position = grid[y_index][x_index]
        else:
            break

    """Traverse Down"""
    curr_position = origin
    x_index = origin_x
    y_index = origin_y
    while curr_position == '':
        if y_index < height - 1:
            direction_spaces["down"] += 1
            y_index += 1
            curr_position = grid[y_index][x_index]
        else:
            break

    """Traverse Left"""
    curr_position = origin
    x_index = origin_x
    y_index = origin_y
    while curr_position == '':
        if x_index > 0:
            direction_spaces["left"] += 1
            x_index -= 1
            curr_position = grid[y_index][x_index]
        else:
            break

    """Traverse Right"""
    curr_position = origin
    x_index = origin_x
    y_index = origin_y
    while curr_position == '':
        if x_index < width - 1:
            direction_spaces["right"] += 1
            x_index += 1
            curr_position = grid[y_index][x_index]
        else:
            break
    return direction_spaces

def fit_word_check(word:str, space_dictionary:dict) -> list:
    """Returns list of directions where the number of squares in a particular direction is at least the length of the word"""
    length_of_word = len(word)
    valid_direction = [lengths[0] for lengths in space_dictionary.items() if lengths[1] >= length_of_word]
    return valid_direction

def populate_word(word:str, direction:str, grid:list, square_position:dict) -> None:
    """For a given direction, function appends each letter of the selected word in that direction"""
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

def fill_rest(grid:list) -> None:
    """Populates rest of the grid with letters"""
    for row_index, row_list in enumerate(grid):
        grid[row_index] = [random.choice(list(string.ascii_uppercase)) if x == '' else x for x in row_list]
    pass

def display_game(grid:list, bank_of_words:list) -> None:
    """Prints final game"""
    print(f"Here are the words you need to find:\n{bank_of_words}")
    print(f"And here is your word-search:\n{grid}\nEnjoy!")
    pass
