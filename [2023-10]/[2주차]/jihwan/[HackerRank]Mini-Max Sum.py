#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    maxNum = sum(arr[1:])
    minNum = sum(arr[:len(arr) - 1])
    return minNum, maxNum

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    print(' '.join(map(str, miniMaxSum(arr))))
