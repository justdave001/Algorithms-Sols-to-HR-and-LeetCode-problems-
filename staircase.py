import math
import os
import random
import re
import sys

# Complete the staircase function below.
n = int(input())

def staircase(n):
    a = 0
    b = n
    for i in range(n):
        a += 1
        
        b -= 1
        print(" "*b + "#"*a)

   
if __name__ == '__main__':
    staircase(n)
