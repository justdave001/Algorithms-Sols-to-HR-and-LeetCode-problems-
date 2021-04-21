
def house():
    positionofhouse = list(map(int, input().rstrip().split()))
    position_tr = list(map(int, input().rstrip().split()))

    
    numberoffruits = list(map(int, input().rstrip().split()))
    
 
    positionofapp = list(map(int, input().rstrip().split()))
    positionofor = list(map(int, input().rstrip().split()))
    lists=[]
    for i in range(numberoffruits[0]):
          positionofapp[i] = positionofapp[i] + position_tr[0]
          lists.append(positionofapp[i])
    
    
    j=0
    for i in lists:
        if (i >= positionofhouse[0]) and (i<= positionofhouse[1]):
            j = j +1
    print(j)
    lists1=[]
    for i in range(numberoffruits[1]):
         positionofor[i] = positionofor[i] + position_tr[1]
         lists1.append(positionofor[i])
    
    
    k=0
    for i in lists1:
          if (i >= positionofhouse[0]) and (i<= positionofhouse[1]):
             k = k + 1
    print(k)
if __name__ == "__main__":
    house()
