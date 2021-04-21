def kangaroo():
    x1v1x2v2 = list(map(int, input().rstrip().split()))
    
    j = ""
   
    
    
        
    j = "NO"
    for i in range(10000000):
        if (x1v1x2v2[0])+(x1v1x2v2[1]*i) == (x1v1x2v2[2])+(x1v1x2v2[3]*i):
                j = "YES"
        
    print(j)
if __name__ == "__main__":
     kangaroo()
       
