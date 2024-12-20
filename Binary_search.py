# from pyarray import Array
# from time import time

# Initialize the array
# a = Array(6)

# Set the values in the array
# for index in range(a.size):
#     a[index] = index + 1

#Implementing binary search to find out the index of element in the array.

#Iterative approach
# def bin_search(arr ,value):
#     low = 0
#     high = arr.size - 1

#     while low <= high:
#         mid = (high + low) // 2

#         if arr[mid] == value:
#             return mid
#         elif value < arr[mid]:
#             high = mid - 1
#         else:
#             low = mid + 1

#     return None

# time1 = time()
# print(bin_search(a, 6))
# time2 = time()
# print((time2 - time1) * 1000,"milliseconds")

#----------------------------------------------------------------------------------------------------------------------

#Recursive approach
# def bin_search_rec(arr ,target ,lo ,hi):
#     mid = (lo + hi) // 2

#     if arr[mid] == target:
#         return mid
#     elif target < arr[mid]:
#         return bin_search_rec(arr ,target ,0 ,mid - 1)
#     else:
#         return bin_search_rec(arr ,target ,mid + 1,len(arr))
    
# time1 = time()
# print(bin_search_rec(a, 6 ,0 ,len(a)))
# time2 = time()
# print((time2 - time1) * 1000,"milliseconds")

#-----------------------------------------------------------------------------------------------------------------------

# #First Occurrence of the repeated Numbers
# #Helper function to detect the position
# def veirfy_position(arr ,target ,mid ):
#     middle_element = arr[mid]

#     if middle_element == target:
#         if mid > 0 and arr[mid - 1] == middle_element:
#             return "left"
#         return "found"
#     elif target < middle_element:
#         return "left"
#     else:
#         return "right"

#Binary search algorithm   
# def find_element(arr ,target ,method):
#     lo ,hi = 0 ,len(arr) - 1

#     while lo <= hi:
#         mid = (lo + hi) // 2
#         result = method(arr ,target ,mid)

#         if result == "found":
#             return mid
#         elif result == "left":
#             hi = mid - 1
#         else:
#             lo = mid + 1

#     return -1

# l = [1,2,3,3,3,3,3,3,3,3,4,5,6,6,6,6]
# print(find_element(l ,6 ,veirfy_position))

#------------------------------------------------------------------------------------------------------------------------

# #For first and last occurrence
# def find_first_occurrence(arr ,target):
#     def verify_first_occurrence(arr ,target ,mid):
#         middle_element = arr[mid]

#         if middle_element == target:
#             if mid > 0 and arr[mid - 1] == middle_element:
#                 return "left"
#             return "found"
#         elif target < middle_element:
#             return "left"
#         else:
#             return "right"
        
#     return find_element(arr ,target ,verify_first_occurrence)

# def find_last_occurrence(arr ,target):
#     def verify_last_occurrence(arr ,target ,mid):
#         middle_element = arr[mid]

#         if middle_element == target:
#             if mid < len(arr) - 1 and arr[mid + 1] == middle_element:
#                     return "right"
#             return "found"
#         elif target < middle_element:
#             return "left"
#         else:
#             return "right"
        
#     return find_element(arr ,target ,verify_last_occurrence)

# def find_first_and_last_occurrence(arr ,target):
#     return find_first_occurrence(arr ,target) ,find_last_occurrence(arr ,target)

# l = [1,2,3,3,3,3,3,3,3,3,4,5,6,6,6,6]
# print(find_first_and_last_occurrence(l ,6))

#------------------------------------------------------------------------------------------------------------------------


#Binary Search algorithm for a rotated list to count the number of rotations
def verify_search(arr ,mid):
        if mid > 0 and arr[mid - 1] > arr[mid]:
            return "found"
        elif arr[0] <= arr[mid]:
            return "right"
        else:
            return "left"
    

def count_rotations(arr):
    lo ,hi = 0 ,len(arr) - 1

    while lo <= hi:
        mid = (hi + lo) // 2

        result = verify_search(arr ,mid)

        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        else:
            lo = mid + 1
    return 0
        

l = [5 ,6 ,7 ,1 ,2 ,3 ,4]
print(count_rotations(l))
    
    
