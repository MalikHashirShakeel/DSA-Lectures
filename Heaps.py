class MaxHeap:
    """
    A MaxHeap implementation where the largest element is always at the root.

    Attributes:
        _heap (list[int]): The list representation of the heap.
        _size (int): The number of elements in the heap.
    """

    def __init__(self):
        """Initializes an empty MaxHeap."""
        self._heap: list[int] = []
        self._size: int = 0

#-----------------------------------------------------------------------------------------------

    def add(self, value: int) -> None:
        """
        Adds a value to the heap while maintaining the heap property.

        Args:
            value (int): The value to add to the heap.
        """
        self._heap.append(value)
        self._size += 1
        self._heapify_up()

#-----------------------------------------------------------------------------------------------

    def remove(self) -> int:
        """
        Removes and returns the maximum value from the heap.

        Returns:
            int: The maximum value in the heap.

        Raises:
            AssertionError: If the heap is empty.
        """
        assert self._size > 0, "Cannot remove from an empty heap."
        if self._size == 1:
            self._size -= 1
            return self._heap.pop()  # Handle single element case

        self._size -= 1
        item = self._heap[0]
        self._heap[0] = self._heap.pop()  # Swap with last element
        self._heapify_down()
        return item
    
#-----------------------------------------------------------------------------------------------

    def _has_parent(self, index: int) -> bool:
        """
        Checks if the given index has a parent node.

        Args:
            index (int): The index to check.

        Returns:
            bool: True if the index has a parent, False otherwise.
        """
        return self._parent_index(index) >= 0
    
#-----------------------------------------------------------------------------------------------

    def _parent_index(self, index: int) -> int:
        """
        Returns the parent index of the given index.

        Args:
            index (int): The child index.

        Returns:
            int: The parent index.
        """
        return (index - 1) // 2
    
#-----------------------------------------------------------------------------------------------

    def _swap(self, index1: int, index2: int) -> None:
        """
        Swaps the elements at two indices in the heap.

        Args:
            index1 (int): The first index.
            index2 (int): The second index.
        """
        self._heap[index1], self._heap[index2] = self._heap[index2], self._heap[index1]

#-----------------------------------------------------------------------------------------------

    def _parent(self, index: int) -> int:
        """
        Retrieves the value of the parent node for the given index.

        Args:
            index (int): The child index.

        Returns:
            int: The value of the parent node.
        """
        return self._heap[self._parent_index(index)]
    
#-----------------------------------------------------------------------------------------------

    def _heapify_up(self) -> None:
        """Restores the heap property by moving an element up as necessary."""
        index = self._size - 1
        while self._has_parent(index) and self._parent(index) < self._heap[index]:
            self._swap(index, self._parent_index(index))
            index = self._parent_index(index)

#-----------------------------------------------------------------------------------------------

    def _left_child_index(self, index: int) -> int:
        """
        Returns the index of the left child for a given index.

        Args:
            index (int): The parent index.

        Returns:
            int: The left child index.
        """
        return 2 * index + 1
    
#-----------------------------------------------------------------------------------------------

    def _right_child_index(self, index: int) -> int:
        """
        Returns the index of the right child for a given index.

        Args:
            index (int): The parent index.

        Returns:
            int: The right child index.
        """
        return 2 * index + 2
    
#-----------------------------------------------------------------------------------------------

    def _max_child_index(self, index: int) -> int:
        """
        Returns the index of the larger child for a given index.

        Args:
            index (int): The parent index.

        Returns:
            int: The index of the larger child, or -1 if no children exist.
        """
        left_child_index = self._left_child_index(index)
        right_child_index = self._right_child_index(index)

        if left_child_index >= self._size:  # No children
            return -1
        if right_child_index >= self._size:  # Only left child exists
            return left_child_index

        return left_child_index if self._heap[left_child_index] > self._heap[right_child_index] else right_child_index
    
#-----------------------------------------------------------------------------------------------

    def _heapify_down(self) -> None:
        """Restores the heap property by moving an element down as necessary."""
        index = 0
        while self._left_child_index(index) < self._size:  # While there are children
            max_child_index = self._max_child_index(index)
            if max_child_index == -1 or self._heap[index] >= self._heap[max_child_index]:
                break
            self._swap(index, max_child_index)
            index = max_child_index

#-----------------------------------------------------------------------------------------------

    def __len__(self) -> int:
        """
        Returns the number of elements in the heap.

        Returns:
            int: The size of the heap.
        """
        return self._size
    
#-----------------------------------------------------------------------------------------------

    def __str__(self) -> str:
        """
        Returns a string representation of the heap.

        Returns:
            str: The heap as a string.
        """
        return str(self._heap)
    
#-----------------------------------------------------------------------------------------------

    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the heap.

        Returns:
            str: The heap as a string.
        """
        return str(self._heap)

#-----------------------------------------------------------------------------------------------

    def __getitem__(self, index: int) -> int:
        """
        Retrieves the value at a specific index in the heap.

        Args:
            index (int): The index to retrieve.

        Returns:
            int: The value at the specified index.

        Raises:
            AssertionError: If the index is out of bounds.
        """
        assert 0 <= index < self._size, "Index out of bounds."
        return self._heap[index]
    
#-----------------------------------------------------------------------------------------------

    def __setitem__(self, index: int, value: int) -> None:
        """
        Sets a value at a specific index and restores the heap property.

        Args:
            index (int): The index to set the value.
            value (int): The new value to set.

        Raises:
            AssertionError: If the index is out of bounds.
        """
        assert 0 <= index < self._size, "Index out of bounds."
        self._heap[index] = value
        self._heapify_up()
        self._heapify_down()

#-----------------------------------------------------------------------------------------------
