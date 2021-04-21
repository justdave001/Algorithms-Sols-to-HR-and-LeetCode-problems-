'''
c = list(map(int, input().split()))

def jumping(c):
    count = 0
    i = 0
    while i + 1 < len(c):
        if i+2 < len(c) and c[i+2] == 0:
            i += 2
            count += 1
        else:
            i += 1
            count += 1
    return count
print(jumping(c))
'''
c = list(map(int, input().split()))
print(c[1])
