""" stack liner data structure 
    it follows last in first out(LIFO) order
    insertion and removal of the element has done from  one end
    push is used for insertion an element in a stack 
    pop is used to remove an elemnt in a stack """
    
    
    

# funtion associated with stack
""" push(x) it is used to insert the element 'x' at the end of stack
    pop() it is used to remove the top/last element of stack 
    size() give the size /length od a stack 
    top() give the refrence of last element presented in stack
    empty()  return the for an empty stack"""
    
    
    
    
    
stack =[]   # time compelxity of list is  O(n)
stack.append('abc')
stack.append('welocome ')
stack.append('to')
stack.append('great learning')
print(stack)
print(stack.pop())


#####* stack in python are created by the collection module which provied deque class
####* append and pop operation are faster in deque as comapre to list
## time colplexity of deque is O(1)
from collections import deque
stack  = deque()
stack.append('abs')
stack.append('heelo')
stack.append('heelo')
stack.append('heelo')
stack.append('heelo')
print(stack.pop())
print(stack)




####implemenatation using queue#######
""" queue module contains the LIFO queue
    it is having some additinal functions and works same as stack
    put function is used to insert the data in queue
    get function is used to remove the element"""
    
    #funtions are get,maxsize ,empty,full,put,qsize
    
    
from queue import LifoQueue
stack = LifoQueue(maxsize=4)
stack.put(2)
stack.put(1)
stack.put(5)
stack.put(3)
stack.put(89)
print(stack.qsize())
print(stack.full())
stack.get()








