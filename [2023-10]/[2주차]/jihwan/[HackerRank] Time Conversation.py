#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    isAm = s[len(s)- 2 : len(s)]
    time = s.split(":")
    if isAm >= 24:
        time[0] = time[0] - 24
    print(time)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = "12:01:30PM"

    result = timeConversion(s)

    # fptr.write(result + '\n')
    #
    # fptr.close()
