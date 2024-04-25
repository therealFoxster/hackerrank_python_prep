#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = list(s)
    for i in range(len(s)):
        if i == 0 and s[i] != " ":
            s[i] = s[i].upper()
        elif s[i].isalpha and s[i - 1] == " ":
            s[i] = s[i].upper()
    return "".join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
