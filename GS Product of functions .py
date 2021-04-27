
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
 
def findingp(n, arr):
    product = 1   
    arr1 = []
    for i in range(n):
        product *= arr[i]
    print(product)
    for j in arr:
        arr1.append(round(product/j))
    return arr1
print(findingp(n, arr))

