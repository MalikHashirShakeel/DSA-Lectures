class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self, max_size):
        self._front = None
        self._rear = None
        self._max_size = max_size
        self._count = 0

    def __len__(self):
        return self._count
    
    def is_empty(self):
        return self._count == 0
    
    def is_full(self):
        return self._count == self._max_size
    
    def enqueue(self, item):
        assert not self.is_full(), "Queue Overflow."
        node = ListNode(item)
        if self.is_empty():
            self._front = node
            self._rear = node
        else:
            self._rear.next = node
            self._rear = node
        self._count += 1

    def dequeue(self):
        assert not self.is_empty(), "Queue Underflow."
        item = self._front.data
        self._front = self._front.next
        if self._front is None:  
            self._rear = None
        self._count -= 1
        return item

    def peek(self):
        assert not self.is_empty(), "Queue is empty."
        return self._front.data


q = Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(len(q))  
print(q.peek())  
print(q.dequeue())  
print(q.dequeue())  
print(q.dequeue())  
print(q.dequeue())  
print(q.dequeue())  
print(len(q))  
