# CSC-221 Coursework
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/Z1VE/CSC-221)

This repository contains coursework for the CSC-221 course at Cape Fear Community College (CFCC). It showcases assignments and labs completed using Python, focusing on object-oriented programming and algorithmic problem-solving.

## Projects

### Assignment 1: Mad Libs Game

A command-line program that generates a Mad Libs story. The user provides a text file as a template, and the script identifies placeholders (e.g., `<noun>`, `<verb>`). It then prompts the user for words to fill in the blanks and generates a new story, which can be saved to a file and displayed on the screen.

#### Features
- Reads story templates from user-specified files.
- Parses tokens (e.g., `<noun>`, `<adjective-phrase>`) to request user input.
- Cleans tokens to create grammatically correct prompts (e.g., "Please Type a/an...").
- Saves the resulting story to a new file.
- Allows the user to play again with a new story.

#### How to Run
```bash
python "Assignments/Assignment 1 - Madlibs/Madlibs.py"
```

### Lab 0: Fraction Class

A Python class that represents a mathematical fraction, complete with support for standard arithmetic and relational operations. The class ensures that fractions are always stored in their simplest, reduced form.

#### Features
- Initializes a `Fraction` object with a numerator and denominator.
- Automatically reduces fractions to their simplest form using the Greatest Common Divisor (GCD).
- Handles negative signs correctly by standardizing them in the numerator.
- Overloads arithmetic operators: `+`, `-`, `*`, `/`.
- Overloads relational operators: `==`, `!=`, `<`, `<=`, `>`, `>=`.
- Includes robust error handling for `TypeError` (non-integer inputs) and `ZeroDivisionError`.

#### Testing
The `fraction_driver.py` script serves as a comprehensive test suite. It runs a wide array of test cases for initialization, arithmetic operations, and relational comparisons, printing a color-coded `PASS` or `FAIL` status for each test to verify the correctness of the `Fraction` class.

#### How to Run the Test Driver
```bash
python "Labs/Lab 0 - Fraction Class/fraction_driver.py"
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.