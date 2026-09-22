# ---------------------------------------------
# NAME.....: Matthew Rumph
# TERM.....: FALL 2026
# COURSE...: CSC 221
# DATE.....: 09/22/2026
# PURPOSE..: Test driver for FootMeasure object class
# FILENAME.: FootMeasure_driver.py
# ---------------------------------------------

from FootMeasure import *


# Initialize different cases

INIT_CASES = {
    (1,1):"1 ft. 1 in.",
    (1,2):"1 ft. 2 in.",
    (1,3):"1 ft. 3 in.",
    (2,1):"2 ft. 1 in.",
    # Only feet
    (6,0):"6 ft.",
    (1,0):"1 ft.",
    (2,0):"2 ft.",
    (3,0):"3 ft.",
    # Only inches
    (0,1):"1 in.",
    (0,2):"2 in.",
    (0,3):"3 in.",
    # More than 12 inches
    (0,12):"1 ft.",
    (1,12):"2 ft.",
    (2,13):"3 ft. 1 in.",
    (3,72):"9 ft.",
    (0,72):"6 ft.",
    (0,74):"6 ft. 2 in.",
    # (0,0)
    (0,0):"0 ft. 0 in."
}

# Mathematical operator methods

# Addition

ADDITION_CASES = {
    ((1,2),(1,3)): "2 ft. 5 in.",
    ((1,6),(4,3)): "5 ft. 9 in.",
    ((0,5),(1,12)): "2 ft. 5 in.",
    ((3,5),(1,13)): "5 ft. 6 in.",
    ((1,10),(1,12)): "3 ft. 10 in.",
    ((2,11),(1,12)): "4 ft. 11 in.",
    ((3,12),(1,12)): "6 ft.",
    ((4,13),(1,12)): "7 ft. 1 in.",
    ((0, 5), (0, 3)): "8 in.",
    ((0, 0), (0, 0)): "0 ft. 0 in.",
}

RELATION_CASES = {
    (1,2):(1,2),
    (1,3):(1,2),
    (8,4):(8,0),
    (6,0):(0,72),
    (6,2):(0,74),
    (6,0):(3,36),
    (0,0):(0,0),
    (0,9):(1,9),
    (1,10):(1,11),
}

RELATION_RESULTS = {
    "Equal":[True,False,False,True,True,True,True,False,False],
    "Not Equal":[False,True,True,False,False,False,False,True,True],
    "Greater than":[False,True,True,False,False,False,False,False,False],
    "Greater than or equal to":[True,True,True,True,True,True,True,False,False],
    "Less than":[False,False,False,False,False,False,False,True,True],
    "Less than or equal to":[True,False,False,True,True,True,True,True,True]
}

OPERATOR_MAP = {
    "Equal": lambda x,y: x==y,
    "Not Equal": lambda x,y: x!=y,
    "Greater than": lambda x,y: x>y,
    "Greater than or equal to": lambda x,y: x>=y,
    "Less than": lambda x,y: x<y,
    "Less than or equal to": lambda x,y: x<=y,
}

for operand in RELATION_RESULTS:
    symbol = OPERATOR_MAP[operand]   # NOT DONE HERE
    print(symbol)
    count = 0
    for num1 in RELATION_CASES:
        measureA = FootMeasure(num1[0],num1[1])
        measureB = FootMeasure(RELATION_CASES[num1][0],RELATION_CASES[num1][1])
        expected = RELATION_RESULTS[operand][count]
        result = 0
        count += 1
        print(f"{measureA} INSERT OPERATOR HERE {measureB},{result}")

for measurement in INIT_CASES:
    result = FootMeasure(measurement[0],measurement[1])
    expected = INIT_CASES[measurement]
    pass_fail = "\033[32m\033[1mPASS\033[0m" if expected == str(result) else "\033[31m\033[1mFAIL\033[0m"
    print(f"Created FootMeasure object. Got: {result} expected: {expected} {pass_fail}")

for measurement in ADDITION_CASES:
    a = FootMeasure(measurement[0][0],measurement[0][1])
    b = FootMeasure(measurement[1][0],measurement[1][1])
    result = a + b
    expected = ADDITION_CASES[measurement]
    pass_fail = "\033[32m\033[1mPASS\033[0m" if expected == str(result) else "\033[31m\033[\033[0m"

    print(f"Operation: {str(a):<3} + {str(b):<3} | Expected: {expected:<5} | Got: {str(result):<5} | {pass_fail}")


