class Human:
    def __init__(self, kind = ""):
        self.kind = kind
    def whatKind(self):
        return self.kind
    
def main():
   GoodHuman = Human("ok")
   print(GoodHuman.whatKind())
   BadHuman = Human("Bad")
   print(BadHuman.whatKind())
if __name__ == "__main__":
   main()

b=1
while b < 100:
    print(b)
    b = b + 1

a=1
b=1
while b < 56:
  print(b)
  a,b = b,a+b
