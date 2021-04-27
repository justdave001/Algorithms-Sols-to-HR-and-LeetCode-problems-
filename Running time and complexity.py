T = int(input())
arr = []
arr2 = []
for i in range(T):
    n = int(input())
    arr.append(n)
print(arr)
def testoore(n):
    for j in arr:
     
      for i in range(1, max(arr)+1):
        if j%i == 0:
             arr2.append(i)
      print(arr2)
      if len(arr2)>2 or len(arr2)==1 :
        print("Not Prime")
      else:
            print("Prime")
      arr2.clear()     
if __name__ == "__main__":
    testoore(n)
