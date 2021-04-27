#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
t = int(input())
arr = []
for t_itr in range(t):
    n = int(input())

    q = list(map(int, input().rstrip().split()))
    arr.append(q)

def minimumBribes(q):
    
    
    for i in range(t):
        counter = 0
        sortedd = list(sorted(arr[i]))
        arrr = []
        w = ""
        for j in arr[i]:
            
            #print(j)
            diff = sortedd.index(j)- arr[i].index(j)
            if sortedd.index(j) > arr[i].index(j)  and diff <=2:
              counter += diff
            
            if sortedd.index(j) > arr[i].index(j)   and diff >2:
                w = "Too chaotic"
                
        arrr.append(counter)
        arrr.append(w) 
    
       
        if  "Too chaotic" in arrr:
                arrr = "Too chaotic" 
                print(arrr)
        if "Too chaotic" not in arrr:
           for i in arrr:
            if i != "":
              print(i)
            
           
                
      
                
   # print(sortedd)
    #print(q)
    
   
if __name__ == '__main__':
    
  minimumBribes(q)

