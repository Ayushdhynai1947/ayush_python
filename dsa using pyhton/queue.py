""" It is liner data structure 
    it follows last in first out
    insertion can take place from the rear end
    deletion can take place from the front end 
    4 major operation in 
    * enqueue(ele)  used to insert element at top
    * dequeue () remove the top element from queue
    * peekfirst () to get the first element  of queue
    * peeklast ()  to get the last element of queue
    * all operation works in constant time O(1)
    """
    
    
class queue:
    def __init__(self) -> None:
         self.queue =[]
    
    def enqueue(self, items):
        self.queue.append(items)
    
    def dequeue(self):
        if len(self.queue) <1:
            return None
        return self.queue.pop(0)
    
    def display(self):
        print(self.queue)
    
    def size(self):
        return len(self.queue)
    
q= queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.display()
q.dequeue()
print('after removing an elemnts')
q.display()













################using  circular Queue################################
class CircularQueue():
    def __init__(self,capacity) -> None:
        self.capacity = capacity
        self.queue = [None] *capacity
        self.front = self.rear =-1
        
    def is_empty(self):
        return self.front ==-1
    
    def is_full(self):
        return(self.rear +1) % self.capacity ==self.front
    
    def enqueue(self,item):
        if self.is_full():
            print('queue is full')
        
        elif self.is_empty():
            self.front = self.rear =0
        else :
            self.rear = (self.rear +1) % self.capacity
        
        
        self.queue[self.rear] = item
    
    def dequeue(self):
        if self.is_empty():
            print('Queue is empty ')
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear =-1
        else:
            self.front =(self.front +1) % self.capacity
        
        return item
    
    def display(self):
        if self.is_empty():
            print('queue is empty ')
            return 
        elif self.rear >= self.front:
            print("queue:", self.queue[self.front:self.rear +1])
        else:
            print("Queue:", self.queue[self.front:] + self.queue[:self.rear + 1])



cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)

cq.display()  # Output: Queue: [1, 2, 3, 4, 5]

cq.dequeue()
cq.dequeue()
cq.display()  # Output: Queue: [3, 4, 5]

cq.enqueue(6)
cq.enqueue(7)
cq.display()  # Output: Queue: [3, 4, 5, 6, 7]