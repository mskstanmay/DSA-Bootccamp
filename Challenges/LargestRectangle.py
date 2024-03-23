#!/bin/python3

import os

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(heights):
    stack = []
    maxRectangle = 0
    index = 0

    while index < len(heights):
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            area = heights[top] * width
            maxRectangle = max(maxRectangle, area)

    while stack:
        top = stack.pop()
        width = index if not stack else len(heights) - stack[-1] - 1
        area = heights[top] * width
        maxRectangle = max(maxRectangle, area)

    return maxRectangle


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
