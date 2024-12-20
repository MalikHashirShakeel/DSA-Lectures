from stack import Stack

# Partition function to place the pivot element in its correct position in the array
def partition(arr, low, high):
    pivot_index = low  # Initialize pivot index to the starting point
    left_pointer = low  # Left pointer starts just after the pivot
    right_pointer = high  # Right pointer starts at the end of the array

    move_left = True  # Boolean flag to alternate between left and right pointers

    # Loop until the left and right pointers meet
    while left_pointer < right_pointer:
        if move_left:  # Move right pointer first
            if arr[right_pointer] < arr[pivot_index]:  # Check if right element is smaller than the pivot
                # Swap right element with the pivot and update the pivot index
                arr[right_pointer], arr[pivot_index] = arr[pivot_index], arr[right_pointer]
                pivot_index = right_pointer  # Update the pivot index
                move_left = False  # Now, move the left pointer in the next iteration
            else:
                right_pointer -= 1  # Move the right pointer towards the left
        else:  # Move left pointer
            if arr[left_pointer] > arr[pivot_index]:  # Check if left element is greater than the pivot
                # Swap left element with the pivot and update the pivot index
                arr[left_pointer], arr[pivot_index] = arr[pivot_index], arr[left_pointer]
                pivot_index = left_pointer  # Update the pivot index
                move_left = True  # Now, move the right pointer in the next iteration
            else:
                left_pointer += 1  # Move the left pointer towards the right

    return pivot_index  # Return the final position of the pivot


# Non-recursive quicksort using a stack to avoid recursion
def quick_sort(arr, stack):
    # Loop while there are subarrays left to process
    while not stack.is_empty():
        # Pop the current subarray range from the stack
        subarray = stack.pop()
        low, high = subarray[0], subarray[1]  # Get the start (low) and end (high) indices

        if low < high:  # Only process if the subarray has more than one element
            # Partition the array and get the pivot index
            pivot = partition(arr, low, high)

            # Push the left subarray (elements before the pivot) to the stack if it has more than one element
            if pivot - 1 > low:
                stack.push([low, pivot - 1])

            # Push the right subarray (elements after the pivot) to the stack if it has more than one element
            if pivot + 1 < high:
                stack.push([pivot + 1, high])

    return arr  # Return the sorted array


l = [44 ,33 ,11 ,55 ,77 ,90 ,40 ,60 ,99 ,22 ,88 ,66]
arr = []
stk = Stack(100)
stk.push([0 ,len(l) - 1])
srt = quick_sort(arr ,stk)
print(arr)