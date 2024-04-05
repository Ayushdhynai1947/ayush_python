class  PrirorityQueue():
    def __init__(self) -> None:
        self.list =[]
        
    def push(self,data,priority):
        index =0
        while  index<len(self.list) and  self.list[index][1]<=priority:
            index +=1
        self.list.insert(index,(data,priority))    
    
    def is_empty(self):
        return   len(self.list)==0
    def pop(self):
        if self.is_empty():
            raise IndexError('PriorityQueue is Empty')
        
        return self.list.pop(0)[0]
    
    def size(self):
        return len(self.list)


p  =PrirorityQueue()
p.push("ayush",4)
p.push("rahul",1)
p.push("hulk",2)
p.push("viney",3)
p.push("gaurav",5)

while  not p.is_empty():
    print(p.pop())
                
    
    
    
