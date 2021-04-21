arr = []
i = 0
name = "aallexx"
print(name.count(name[i]))
"""
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

arr2  = []
def hourglass():
    summ = 0
    for i in range(4):
        for j in range(4):
            summ = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            arr2.append(summ)
     print(max(arr2))
if __name__ == "__main__":
    hourglass()
"""       
