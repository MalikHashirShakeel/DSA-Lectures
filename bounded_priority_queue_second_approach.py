class BoundedPriorityQueue:
    def __init__(self ,max_priority):
        self._queue = list()
        self._max_priority = max_priority

#-------------------------------------------------------------------------------------------------------------------------

    def __len__(self):
        return len(self._queue)
    
#-------------------------------------------------------------------------------------------------------------------------

    def is_empty(self):
        return len(self) == 0
    
#-------------------------------------------------------------------------------------------------------------------------

    def enqueue(self ,tpl_item):
        assert 0 <= tpl_item[1] <= self._max_priority ,"Priority out of range."
        if self.is_empty():
            self._queue.append(tpl_item)

        else:
            inserted = False
            for idx in range(len(self)):
                if self._queue[idx][1] > tpl_item[1]:
                    self._queue.insert(idx ,tpl_item)
                    inserted = True
                    break
            
            if not inserted:
                self._queue.append(tpl_item)

#-------------------------------------------------------------------------------------------------------------------------

    def dequeue(self):
        assert not self.is_empty() ,"Cannot remove from empty queue."
        return self._queue.pop(0)
    
#-------------------------------------------------------------------------------------------------------------------------

    def __str__(self):
        if self.is_empty():
            return "BoundedPriorityQueue is empty."
        return "BoundedPriorityQueue:\n" + "\n".join(f"Item: {item[0]}, Priority: {item[1]}" for item in self._queue)

#=========================================================================================================================

# q1 = BoundedPriorityQueue(10)
# q1.enqueue(("apple" ,5))
# q1.enqueue(("mango" ,4))
# q1.enqueue(("banana" ,1))
# q1.enqueue(("peach" ,2))
# q1.enqueue(("pear" ,0))
# q1.enqueue(("ananas" ,3))
# q1.enqueue(("strawberry" ,7))
# print(q1)


