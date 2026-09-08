#------------------------------
# NAME : Matthew
# DATE : 9/8/26
# TERM : FALL 2026
# COURSE : CSC 221
# PROJECT : Fraction Class Lab
# FILENAME : fraction.py
#------------------------------
from fraction import Fraction

def main():
    print("Creating fractions : (1,2), (2,8), (0,2), (8,2), (-1,2), (2,-8), (0, -2), (-8, 2), and (-8, -2)\n")
    frac1 = Fraction(1,2)
    frac2 = Fraction(2,8)
    frac3 = Fraction(0,2)
    frac4 = Fraction(8,2)
    frac5 = Fraction(-1,2)
    frac6 = Fraction(2,-8)
    frac7 = Fraction(0,-2)
    frac8 = Fraction(8,2)
    frac9 = Fraction(-8,-2)

# Testing all functions and if they display correctly
    print(f"Fraction 1 should read 1/2:     {frac1}")
    print(f"Fraction 2 should read 1/4:     {frac2}")
    print(f"Fraction 3 should read 0/2:     {frac3}")
    print(f"Fraction 4 should read 4:       {frac4}")
    print(f"Fraction 5 should read -1/2:    {frac5}")
    print(f"Fraction 6 should read -1/4:    {frac6}")
    print(f"Fraction 7 should read 0:       {frac7}")
    print(f"Fraction 8 should read 4:       {frac8}")
    print(f"Fraction 9 should read 4:       {frac9}")

# Testing all Fraction object methods

    INIT_CASES = {
        (2,4):"/"



    }
    ARITHMETIC_CASES = {
        'negate':[],
        'addition':[],
        'subtraction':[],
        'multiplication':[],
        'division':[]
    }
    RELATIONAL_CASES = {
        'equal':[[(),(),True],[],[],[]],
        'not equal':[],
        'less than':[],
        'less than or equal':[],
        'greater than':[],
        'greater than or equal':[]
    }

    for fraction in fractions:
        print()
    # get_denominator()
    print(f"Fraction 1 denominator should display 2:        {frac1.get_denominator()}")
    print(f"Fraction 2 denominator should display 4:        {frac2.get_denominator()}")
    print(f"Fraction 6 denominator should display -4:       {frac6.get_denominator()}")
    print(f"Fraction 9 denominator should display -1:       {frac9.get_denominator()}")
    print('\n')

    # get_numerator
    print(f"Fraction 1 denominator should display 1:        {frac1.get_numerator()}")
    print(f"Fraction 2 denominator should display 1:        {frac2.get_numerator()}")
    print(f"Fraction 6 denominator should display 1:       {frac6.get_numerator()}")
    print(f"Fraction 9 denominator should display -4:       {frac9.get_numerator()}")



if __name__ == '__main__':
    main()
