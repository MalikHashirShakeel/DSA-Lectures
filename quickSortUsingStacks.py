# from stack import Stack

# def partition(arr, start, end):
#     loc, left, right = start, start, end

#     is_left = True
#     while left < right:
#         if is_left:
#             if arr[right] < arr[loc]:
#                 arr[right], arr[loc] = arr[loc], arr[right]
#                 loc = right
#                 is_left = False
#             else:
#                 right -= 1
#         else:
#             if arr[left] > arr[loc]:
#                 arr[left], arr[loc] = arr[loc], arr[left]
#                 loc = left
#                 is_left = True
#             else:
#                 left += 1

#     return loc

# def quick_sort(arr, stk):
#     while not stk.is_empty():
#         item = stk.pop()
#         start, end = item[0], item[1]
#         if start < end:
#             pivot = partition(arr, start, end)

#             # Push the left part to stack
#             if pivot - 1 > start:
#                 stk.push([start, pivot - 1])

#             # Push the right part to stack
#             if pivot + 1 < end:
#                 stk.push([pivot + 1, end])

#     return arr
    
# l = [44 ,33 ,11 ,55 ,77 ,90 ,40 ,60 ,99 ,22 ,88 ,66]
# arr = []
# stk = Stack(100)
# # stk.push([0 ,6])
# srt = quick_sort(arr ,stk)
# print(arr)
        

