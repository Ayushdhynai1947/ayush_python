

class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
        
    def pop(self):
        if not self.is_empty():
          return super().pop
        else:
            raise IndexError('stack is empty')
        
    def peak(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("stack is empty")
        
    def size(self):
        return len(self)
    
    def insert(self,indx ,data):
        raise AttributeError("no attribute 'inert' in stack")
    
s1 = Stack()
s1.push(20)
s1.push(50)
s1.push(30)
print("top value=",s1.peak())