class Solution:
    def reverse(self, x: int) -> int:

        arr = []
        for i in str(abs(x)):
            arr.append(i)
        
        reverse = list(reversed(arr))
        stringed = ''.join(reverse)
        integered = int(stringed)
        if x <0:
            integered *=-1
        if integered < -(2**31) or integered>(2**31)-1: 
             integered = 0
        return integered
