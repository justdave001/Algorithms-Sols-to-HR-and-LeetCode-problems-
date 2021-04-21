import math
import os
import random
import re
import sys
n = int(input())

scores = list(map(int, input().rstrip().split()))

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maxi=scores[0]
    mini=scores[0]
    maxcount =0
    mincount=0
    for i in range(len(scores)):
        if(scores[i]>maxi):
            maxi = scores[i]
            maxcount+=1
        if(scores[i]<mini):
            mini = scores[i]
            mincount+=1
    print(maxcount, mincount)

if __name__ == '__main__':
   



   breakingRecords(scores)

   
