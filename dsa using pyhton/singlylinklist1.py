# # creating node in a single link list

# class Node:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.refence = None
        
        
# Node1 = Node(7)
# print(Node1.data)
# print(Node1.refence)


# #################################
# ### traversal in link list
# class node:
#     def __init__(self,data) -> None:
#         self.data = data
#         self.next  = None
        
# class Sll:
#     def __init__(self) -> None:
#         self.head = None
        
        
#     def traversal(self):
#         if self.head is None:
#             print('singly link list is empty ')
#         else:
#             a  = self.head
#             while  a is not None:
#                 print(a.data,end= " ") 
#                 a = a.next
# sll = Sll()  
# # sll.head = n1          
# n1 = node(5)
# n2 = node(10)
# n1.next = n2
# n3 = node(52)
# n4 = node(56)




#################single link list###########################
class Node:
    def __init__(self,item =None,next=None) -> None:
        self.item = item 
        self.next = next
        
class Sll:
    def __init__(self,start = None) -> None:
         self.start = start
         
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self,data):
        n = Node(data,self.start)
        self.start = n
    def insert_at_last(self,data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp =temp.next
            temp.next = n
        else:
            self.start =n
            
            
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None   
    def inser_after(self ,temp,data):
        if temp is not None:
            n = Node(data,temp.next)
            temp.next = n
            
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
    
    def delete_fist(self):
        if self.start is not None:
            self.start = self.start.next
            
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start= None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next= None   
                
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item ==data:
                self.start = None
              
        else:
            temp = self.start
            if temp.item ==data:
                self.start =temp.next
            else:
             while temp.next is not None:
                if temp.next.item ==data:
                    temp.next= temp.next.next
                    break
                temp = temp.next
    def  __iter__(self):
        return SLLITerator(self.start)   
    
    
    
class SLLITerator:
    def __init__(self,start) -> None:
        self.current =start
        
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current=self.current.next
        return data
 
 
## driver code
""" 
mylist = Sll()
mylist.insert_at_start(20)   
mylist.insert_at_start(10) 
mylist.insert_at_last(30)
mylist.inser_after (mylist.search(20),25)
mylist.print_list()
mylist.delete_item(20)
print()
mylist.print_list()
print()


"""
        