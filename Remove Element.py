<<<<<<< HEAD
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i =0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i +=1 
        return len(nums)
=======
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i =0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i +=1 
        return len(nums)
>>>>>>> bb4dee632f7ba40081fd47f4bd4f1033e6577977
