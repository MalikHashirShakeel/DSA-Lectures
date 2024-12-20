def insertion_sort(arr):
    curr = 0

    for item in range(1 ,len(arr)):
        curr = arr[item]
        prev = item - 1

        while prev >= 0 and arr[prev] > curr:

            arr[prev + 1] = arr[prev]
            prev -= 1

        arr[prev + 1]  = curr

    return arr

#Test Run
arr = [1, 4, 3, 5, 6, 8, 7, 9, 0, 2, 8]
sorted_array = insertion_sort(arr)
print(sorted_array)