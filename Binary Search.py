#***Binary search method**
#https://beyondcorner.com/calculate-time-complexity-algorithms-java-programs/
arr=[]
n = int(input())

for _ in range(n):
    arr.append(int(input()))
numbertosearch = int(input("Input number: "))
def Binary_searching(arr, numbertosearch):
    right = n-1
    left = 0
    midpoint = (right+left)//2
    while left < right:
        if arr[midpoint] == numbertosearch:
            return midpoint
        elif arr[left] == numbertosearch:
            return left
        elif arr[right] == numbertosearch:
            return right
        elif arr[midpoint] < numbertosearch:
            right = midpoint + 1
        elif arr[midpoint] > numbertosearch:
            left = midpoint -1

print(Binary_searching(arr, numbertosearch))
    
