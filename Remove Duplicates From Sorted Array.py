<<<<<<< HEAD
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                 del (nums[i])
            else:
                i += 1
        return len(nums)
      
=======
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                 del (nums[i])
            else:
                i += 1
        return len(nums)
      
>>>>>>> bb4dee632f7ba40081fd47f4bd4f1033e6577977
