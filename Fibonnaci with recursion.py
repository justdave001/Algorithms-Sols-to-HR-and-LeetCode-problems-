inputt= int(input())

def fibo(number):
    if number == 0:
        return 0
    elif number ==1:
        return 1
    else:
        return (fibo(number)+fibo(number-1))
for i in range(inputt):
    print(fibo(i))
