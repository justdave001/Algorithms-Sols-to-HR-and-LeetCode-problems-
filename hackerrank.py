# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER k
#to find if number is present in a list
'''
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
    
k = int(input())
def findNumber(l, k):
    # Write your code here
    l = sorted(l)
    if k in l:
        return "YES"
    else:
        return "NO"
print(findNumber(l,k))
'''

#to find odd numbers in a range
'''
l = int(input())
r = int(input())

for i in range(l, r+1): 
    if i%2 != 0:
        print(i)
'''
'''
a = [1,2,2,3,4]
b=set(a)
print(b)
n = int(input())
ar = []
def sockMerchant(n, ar):
    for i in range(n):
        ar.append(int(input()))
    pairs = 0
    color = set()
    for i in range(len(ar)):
        if ar[i] not in color:
          color.add(ar[i])
    print(len(color))
'''
'''
        else:
            
            pairs += 1
            color.remove(ar[i])
            '''
'''
   
sockMerchant(n, ar)
'''
'''
arr = [[2,2,3],
          [4,5,6],
          [7,8,9]]
i,j = 0,len(arr)-1
while i<len(arr):
    print(arr[i][j])
    i +=1
    j -=1

'''
"""
c = list(map(int, input().rstrip().split()))
lists = []
j = 0
for i in range(c[0]):
    j = j+1
    lists.append(j)
print(lists)
    
"""

  
 
