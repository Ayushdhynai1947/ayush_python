#implemtwtion dequeu by extending doubly link list class
from deque_using_doubly_22list import *

class deque(Deque):
    def __init__(self):
        super().__init__()
        
    def insert_front(self, data):
         super().insert_front(data)
    
    def insert_rear(self, data):
         super().insert_rear(data)
    
    def delete_front(self):
        return super().delete_front()
    
    def delete_rear(self):
        return super().delete_rear()
    
    def get_front (self):
        if self.is_empty():
            raise IndexError ("Deque is empty")
        
        return self.front.data
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError('deque is empty')
        return self.rear.data
    
    def __len__(self):
        return  self.size
    
d = Deque()
d.insert_front(40)
d.insert_rear(30)
d.insert_front(5)
print("Front:", d.get_front())  # Output: Front: 5
print("Rear:", d.get_rear())    # Output: Rear: 20
d.delete_front()
d.delete_rear()
print("Size:", len(d))
