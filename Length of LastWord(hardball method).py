class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        listed = list(s)
            
        j = len(s)-1
        if s[j] != " ":
            while j>0:
                if s[j] != " ":
                        counter += 1
                        j -= 1
                elif s[j] == " ":
                        break

        elif (s[len(s)-1]) == " ":
            while j >-1:
                if s[j] == " ":
                    j -= 1
                elif s[j].isalpha():
                    counter += 1
                    j -= 1
                    if s[j] == " ":
                        break
        return counter
