
def gettotalx():
    
     nandm = list(map(int, input().rstrip().split()))
     arr = list(map(int, input().rstrip().split()))
     arr1 = list(map(int, input().rstrip().split()))
     for i in range(nandm[0]+1):
          arrr = ([],)*i
     arrr1 = []
    # j = range(1, 100)
     for i in range(nandm[1]):
             for j in range(2,101):
                 if arr1[i]%j == 0:
                     arrr1.append(j)
     newset = set(arrr1)
     print(newset)
     for i in range(nandm[0]):
      for j in range(2, 101):
         if (j%arr[i]==0):
             arrr.append(j)
     neww = set(arrr)
     return neww
    
if __name__ == "__main__":
    gettotalx()


