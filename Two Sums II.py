<<<<<<< HEAD
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        loww, high = 0, len(numbers)-1
        while loww < high:
            number = numbers[loww] + numbers[high]
            if number == target:
                return[loww+1, high+1]
            elif number < target: loww += 1
            else:
                 high -= 1
        return[-1,-1]

=======
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        loww, high = 0, len(numbers)-1
        while loww < high:
            number = numbers[loww] + numbers[high]
            if number == target:
                return[loww+1, high+1]
            elif number < target: loww += 1
            else:
                 high -= 1
        return[-1,-1]

>>>>>>> bb4dee632f7ba40081fd47f4bd4f1033e6577977
