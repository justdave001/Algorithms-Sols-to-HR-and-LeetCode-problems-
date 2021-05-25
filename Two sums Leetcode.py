n = int(input())

nums = []
arr = []
arr1 = []
counter =0
for _ in range(n):
    nums.append(int(input()))
for i in nums:
    arr.append(i)
        
search = int(input())
for i in range(n):
    for j in range(i+1, n):
        counter = arr[i] + arr[j]
        if counter == search:
            arr1.append(i)
            arr1.append(j)
print(arr1)
