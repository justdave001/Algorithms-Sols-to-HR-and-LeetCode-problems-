"""
n = int(input("Number of rows:"))
m = int(input("Number of cols:"))


matrix = []
for i in range(n):
    for j in range(m):
        matrix.append(int(input()))

https://prepinsta.com/goldman-sachs/technical-test/coding-questions/
https://www.csestack.org/group-anagrams-list-coding-challenge/
https://www.geeksforgeeks.org/tag/goldman-sachs/
https://www.youtube.com/watch?v=hPUSrHPdo-4
https://www.csestack.org/goldman-sachs-online-coding-test-questions/
"""
arr=[]
arr2=[]
n = int(input())
for _ in range(n):
    arr.append(int(input()))
print(arr)
def counterr(arr):
  maxloss=0
  for i in range(n-1):
    for j in range(len(arr)-1-i):
        arr2.append(arr[i]-arr[i+j+1])
   # arr.pop(i)
  maxloss = max(arr2)
  print(maxloss)
  if maxloss < 0:
        print(0)
if __name__=="__main__":
    counterr(arr)
        
    


