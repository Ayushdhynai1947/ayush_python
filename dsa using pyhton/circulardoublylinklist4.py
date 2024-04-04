"""circular link list """
class node:
    def __init__(self,item = None,prev = None,next = None) -> None:
        self.item = item
        self.prev = prev
        self.next = next

class CDLL:
    def __init__(self,start = None) -> None:
        self.start = start
        
    def is_empty(self):
        return self.start ==None
    
    def insert_at_start(self,data):
        n = node(data)
        if self.is_empty():
            n.next= n
            n.prev=n
        else:
            n.next =self.start
            n.prev = self.start.prev
            self.start.prev.next=n
            self.start.prev =n
        self.start=n    
    def insert_at_last(self,data):
        n = node(data)
        if self.is_empty():
            n.next= n
            n.prev=n
            self.start =n
        else:
            n.next   = self.start
            n.prev = self.start.prev
            n.prev.next = n
            self.start.prev = n
            
    def search(self,data):
        temp = self.start
        if temp==None:
            return None
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    
    
            