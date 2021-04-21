


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

x = int(input("search"))
def search(arr, x):
    if x in arr:
        return "YES"
    else:
        return "NO"
print(search(arr, x))
