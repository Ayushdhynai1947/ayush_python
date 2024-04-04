from typing import SupportsIndex

#To implement a deque using an extended list class
class deque(list):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    
    def is_empty(self):
        return len(self)==0
    def insert_front(self,data):
        self.insert(0,data)
        
    def insert_rear(self,data):
        self.append(data)
        

    def delete_front(self):
        if self.is_empty():
            raise IndexError('deque is empty ')
        else:
           return  self.pop(0)
    
    def delete_rear(self):
        if self.is_empty():
            raise IndexError('deque is empty ')
        else :
            return self.pop()
    
    def get_front(self):
        if self.is_empty():
            raise IndexError('deque is empty ')
        else:
            return self[0]
        
    def get_rear(self):
        if self.is_empty():
            raise IndexError('deque is empty ')
        else:
            return self[-1]
    
    def size(self):
        return len(self)
        
d = deque()
d.insert_front(10)
d.insert_rear(20)
d.insert_front(5)
print("Front:", d.get_front())  # Output: Front: 5
print("Rear:", d.get_rear())    # Output: Rear: 20
d.delete_front()
d.delete_rear()
print("Size:", d.size())        