#Write your code here
class Calculator:
    def power(self, n,p):
            self.n =n
            self.p = p
            if n>0 and p>0:
                return(n**p)
            else:
                raise Exception("n and p should be non-negative")

T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=Calculator().power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
