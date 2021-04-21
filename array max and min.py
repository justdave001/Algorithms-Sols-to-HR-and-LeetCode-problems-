import math
import os
import random
import re
import sys
"""
# Complete the miniMaxSum function below.
arr = list(map(int, input().rstrip().split()))
def miniMaxSum(arr):
      sort = sorted(arr)
      print(sum(sort[:4]), sum(sort[-4:]) )

if __name__ == '__main__':
    miniMaxSum(arr)
"""
"""
array = list(map(int, input().rstrip().split()))
a =0
for i in array:
    a += i
print(a)
"""
candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))
arri = []
def birthdayCakeCandles(candles):
    # Write your code here
    array = sorted(candles)
    for i in range(candles_count):
       arri.append(candles)
       arr = str(array[candles_count])
       print(arr)
    
    
if __name__ == '__main__':
    birthdayCakeCandles(candles)
