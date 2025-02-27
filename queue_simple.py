class Queue:
    def __init__(self):
        self._queue = list()

#------------------------------------------------------------------------------------------------------------------------

    def __len__(self):
        return len(self._queue)
    
#------------------------------------------------------------------------------------------------------------------------

    def is_empty(self):
        return len(self) == 0
    
#------------------------------------------------------------------------------------------------------------------------

    def enqueue(self ,item):
        self._queue.append(item)

#------------------------------------------------------------------------------------------------------------------------

    def dequeue(self):
        assert not self.is_empty() ,"Cannot pop from empty Queue."
        return self._queue.pop(0)
