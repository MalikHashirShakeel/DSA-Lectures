from pyarray import Array
from time import time

# Initialize the array
a = Array(6)

# Set the values in the array
for index in range(a.size):
    a[index] = index + 1

# Searching for the index of a value in the custom-defined array class.
def linsearch(arr, value):
    for index in range(arr.size):
        if arr[index] == value:
            return index  # Return the index where the value is found
    return None  # Return None if the value is not found

time1 = time()
print(linsearch(a, 6))  # This should return 5
time2 = time()
print((time2 - time1) * 1000,"milliseconds")


