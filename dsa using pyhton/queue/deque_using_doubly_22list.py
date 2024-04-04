## using doubly link list

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def insert_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.size += 1

    def insert_rear(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node
        self.size += 1

    def delete_front(self):
        if self.is_empty():
            raise IndexError('Deque is empty')
        data = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.size -= 1
        return data

    def delete_rear(self):
        if self.is_empty():
            raise IndexError('Deque is empty')
        data = self.rear.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.size -= 1
        return data

    def get_front(self):
        if self.is_empty():
            raise IndexError('Deque is empty')
        return self.front.data

    def get_rear(self):
        if self.is_empty():
            raise IndexError('Deque is empty')
        return self.rear.data


# Example usage:
d = Deque()
d.insert_front(10)
d.insert_rear(20)
d.insert_front(5)
print("Front:", d.get_front())  # Output: Front: 5
print("Rear:", d.get_rear())    # Output: Rear: 20
d.delete_front()
d.delete_rear()
print("Size:", d.size())         # Output: Size: 1

            