#!/bin/python3

import os

def equalStacks(h1, h2, h3):
    s1 = sum(h1)
    s2 = sum(h2)
    s3 = sum(h3)
    
    while h1 and h2 and h3:
        min_height = min(s1, s2, s3)
        
        while s1 > min_height:
            s1 -= h1.pop(0)
            
        while s2 > min_height:
            s2 -= h2.pop(0)
            
        while s3 > min_height:
            s3 -= h3.pop(0)
        
        if s1 == s2 == s3:
            return s1
    
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
