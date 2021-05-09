class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        arr = []
        if s.count(s[0]) == len(s):
            return True
        for i in set(s):
            counter = s.count(i)%2
            arr.append(counter)
        
        if arr.count(1)>1:
            return False
        else:
            return True
