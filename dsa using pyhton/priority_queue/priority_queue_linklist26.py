class node :
    def __init__(self,item =None,priority =None,next =None) -> None:
        self.item = item
        self.priority =priority
        self.next =next

class PriorityQueue:
    def __init__(self) -> None:
        self.start = None
        self.item_count =0
        
    def push(self,data,priority):
        n = node(data,priority)
        if not self.start or priority <self.start.priority:
            n.next = self.start
            self.start =n
        else:
            temp = self.start
            while temp.next and temp.next.priority<=priority:
        
    