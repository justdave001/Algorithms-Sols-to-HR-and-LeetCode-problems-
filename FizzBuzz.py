<<<<<<< HEAD
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [0]*n
        for i in range(1, n+1):
            if i%15 == 0:
                answer[i-1]= "FizzBuzz"
            elif i%3 == 0:
                answer[i-1] = "Fizz"
            elif i % 5 == 0:
                answer[i-1] = "Buzz"
            else:
                answer[i-1] = str(i)
        print(answer)
       
        return answer
=======
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [0]*n
        for i in range(1, n+1):
            if i%15 == 0:
                answer[i-1]= "FizzBuzz"
            elif i%3 == 0:
                answer[i-1] = "Fizz"
            elif i % 5 == 0:
                answer[i-1] = "Buzz"
            else:
                answer[i-1] = str(i)
        print(answer)
       
        return answer
>>>>>>> bb4dee632f7ba40081fd47f4bd4f1033e6577977
