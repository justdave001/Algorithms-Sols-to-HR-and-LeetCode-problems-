#!/bin/python3
"""
import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    counter = 0
    i = 0
    
    while i < n:
        j = i+1
        print(arr[i])
        if arr[i] != j:
            arr[arr.index(i+1)], arr[i] = arr[i], arr[arr.index(i+1)]
            print(arr[arr.index(i+1)])
            counter +=1
        i += 1
    return(counter)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
"""

#***more Effective Solution ***
import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    counter = 0

    
    for i in range(n):
        while arr[i]-1 != i:
            ele = arr[i]
            arr[ele-1], arr[i] = arr[i], arr[ele-1]
            counter += 1
    return counter
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

