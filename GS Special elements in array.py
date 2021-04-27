m = int(input("Enter number of rows:"))
n = int(input("Enter number of columns:"))

matrix =[]
arr1 = []
arr2=[]
arr3 = []
for row in range(m):
    outer = []
    for column in range(n):
        outer.append(int(input()))
    matrix.append(outer)
for i in range(m):
    for j in range(n):
        arr1.append(matrix[i][j])
    for number in arr1:
        if number == max(arr1) or number == min(arr1):
            arr3.append(number)
    arr1.clear()
for i in range(n):
    for j in range(m):
        arr2.append(matrix[j][i])
    for numbers in arr2:
        if numbers == max(arr2) or numbers == min(arr2):
            arr3.append(numbers)
    arr2.clear()
setted = set(arr3)
print("\n")
print(len(setted))
