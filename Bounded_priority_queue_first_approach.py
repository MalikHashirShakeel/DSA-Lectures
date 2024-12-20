class BoundedPriorityQueue:
    def __init__(self ,max_priority):
        self._queue = list()
        self._max_priority = max_priority

#-------------------------------------------------------------------------------------------------------------------------

    def is_empty(self):
        return len(self._queue) == 0
    
#-------------------------------------------------------------------------------------------------------------------------

    def __len__(self):
        return len(self._queue)
    
#-------------------------------------------------------------------------------------------------------------------------

    def enqueue(self ,tpl_value):
        assert 0 < tpl_value[1] <= self._max_priority ,"Priority out of range."
        self._queue.append(tpl_value)

#-------------------------------------------------------------------------------------------------------------------------

    def dequeue(self):
        assert not self.is_empty() ,"Cannot dequeue from an empty queue."
        idx = 0
        heighest_priority = self._queue[0][1]

        for item in range(1 ,len(self)):
            if self._queue[item][1] < heighest_priority:
                idx = item
                heighest_priority = self._queue[item][1]
        item = self._queue.pop(idx)
        return item
    
#-------------------------------------------------------------------------------------------------------------------------

    def __str__(self):
        return ".".join([f"({item[0] ,item[1]})" for item in self._queue])
    
#-------------------------------------------------------------------------------------------------------------------------