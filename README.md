# WordSearch

A quick game of word-search I created for fun. Currently in development

# Plan:

Would like to create a game of 'word-search',
Generates a random M x N (integers) grid with random letter of the english alphabet
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

# Further Developments:

- Implement a Command Line Interface (CLI) to enable user to skip prompts and insert their chosen number of words, width and height straight away
- Add a function to calculate a suggestion for size of grid given the number of words. Measures length of longest word and total number of letters in whole bank of words.
- Reduce code repetition in user prompts, create a function to take care of asking for user input and looping until valid
- Certain words in bank not super interesting like "as", omit these from available words by checking length of words in selected list and redrawing
- Implement diagonal word population, not too difficult of an extension just extra lines of code
- Implement crossover words, this is a challenge! When checking for available squares given a current position, if the moment a non-empty string is reached, if that letter matches the letter of the word you are checking for, bingo, and continue counting available squares past that square.
- Could ask the user if they would like to reroll their choice of words
- Create unit tests to test validity of the game
- Use external library for better visuals for the final print/takes user to a webpage/exports a sheet to be printed off
