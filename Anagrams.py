n = int(input("Input length of list:"))
arr = []
        
for _ in range(n):
        arr.append(input("input:"))
setted  = set(arr)

anagramed = [''.join(sorted(x)) for x in arr]

finalarr = []
for aword in set(anagramed):
    index = [i for i,x in enumerate(anagramed) if x == aword]
    
    newarr = []
    for i in index:
        newarr.append(arr[i])
    finalarr.append(newarr)
    print(finalarr)
