#Deque using list

class deque:
    def __init__(self) -> None:
        self.item = []
    
    def is_empty(self):
        return len(self.item)==0
    
    def insert_front(self,data):
        self.item.insert(0,data)
    
    def insert_rear(self,data):
        self.item.append(data)
    
    def delete_front(self):
        if self.is_empty():
            raise IndexError('deque is empty')
        else:
           return  self.item.pop(0)
    
    def delete_rear(self):
        if self.is_empty():
            raise IndexError('deque is empty')
        else:
            return self.item.pop()
    
    def get_front(self):
        if self.is_empty():
            raise IndexError('deque is empty')
        else:
            return self.item[0]
        
    def get_rear(self):
        if self.is_empty():
            raise IndexError('deque is empty')
        else:
            return self.item[-1]
        
    def size(self):
        return len(self.item)
    
d1 =deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_rear(30)
d1.insert_rear(40)
print(d1.get_front(),d1.get_rear())


d1.delete_front()
d1.delete_rear()
print(d1.get_front(), d1.get_rear())
        