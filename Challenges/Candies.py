#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def candies(n, arr):
    # Initialize candies array with 1 candy for each student
    candies_arr = [1] * n

    # Scan from left to right, update candies based on left neighbor
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            candies_arr[i] = candies_arr[i - 1] + 1

    # Scan from right to left, update candies based on right neighbor
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            candies_arr[i] = max(candies_arr[i], candies_arr[i + 1] + 1)

    # Total candies needed is the sum of candies for each student
    total_candies = sum(candies_arr)
    return total_candies


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
