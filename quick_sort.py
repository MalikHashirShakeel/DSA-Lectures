#Quick Sort =>

def partition(arr, start=0, end=None):
    #If we have not set the ending pointer, it will automatically set it.
    if end is None:
        end = len(arr) - 1

    #initialize left pointer at first element , rifht at second last and pivot at last.
    left_pointer, right_pointer, pivot = start, end - 1, arr[end]

    #Continue until the right and left pointers reaches at the same position.
    while left_pointer <= right_pointer:
        #if the element at the left pointer is less than pivot.
        if arr[left_pointer] < pivot:
            #advance the left pointer
            left_pointer += 1
        #if the element at the right pointer is greater than pivot.
        elif arr[right_pointer] > pivot:
            #decrement the right pointer
            right_pointer -= 1
        else:
            #if both conditions not met ,swap the elements at the left and right pointers
            arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
            #Advance and decrement left and right pointers respectively.
            left_pointer += 1
            right_pointer -= 1

    #If the element at the left pointer is greater than the pivot ,swap it with pivot.
    if arr[left_pointer] > pivot:
        #swapping.
        arr[left_pointer], arr[end] = arr[end], arr[left_pointer]
        #return the index of pivot
        return left_pointer
    else:
        #return the index of pivot
        return end


def quick_sort(arr, start=0, end=None):
    #If we have not set the ending pointer, it will automatically set it.
    if end is None:
        end = len(arr) - 1

    #This is the condition that the arr must contain more than one elements
    #start == end (One element)
    #start > end(No elements at all.)
    if start < end:
        #It will set the list with pivot in the middle, smaller than pivots in the left and remaining at right.
        pivot = partition(arr, start, end)
        #recursively call until the left sublist contain only one element or no elements
        quick_sort(arr, start, pivot - 1)
        #recursively call until the right sublist contain only one element or no elements
        quick_sort(arr, pivot + 1, end)

    #Return final sorted array.
    return arr

#Test Run
arr = [1, 4, 3, 5, 6, 8, 7, 9, 0, 2, 8]
sorted_array = quick_sort(arr)
print(sorted_array)
