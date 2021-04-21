#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
nk = input().split()

n = int(nk[0])

k = int(nk[1])

ar = list(map(int, input().rstrip().split()))
arr = []
def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
         ar[0], ar[i] = ar[i], ar[0]
         
         for j in range(n-1): 
          temp = ar[0]+ar[j+1]
          if temp%k == 0:
            count += 1
    print(count/2)
       
if __name__ == '__main__':
    

   

     divisibleSumPairs(n, k, ar)

   
