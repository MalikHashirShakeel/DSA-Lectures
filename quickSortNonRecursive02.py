from stack import Stack

# Helper function to rearrange the pivot using the median-of-three method
def shift_pivot(arr, low, high):
    if high - low > 1:  # Ensure there are at least 3 elements
        mid = (low + high) // 2
        # Find the median of arr[low], arr[mid], arr[high]
        temp_list = [arr[low], arr[mid], arr[high]]
        temp_list.sort()
        
        # Move the median to the low position (to act as the pivot)
        median = temp_list[1]
        if median == arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
        elif median == arr[mid]:
            arr[low], arr[mid] = arr[mid], arr[low]

# Partition the array and return the final position of the pivot
def partition(arr, low, high):
    shift_pivot(arr, low, high)  # Ensure pivot is set using median-of-three

    pivot_index = low  # Pivot starts at 'low' index
    left_ptr = low
    right_ptr = high
    move_left = True  # Control to alternate between moving left and right pointers

    while left_ptr < right_ptr:
        if move_left:
            # Move right pointer left until an element smaller than pivot is found
            if arr[right_ptr] < arr[pivot_index]:
                # Swap with pivot and update pivot position
                arr[right_ptr], arr[pivot_index] = arr[pivot_index], arr[right_ptr]
                pivot_index = right_ptr
                move_left = False  # Switch to move the left pointer next
            else:
                right_ptr -= 1
        else:
            # Move left pointer right until an element larger than pivot is found
            if arr[left_ptr] > arr[pivot_index]:
                # Swap with pivot and update pivot position
                arr[left_ptr], arr[pivot_index] = arr[pivot_index], arr[left_ptr]
                pivot_index = left_ptr
                move_left = True  # Switch to move the right pointer next
            else:
                left_ptr += 1

    return pivot_index  # Return the final pivot position

# Non-recursive quicksort function using a stack
def quick_sort(arr, stk):
    while not stk.is_empty():
        low, high = stk.pop()  # Get the sublist indices to sort

        if low < high:
            # Partition the array and get the pivot's final position
            pivot = partition(arr, low, high)

            # Push the left sublist onto the stack if it has more than one element
            if low < pivot - 1:
                stk.push([low, pivot - 1])

            # Push the right sublist onto the stack if it has more than one element
            if pivot + 1 < high:
                stk.push([pivot + 1, high])

    return arr


l = [88, 22, 77, 22, 66, 55, 44, 22, 33]
s = Stack(100)
s.push([0 ,len(l) - 1])
sorted_l = quick_sort(l ,s)
print(sorted_l)