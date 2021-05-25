<<<<<<< HEAD
class Solution:
    def romanToInt(self, s: str) -> int:
        zipper = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        listed = list(s)
        
        arr = []
        for i in range(len(s)-1):
            
            if zipper[listed[i]] < zipper[listed[i+1]]:
                zipper[listed[i]] *= -1
            
            arr.append(zipper[listed[i]])
            if zipper[listed[i]] < 0:
                zipper[listed[i]] *= -1
        arr.append(zipper[listed[len(s)-1]])
        return sum(arr)
                
=======
class Solution:
    def romanToInt(self, s: str) -> int:
        zipper = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        listed = list(s)
        
        arr = []
        for i in range(len(s)-1):
            
            if zipper[listed[i]] < zipper[listed[i+1]]:
                zipper[listed[i]] *= -1
            
            arr.append(zipper[listed[i]])
            if zipper[listed[i]] < 0:
                zipper[listed[i]] *= -1
        arr.append(zipper[listed[len(s)-1]])
        return sum(arr)
                
>>>>>>> bb4dee632f7ba40081fd47f4bd4f1033e6577977
