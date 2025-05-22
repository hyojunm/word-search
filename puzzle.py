# TODO: fix problem where words are sharing letters in the same/opposite direction
# TODO: add letter frequency analysis for filling in empty spaces
# TODO: implement encoding of puzzle, word list, and solution
# TODO: instead of random placement, take the average of all letters added so far
# TODO: always sharing letters makes the puzzle too easy?
# TODO: prevent additional words from accidentally appearing in the puzzle


import random


# direction values (from *)

# 0 | 1 | 2
# ---------
# 3 | * | 4
# ---------
# 5 | 6 | 7

NORTHWEST = 0
NORTH     = 1
NORTHEAST = 2
WEST      = 3
EAST      = 4
SOUTHWEST = 5
SOUTH     = 6
SOUTHEAST = 7


def validate_list(words):
    if not len(words):
        return 'The list cannot be empty.'

    word_set = []

    for w in words:
        if w in word_set:
            return 'There cannot be duplicate words in the list.'

        for c in w.lower():
            if ord(c) < ord('a') or ord(c) > ord('z'):
                return 'There cannot be words with special characters in the list.'

        word_set.append(w)


def edit_list(words):
    words_mod = []

    for w in words:
        words_mod.append(w.upper())

    return words_mod


def analyze_list(words):
    num_words = len(words)
    num_letters = 0
    max_word_len = 0

    for w in words:
        num_letters += len(w)
        max_word_len = max(max_word_len, len(w))

    return (num_words, num_letters, max_word_len)


def move(row, col, direction, distance):
    if distance > 1:
        row, col = move(row, col, direction, distance - 1)

    if direction == NORTHWEST or direction == NORTH or direction == NORTHEAST:
        row -= 1 # up

    if direction == SOUTHWEST or direction == SOUTH or direction == SOUTHEAST:
        row += 1 # down

    if direction == NORTHWEST or direction == WEST or direction == SOUTHWEST:
        col -= 1 # left

    if direction == NORTHEAST or direction == EAST or direction == SOUTHEAST:
        col += 1 # right

    return (row, col)


def opposite(direction):
    return (7 - direction)


def insert_word(grid, letters, word, row, col, direction):
    curr_row, curr_col = row, col

    for char in word:
        if curr_row < 0 or curr_row >= len(grid):
            return False

        if curr_col < 0 or curr_col >= len(grid[0]):
            return False

        if grid[curr_row][curr_col] != None and grid[curr_row][curr_col] != char:
            return False

        curr_row, curr_col = move(curr_row, curr_col, direction, 1)

    curr_row, curr_col = row, col

    for char in word:
        grid[curr_row][curr_col] = char
        letters.append((char, curr_row, curr_col))

        curr_row, curr_col = move(curr_row, curr_col, direction, 1)

    return True


def is_empty_row(grid, row_index):
    for c in grid[row_index]:
        if c != None:
            return False

    return True


def is_empty_col(grid, col_index):
    for i in range(len(grid)):
        if grid[i][col_index] != None:
            return False

    return True


def trim_puzzle(grid):
    i = 0

    while i < len(grid):
        if is_empty_row(grid, i):
            grid = grid[0:i] + grid[i+1:]
        else:
            i += 1

    i = 0

    while i < len(grid[0]):
        if is_empty_col(grid, i):
            for j in range(len(grid)):
                grid[j] = grid[j][0:i] + grid[j][i+1:]
        else:
            i += 1

    return grid


def print_puzzle(grid):
    for row in grid:
        for letter in row:
            print('*' if letter is None else letter, end='')

        print()


def create_puzzle(words):
    words = edit_list(words)
    num_words, num_letters, max_word_len = analyze_list(words)

    grid = []
    letters = []

    for i in range(num_letters):
        grid.append([None for _ in range(num_letters)])

    while len(words):
        word = random.choice(words)
        success = False

        for i in range(len(letters)):
            char, row, col = letters[i]

            if char not in word:
                continue

            # randomize these two values if possible
            char_index = word.index(char)
            direction = random.randint(0, 7)
            
            start_row, start_col = move(row, col, opposite(direction), char_index)
            
            if insert_word(grid, letters, word, start_row, start_col, direction):
                success = True
                break

        while not success:
            start_row = random.randint(0, len(grid) - 1)
            start_col = random.randint(0, len(grid[0]) - 1)
            direction = random.randint(0, 7)

            if insert_word(grid, letters, word, start_row, start_col, direction):
                success = True

        words.remove(word)

    grid_mod = trim_puzzle(grid)

    for i in range(len(grid_mod)):
        for j in range(len(grid_mod[0])):
            if grid_mod[i][j] is None:
                grid_mod[i][j] = chr(ord('A') + random.randint(0, 25))

    return grid_mod


if __name__ == '__main__':
    words = ['apple', 'banana', 'orange', 'cherry', 'kiwi', 'watermelon']
    print_puzzle(create_puzzle(words))
