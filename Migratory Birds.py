arr_count = int(input().strip())
phonebook = {}
arr = list(map(int, input().rstrip().split()))
new = []
def migratoryBirds(arr):
    i = 0
    while i in range(arr_count-1):
         i += 1
         count = 0 
         j = -1
         while j in range(-1, arr_count-1):
            j += 1
           
            if i == arr[j]:
             count += 1
         new.append(count)
         
    
    r = max(new)
    
    k = 0
    while k in range(arr_count-1):
          k += 1
         
          phonebook[k] = new[k-1]
    
    l1 = list(phonebook.values())
    l2 = list(phonebook.keys())
    

    position = l1.index(r)
    print(l2[position])
   

if __name__ == '__main__':
    migratoryBirds(arr)
