# queue implementaion using list  using list 

class Queue:
    def __init__(self) -> None:
        self.item = []
        # self.front=None
        # self.rear =None
    def is_empty(self):
       return len(self.item) ==0  
    
    def enqueue(self,data):
        self.item.append(data)
    
    def dequeu(Self):
        if not Self.is_empty():
            Self.item.pop(0)
        else:
            raise IndexError('queue underflow')
        
    def get_front(self):
        if not self.is_empty():
            return self.item[0]
        
        else:
            raise IndexError("Queue is underflow ")
    
    def get_rear(self):
        if not self.is_empty():
            return self.item[-1]
        
        else:
            raise IndexError("queue underflow ")
    
    def size(self):
        return len(self.item)
    
    
q1 = Queue()

try:
 print("value is",q1.get_front())
except IndexError as e:
    print(e.args[0])
    
    
q1 .enqueue(10)
q1 .enqueue(20)
q1 .enqueue(30)
q1 .enqueue(40)
print("front =",q1.get_front(),"rear =",q1.get_rear())


try:
    q1.dequeu()
    print("queue has now",q1.size(),"elements ")
except IndexError as e:
    print(e.args[0])