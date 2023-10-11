#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    lst = []
    plus = 0
    minus = 0
    for i in arr:
        if i > 0:
            plus += 1
        elif i < 0:
            minus += 1
    lst.append(format(float(plus / len(arr)), ".6f"))
    lst.append(format(float(minus / len(arr)), ".6f"))
    lst.append(format(float((len(arr) - plus - minus) / len(arr)), ".6f"))
    return lst


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    for i in plusMinus(arr):
        print(i)
