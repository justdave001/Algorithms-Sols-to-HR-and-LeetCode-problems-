"""
m = int(input())
arr = list(map(int, input().rstrip().split()))
arr2 = []
arr3 = []
arr4 = []

final2 = []
n = int(input())
arr1 = list(map(int, input().rstrip().split()))
def sorting(arr, arr1):
    arr
    reverse = list(reversed(sorted(arr)))
   
    counter = 1
    counter1 = 1
    arr2.append(counter)
    arr4.append(counter1)
    i =0
    while i < (len(reverse)-1):
        if reverse[i] == reverse[i+1]:
            counter
            arr2.append(counter)
        if reverse[i] > reverse[i+1]:
            counter += 1
            arr2.append(counter)
        i +=1
        
    reverse1 = list(reversed(sorted(arr1)))
    
    zipped = list(zip(arr2,reverse))
   
   
    
    w = 0
    while w < (len(reverse1)-1):
        final = [] 
        for i,x in zipped:
            if reverse1[w] >= x:
              final.append(i)
        if len(final) > 0:
         final2.append(min(final))
        w += 1  
    for i in reverse1:
      final = []  
      if i<min(reverse):
            counter += 1
            final.append(counter)
    if len(final) > 0:
     final2.append(min(final))
    kl = list(reversed(final2))
    i = 0
    while i < len(kl):
        print(kl[i])
        i += 1

if __name__ == "__main__":
    sorting(arr, arr1)
"""
def climbingLeaderboard(ranked, player):
    ranked = sorted(list(set(ranked)), reverse=True)
    player = sorted(player, reverse=True)
    
    l=len(ranked)
    j=0
    
    ans=[]
    for i in range(len(player)):
        while j<l and player[i]<ranked[j]:
            j+=1
        
        ans.append(j+1)
        
    return ans[::-1]
   
