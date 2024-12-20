from tree_functions import *

class Heap:
    def __init__(self ,arr):
        self._heap = self.build_heap(arr)
        self._heap_root = build_tree(self._heap)

#------------------------------------------------------------------------------------------------------------------------

    def build_heap(self ,arr):
        idx = 1

        while idx < len(arr):
            parent = (idx - 1) // 2

            if idx != 0 and arr[idx] > arr[parent]:
                arr[idx] ,arr[parent] = arr[parent] ,arr[idx]
                idx = parent - 1

            idx += 1
        return arr

#-------------------------------------------------------------------------------------------------------------------------

hp = Heap([34 ,56 ,29 ,45 ,37 ,68])
