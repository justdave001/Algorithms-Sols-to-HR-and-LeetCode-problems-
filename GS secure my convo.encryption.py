
n= int(input("Enter 1 to encrypt and 2 to decrypt:"))
message = input("Enter message:")
private = int(input("Enter Private Key: "))
arr2 = list(map(int, str(private)))

arr3=[]
if n == 1:
    for i in range(len(arr2)):
        arr3.append(message[i]*arr2[i])
    print(arr3)
    stringed = "".join(arr3)
    unspaced = stringed.replace(" ","")
    for i in message:
      if i not in stringed:
        arr3.append(i)
    print("".join(arr3))
newar = []

if n == 2:
    l = list(message)
    for i in l:
        if i not in newar:
            newar.append(i)
    print("".join(newar))
   
