<<<<<<< HEAD
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        sortedd = list(sorted(nums1))
        if len(sortedd) %2 != 0:
            indexx = int(len(sortedd)/2)
            return sortedd[indexx]
        elif len(sortedd) %2 == 0:
            leftm = int(len(sortedd)/2-1)
            right = leftm+1
            return ((sortedd[leftm]+sortedd[right])/2)
=======
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        sortedd = list(sorted(nums1))
        if len(sortedd) %2 != 0:
            indexx = int(len(sortedd)/2)
            return sortedd[indexx]
        elif len(sortedd) %2 == 0:
            leftm = int(len(sortedd)/2-1)
            right = leftm+1
            return ((sortedd[leftm]+sortedd[right])/2)
>>>>>>> bb4dee632f7ba40081fd47f4bd4f1033e6577977
