<<<<<<< HEAD
class Solution:
    def maxArea(self, height: List[int]) -> int:
       i = 0
       j = len(height)-1
       maximum = 0
       while i < j:
         maximum = max(maximum, min(height[i], height[j])*(j-i))
         print(maximum)
         if height[i] < height[j]:
           i += 1
           
         else:
            j -= 1
            
            
       return maximum
=======
class Solution:
    def maxArea(self, height: List[int]) -> int:
       i = 0
       j = len(height)-1
       maximum = 0
       while i < j:
         maximum = max(maximum, min(height[i], height[j])*(j-i))
         print(maximum)
         if height[i] < height[j]:
           i += 1
           
         else:
            j -= 1
            
            
       return maximum
>>>>>>> bb4dee632f7ba40081fd47f4bd4f1033e6577977
