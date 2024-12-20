from pyarray import Array

class Queue:
    def __init__(self ,max_size):
        self._queue = Array(max_size)
        self._front = 0
        self._back = max_size - 1
        self._count = 0

#-------------------------------------------------------------------------------------------------------------------------

    def is_empty(self):
        return self._count == 0
    
#-------------------------------------------------------------------------------------------------------------------------

    def is_full(self):
        return self._count == len(self._queue)
    
#-------------------------------------------------------------------------------------------------------------------------

    def enqueue(self ,item):
        assert not self.is_full() ,"Cannot add into a full queue."
        maxSize = len(self._queue)
        self._back = (self._back + 1) % maxSize
        self._queue[self._back] = item # using addone inside the function
        self._count += 1

#-------------------------------------------------------------------------------------------------------------------------

    def dequeue(self):
        assert not self.is_empty() ,"Cannot remove from an empty queue."
        item = self._queue[self._front]
        maxSize = len(self._queue)
        self._front = (self._front + 1) % maxSize
        self._count -= 1
        return item
    
#-------------------------------------------------------------------------------------------------------------------------

    def traverse(self):
        self._queue.traverse()

#-------------------------------------------------------------------------------------------------------------------------

    def front(self):
        assert not self.is_empty() ,"Empty queue."
        return self._queue[self._front]
    
#-------------------------------------------------------------------------------------------------------------------------

    def print_queue(self):
        self._queue.traverse()

#=========================================================================================================================

q1 = Queue(5)
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
print(q1.dequeue())
print(q1.dequeue())
q1.enqueue(6)
q1.enqueue(7)
print("Front",q1.front())
q1.print_queue()

