# ============================================================
# PROGRAMMER:..... Matthew Rumph
# COURSE:......... CSC 221
# TERM:........... FALL 2026
# PROJECT:........ Recipe Conversion Program
# FILENAME:....... recipeConversion.py
# ============================================================
from fraction import *


def get_file():
    """
    Gets filename from user and attempts to open file up to three times.
    If the file exceeds three attempts of opening successfully,
    an IO exception is raised
    :return: Tuple of the filename entered by the user and the open file object
    """
    # loop 3 times
    for i in range(3):
        try:
            filename = input("Recipe Filename: ")
            input_file = open(filename)
            return filename, input_file
        except FileNotFoundError:
            print("\033[31mThe File was not found. Please try again\033[0m\n")
    raise IOError("\033[31mIOError: You exceeded 3 attempts please verify your file and try again.\033[0m")


# DO NOT CHANGE THE CODE, ONLY COMMENT
def remove_measure(line):
    """
    Returns the given line with any initial digits and fractions (and
    any surrounding blanks) removed
    :param line: str line to be processed
    :return: str line with measurements removed
    """
    k = 0 # count variable to iterate through string
    blank_char = ' ' # defining white space

    while k < len(line) and (line[k].isdigit() or line[k] in ('/', blank_char)): # counts index of string up until there are no digits left and white space following digit
        k = k + 1

    return line[k:] # returns string without our measurements / fractions / digits


# DO NOT CHANGE THE CODE, ONLY COMMENT
def scan_as_fraction(line):
    """
    Scans all digits, including fractions, and returns as a Fraction object
    For example, '1/2' would return as a Fraction value 1/2, '2' would return
    as Fraction 2/1, and '2 1/2' would return as Fraction value 3/2
    :param line: str line to be processed
    :return: Fraction object of the given line's measurement
    """
    completed_scan = False # Stop Variable
    value_as_fraction = Fraction(0, 1)  # temp fraction variable with value of 0

    # iterating through our string and measuring up until we find digits
    while not completed_scan:
        k = 0
        while k < len(line) and line[k].isdigit():
            k = k + 1

        numerator = int(line[:k]) # once we stop at a string or white space we go backwards and set that first number to our numerator because in both cases of it being either a number or a fraction that first digit will be our numerator

        if k < len(line) and line[k] == '/': # finding the denominator half of our fraction by looking for "/"
            k = k + 1
            start = k # set the beginning of our denominator to first digit after the /
            while k < len(line) and line[k].isdigit(): # as long as we don't reach the end and our current value is still a digit we keep looping and adding to our denominator
                k = k + 1

            denominator = int(line[start:k]) # set denominator to found value
        else:
            denominator = 1 # if we don't find a denominator we set it to 1 aka we just found a digit by itself

        value_as_fraction = value_as_fraction + Fraction(numerator, denominator) # we make our fraction object

        if k == len(line): # if we made it to the end of our line we turn our scan to completed
            completed_scan = True
        else: # else we remove our first digit/fraction found and keep looking till the end of our string
            line = line[k:].strip()

            if not line[0].isdigit(): # if we don't see a digit at the first value of a line we've finished our scan
                completed_scan = True

    return value_as_fraction # return sum of values as 1 fraction


def convert_line(line, factor):
    """
    If the line begins with a digit, then returns the line with the value
    incremented by factor, otherwise returns line unaltered
    For example, for a factor of 2, '1/4 cup sugar' returns as '1/2 cup sugar'
    and '2 cups sugar' returns as '4 cups sugar'
    :param line: str line to be processed
    :param factor: int | Fraction factor to change line measurement by
    :return: str processed line
    """
    # your code goes here
    # The idea is that you are going to receive a line of the recipe
    # If you find a digit in the line
    # Scan through the line looking for the fraction and multiply it by the factor to create a new fraction
    # then you need to build the new line by removing the original measurement and putting the new fraction
    # measure in the line
    # Return the new line
    # This function should use scan_as_fraction and remove_measure functions
    if line[0].isdigit():
        fraction = scan_as_fraction(line)
        string_no_fraction = remove_measure(line)
        converted_line = f"{fraction * factor} {string_no_fraction.lstrip()}"
        return converted_line
    else:
        return line





# DO NOT CHANGE ANYTHING BELOW THIS LINE!
# You are responsible for writing the 2 empty functions above and
# adding comments to the other two functions
def main():
    # display welcome
    print("This program will convert a given recipe to a different\n"
          "quantity based on a specified conversion factor. Enter a\n"
          "factor of 1/2 to halve, 2 to double, 3 to triple, etc.\n")

    try:
        # get filename and open file
        filename, input_file = get_file()  # you need to write this function

        # get conversion factor
        factor = input("Enter a conversion factor: ")
        factor = scan_as_fraction(factor)

        # open output file named "conv_" + filename
        output_filename = "conv_" + filename
        output_file = open(output_filename, 'w')

        # convert recipe
        empty_str = ''
        line = input_file.readline()  # you are converting the recipe line by line

        while line != empty_str:  # while we haven't reached the end of the file
            new_line = convert_line(line, factor)  # you need to write this function
            output_file.write(new_line)  # write the new line to the output file
            line = input_file.readline()  # get the next line of the original recipe

        # close files
        input_file.close()
        output_file.close()

        # display completion message
        print(f"Converted recipe in file: {output_filename}")

    except IOError as err_mess:  # catch IOError
        print(err_mess)


if __name__ == '__main__':
    main()
