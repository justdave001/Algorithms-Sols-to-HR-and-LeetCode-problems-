<<<<<<< HEAD
class Solution:
    def intToRoman(self, num: int) -> str:
        zipper = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]
        arr = []
        for numb, roman in zipper:
            if num == 0:
                break
            
            count, num = divmod(num, numb)
            arr.append(roman * count)
        return ''.join(arr)
=======
class Solution:
    def intToRoman(self, num: int) -> str:
        zipper = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]
        arr = []
        for numb, roman in zipper:
            if num == 0:
                break
            
            count, num = divmod(num, numb)
            arr.append(roman * count)
        return ''.join(arr)
>>>>>>> bb4dee632f7ba40081fd47f4bd4f1033e6577977
