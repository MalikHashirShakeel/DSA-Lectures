def merge(sub_arr_1 ,sub_arr_2):
    #Initialize the merged array ,the right and left pointers
    merged_arr ,sub_arr_1_pointer ,sub_arr_2_pointer = [] ,0 ,0

    #Continue expanding the merged array until one subarray is completely exhausted.
    while sub_arr_1_pointer < len(sub_arr_1) and sub_arr_2_pointer < len(sub_arr_2):
        #If the left array pointer value is less than right array pointer value.
        if sub_arr_1[sub_arr_1_pointer] <= sub_arr_2[sub_arr_2_pointer]:
            #Append the left array pointer value in the merged array.
            merged_arr.append(sub_arr_1[sub_arr_1_pointer])
            #Advance the pointer.
            sub_arr_1_pointer += 1
        #If the right array pointer value is less than left array pointer value.
        else:
            #Append the right array pointer value in the merged array.
            merged_arr.append(sub_arr_2[sub_arr_2_pointer])
            #Advance the pointer.
            sub_arr_2_pointer += 1

    #If any array has a remaining portion ,note it down
    sub_arr_1_remaining = sub_arr_1[sub_arr_1_pointer:]
    sub_arr_2_remaining = sub_arr_2[sub_arr_2_pointer:]

    #Return the final merged array with the the remaining elements in any of the subarray.
    return merged_arr + sub_arr_1_remaining + sub_arr_2_remaining


def merge_sort(arr):
    #If the array contains only single or it is empty then simply return the array
    if len(arr) <= 1:
        return arr
    
    #Take a midpoint of the array
    mid = len(arr) // 2

    #Divide the array into two parts ,left and right
    left_sub_array = arr[:mid]
    right_sub_array = arr[mid:]

    #Call the recursive function on both path until array contains only single element
    left_sorted_array ,right_sorted_array = merge_sort(left_sub_array) ,merge_sort(right_sub_array)

    #Merge the two sorted subarrays
    final_merged_array = merge(left_sorted_array ,right_sorted_array)

    #Return the final merged array.
    return final_merged_array


#Testing
array = [1 ,4 ,3 ,5 ,6 ,8 ,7 ,9 ,0 ,2 ,8]
merged_array = merge_sort(array)
print(merged_array)

