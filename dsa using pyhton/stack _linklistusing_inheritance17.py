from singlylinklist1 import *
class stack(Sll):
    def __init__(self) -> None:
        super().__init__()
        self.item_count =0
    def is_empty(self):
        return super().is_empty()
    
    def push(self,data):
        self.insert_at_start(data)
        self.item_count +=1
    
    
    def pop(self):
        if not self.is_empty():
            self.delete_fist()
            self.item_count-=1
        else:
            raise IndexError('stcak under flow')   
    def peek(self):
        if not self.is_empty():
            return self.start.item
        
        else:
            raise IndexError('stack under flow')
        
    def size(self):
        return self.item_count
        
s1 =stack()
s1.push(10) 
s1.push(20)  
s1.push(30)    
print("top elment on the stack ",s1.peek())
s1.pop()
print("top elment on the stack ",s1.peek())