class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x==0:
            return True
        elif x >0:
            number = x
            reverse = []
            while number >0:
                dig = number%10
                reverse.append(dig)
                number = number // 10
            if reverse[::-1] == reverse:
                return True
            else:
                return False
