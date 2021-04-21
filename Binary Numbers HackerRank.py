n=int(input())
j = []
while n >0:
    remainder =  n%2
    n = int(n/2)
    j.append(remainder)
#print(j)
arr = []
counter =1
for i in range(len(j)-1):
    if j[i] == 1 and (j[i]==j[i+1]):
        counter += 1
    if j[i+1] ==0:
           counter = 1
    arr.append(counter)
print(max(arr))        
