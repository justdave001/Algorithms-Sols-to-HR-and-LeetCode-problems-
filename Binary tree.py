class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    def space(self):
        incr = 0
        p = self.parent
        while p:
            incr += 1
            p = p.parent
        return incr
    def printt(self):
        spacs = " " * self.space()*4
        print(spacs + self.data)
        if self.children:
             for child in self.children:
                 child.printt()
            
    def add_child(self, vall):
        vall.parent = self
        
        self.children.append(vall)

   
def building():
    
    root = Node("Electronics")
    Laptop = Node("Laptop")
    Laptop.add_child(Node("Apple"))
    
    Television = Node("Tv")
    Television.add_child(Node("Samsung"))
    
    Phone = Node("Mobile")
    Phone.add_child(Node("Iphone"))
    
    
    root.add_child(Laptop)
    root.add_child(Television)
    root.add_child(Phone)
    
    return root
if __name__ == "__main__":
    root = building()
    root.printt()
