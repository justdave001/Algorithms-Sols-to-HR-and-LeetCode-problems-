import collections
x = list(map(int, input().rstrip().split()))
list1 = []
list2 = []
list3 = []
list4 = []
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))


def geTotal(a,b):
    
    for i in range(x[0]):
        list1.append(a[i])
   
    for i in range(x[1]):
        list2.append(b[i])
    
    for  j in range(len(list1)):
        for i in range(1,101):
      
          if i%list1[j]==0:
            list3.append(i)
    

    y =set([x for x in list3 if list3.count(x) == len(a)])

    for j in range(len(list2)):
        for i in range(1,101):
            if list2[j]%i == 0:
                list4.append(i)
    z = set([x for x in list4 if list4.count(x) == len(b)])
    
    print(sorted(z.intersection(y)))
if __name__=="__main__":
    geTotal(a,b)
    

