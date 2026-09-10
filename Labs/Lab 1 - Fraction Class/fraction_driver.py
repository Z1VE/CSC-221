#------------------------------
# NAME : Matthew
# DATE : 9/8/26
# TERM : FALL 2026
# COURSE : CSC 221
# PROJECT : Fraction Class Lab (Driver Test File)
# FILENAME : fraction_driver.py
#------------------------------
from fraction import Fraction

def main():
    INIT_CASES = {
        (1,2):'1/2',
        (2,8):'1/4',
        (0,2):'0',
        (8,2):'4',
        (-1,2):'-1/2',
        (2,-8):'-1/4',
        (0,-2):'0',
        (-8,2):'-4',
        (-8,-2):'4',
    }
    ARITHMETIC_CASES = {
        'negate':[[(1,2),'-1/2'],[(3,9),'-1/3'],[(3,-2),'3/2'],[(-9,-2),'-9/2']],
        'addition':[
    [(1, 2), (1, 2), ('1/1')],
    [(1, 2), (2, 4), ('1/1')],
    [(2, 8), (0, 2), ('1/4')],
    [(-8, -2), (-4, -1), ('8/1')],
    [(-8, -2), (-8, 2), ('0/1')],
    [(2, 8), (1, 4), ('1/2')],
    [(-2, 1), (-5, 3), ('-11/3')]
],
        'subtraction':[
    [(1, 2), (1, 2), '0/1'],
    [(1, 2), (2, 4), '0/1'],
    [(2, 8), (0, 2), '1/4'],
    [(-8, -2), (-4, -1), '0/1'],
    [(-8, -2), (-8, 2), '8/1'],
    [(2, 8), (1, 4), '0/1'],
    [(-2, 1), (-5, 3), '-1/3']
]
,
        'multiplication':[
    [(1, 2), (1, 2), '1/4'],
    [(1, 2), (2, 4), '1/4'],
    [(2, 8), (0, 2), '0/1'],
    [(-8, -2), (-4, -1), '16/1'],
    [(-8, -2), (-8, 2), '-16/1'],
    [(2, 8), (1, 4), '1/16'],
    [(-2, 1), (-5, 3), '10/3']
]
,
        'division':[
    [(1, 2), (1, 2), '1/1'],
    [(1, 2), (2, 4), '1/1'],
    [(-8, -2), (-4, -1), '1/1'],
    [(-8, -2), (-8, 2), '-1/1'],
    [(2, 8), (1, 4), '1/1'],
    [(-2, 1), (-5, 3), '6/5']
]

    }
    RELATIONAL_CASES = {
        'equal':[[(1,2),(1,2),True],[(1,2),(2,4),True],[(2,8),(0,2),False],[(-8,-2),(-4,-1),True],[(-8,-2),(-8,2),False],[(2,8),(1,4),True],[(-2,1),(-5,3),False]],
        'not equal':[[(1,2),(1,2),False],[(1,2),(2,4),False],[(2,8),(0,2),True],[(-8,-2),(-4,-1),False],[(-8,-2),(-8,2),True],[(2,8),(1,4),False],[(-2,1),(-5,3),True]],
        'less than':[[(1,2),(1,2),False],[(1,2),(2,4),False],[(2,8),(0,2),False],[(-8,2),(-4,-1),True],[(-8,-2),(-8,2),False],[(2,8),(6,4),True],[(-2,1),(-1,3),True]],
        'less than or equal':[[(1,2),(1,2),True],[(1,2),(2,4),True],[(2,8),(0,2),False],[(-8,2),(-4,-1),True],[(-8,-2),(-8,2),False],[(2,8),(6,4),True],[(-2,1),(-1,3),True]],
        'greater than':[[(1,2),(1,2),False],[(1,2),(2,4),False],[(2,8),(0,2),True],[(-8,2),(-4,-1),False],[(-8,-2),(-8,2),True],[(2,8),(6,4),False],[(-2,1),(-1,3),False]],
        'greater than or equal':[[(1,2),(1,2),True],[(1,2),(2,4),True],[(2,8),(0,2),True],[(-8,2),(-4,-1),False],[(-8,-2),(-8,2),True],[(2,8),(6,4),False],[(-2,1),(-1,3),False]]
    }
# Shows the initialization working and reduction of fractions as well as symbol handling
    for fraction in INIT_CASES:
        numerator,denominator = fraction
        frac = Fraction(numerator,denominator)

        print(f"The fraction {fraction} should display: {INIT_CASES[fraction]} and it displays: {frac}")

    print('\n-------------ARITHMETIC CASES-------------')


# Shows the results of Arithmetic Operators
    for operator in ARITHMETIC_CASES:
        print(f"\n-------------{operator.upper()}-------------")
        for case in ARITHMETIC_CASES[operator]:
            if len(case) > 2: # checks for every case that isn't negate because our testing list only holds 2 values compared to the others
                frac1 = Fraction(case[0][0], case[0][1])
                frac2 = Fraction(case[1][0], case[1][1])
                expected = case[2]

                op_symbol = (
                    "+" if operator == "addition" else
                    "-" if operator == "subtraction" else
                    "*" if operator == "multiplication" else
                    "/" if operator == "division" else
                    "ERROR"
                )

                # Compute the result and store it in a separate variable
                actual = (
                    frac1 + frac2 if operator == "addition" else
                    frac1 - frac2 if operator == "subtraction" else
                    frac1 * frac2 if operator == "multiplication" else
                    frac1 / frac2 if operator == "division" else
                    "ERROR"
                )
                print(f"The fraction {frac1} {op_symbol} {frac2} should display as {expected} and displays as: {actual} {"\033[32m\033[1mPASS" if expected == str(actual) else "\033[31m\033[1mFAIL"}\033[0m")

            else:
                frac1 = Fraction(case[0][0], case[0][1])
                expected = case[1]

                result = str(-frac1)
                print(f"The fraction {frac1} negated should display as {expected} and displays as: {result} {"\033[32m\033[1mPASS" if expected == str(result) else "\033[31m\033[1mFAIL"}\033[0m")


# Shows the results of all boolean relational operators
    print('\n-------------RELATIONAL CASES-------------')
    for operator in RELATIONAL_CASES:
        print(f"\n-------------{operator.upper()}-------------")
        for case in RELATIONAL_CASES[operator]:
            frac1 = Fraction(case[0][0], case[0][1])
            frac2 = Fraction(case[1][0], case[1][1])
            expected = case[2]

            # Determine the operator string representation for display
            op_symbol = (
                "==" if operator == "equal" else
                "!=" if operator == "not equal" else
                "<" if operator == "less than" else
                "<=" if operator == "less than or equal" else
                ">" if operator == "greater than" else
                ">=" if operator == "greater than or equal" else
                "ERROR"
            )

            # Compute the result and store it in a separate variable
            actual = (
                frac1 == frac2 if operator == "equal" else
                frac1 != frac2 if operator == "not equal" else
                frac1 < frac2 if operator == "less than" else
                frac1 <= frac2 if operator == "less than or equal" else
                frac1 > frac2 if operator == "greater than" else
                frac1 >= frac2 if operator == "greater than or equal" else
                "ERROR"
            )

            print(f"The fraction {frac1} {op_symbol} {frac2} should display as {expected} and displays as: {actual} {"\033[32m\033[1mPASS" if expected == actual else "\033[31m\033[1mFAIL"}\033[0m")

    # Because we call __reduce() in our init we can't see what the original fraction looked like

# OLD CODE

    # get_denominator()
    # print(f"Fraction 1 denominator should display 2:        {frac1.get_denominator()}")
    # print(f"Fraction 2 denominator should display 4:        {frac2.get_denominator()}")
    # print(f"Fraction 6 denominator should display -4:       {frac6.get_denominator()}")
    # print(f"Fraction 9 denominator should display -1:       {frac9.get_denominator()}")
    # print('\n')
    #
    # # get_numerator
    # print(f"Fraction 1 denominator should display 1:        {frac1.get_numerator()}")
    # print(f"Fraction 2 denominator should display 1:        {frac2.get_numerator()}")
    # print(f"Fraction 6 denominator should display 1:       {frac6.get_numerator()}")
    # print(f"Fraction 9 denominator should display -4:       {frac9.get_numerator()}")

#     print("Creating fractions : (1,2), (2,8), (0,2), (8,2), (-1,2), (2,-8), (0, -2), (-8, 2), and (-8, -2)\n")
#     frac1 = Fraction(1,2)
#     frac2 = Fraction(2,8)
#     frac3 = Fraction(0,2)
#     frac4 = Fraction(8,2)
#     frac5 = Fraction(-1,2)
#     frac6 = Fraction(2,-8)
#     frac7 = Fraction(0,-2)
#     frac8 = Fraction(8,2)
#     frac9 = Fraction(-8,-2)
#
# # Testing all functions and if they display correctly
#     print(f"Fraction 1 should read 1/2:     {frac1}")
#     print(f"Fraction 2 should read 1/4:     {frac2}")
#     print(f"Fraction 3 should read 0/2:     {frac3}")
#     print(f"Fraction 4 should read 4:       {frac4}")
#     print(f"Fraction 5 should read -1/2:    {frac5}")
#     print(f"Fraction 6 should read -1/4:    {frac6}")
#     print(f"Fraction 7 should read 0:       {frac7}")
#     print(f"Fraction 8 should read 4:       {frac8}")
#     print(f"Fraction 9 should read 4:       {frac9}")

# Testing all Fraction object methods

if __name__ == '__main__':
    main()
