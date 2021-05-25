#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.

nd = input().split()

n = int(nd[0])

d = int(nd[1])

a = list(map(int, input().rstrip().split()))
#print(a[-4])
arr = []
for i in a:
   arr.append(i)

def rotLeft(a, d):
  
    for i in range(n):
        a[i-d] = arr[i]
        
        
    print(' '.join([str(element) for element in a])) 

if __name__ == '__main__':


 rotLeft(a, d)


