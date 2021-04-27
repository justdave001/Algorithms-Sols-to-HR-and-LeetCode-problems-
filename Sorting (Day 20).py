
import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

def sorting(n):
    counter=0
    for i in range(n-1):
        for j in range(n-1):
           if a[j] > a[j+1]:
             a[j], a[j+1] = a[j+1], a[j]
             counter +=1  
    print(counter)
if __name__ =="__main__":
    sorting(n)
            
            
            
