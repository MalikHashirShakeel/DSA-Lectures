def bubble_sort(arr):
    #n-1 iterations will be done because it is already checking the next one.So the last will already be checked.
    for i in range(len(arr) - 1):
        #Assume the arr is already sorted.
        sorted = True
        #Every time ,we will check one element less than we checked in the previous analysis.
        for j in range(len(arr) - i - 1):
            #If element is greater than the next element
            if arr[j] > arr[j + 1]:
                #swapping
                arr[j] ,arr[j + 1] = arr[j + 1] ,arr[j]
                #we find out that the arr is not sorted
                sorted = False
        #If the arr is already sorted than there is no need to check more.
        if sorted == True:
            return arr
    #after all observations ,finally return the sorted array.
    return arr
        
l = [1,2,4,3,7,6,8,4,6,5]
print(bubble_sort(l))