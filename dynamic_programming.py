#A helper function to verify that the index we are searching for is positive.
def verify_index(arr ,idx_1 ,idx_2):
    #If any index is negative.
    if idx_1 < 0 or idx_2 < 0:
        return 0
    #If both indices are valid.
    else:
        #Returning the value at that particular index.
        return arr[idx_1][idx_2]

#Dynamic programming function
def lcs_dynamic_programming(seq_1 ,seq_2):
    #Take the size of both sequences.
    m ,n = len(seq_1) ,len(seq_2)
    #Create a table(matrix) like structure ,sequence 1 is the row and sequence 2 is the column
    result = [[0 for _ in range(n)] for _ in range(m)]

    #Iterating on every individual element od the table.
    for idx_1 in range(m):
        for idx_2 in range(n):
            #If the particular index of both sequences contain the same value
            if seq_1[idx_1] == seq_2[idx_2]:
                #We add 1 to the element that is diagonally behind it.
                result[idx_1][idx_2] = 1 + verify_index(result ,idx_1 - 1 ,idx_2 - 1)
            #If the particular index of both sequences does not contain the same value
            else:
                #choose the longest subsequence between the element above the current element or on the left of the element.
                result[idx_1][idx_2] = max(verify_index(result ,idx_1 - 1 ,idx_2),
                                           verify_index(result ,idx_1 ,idx_2 - 1))

    #return the last value of table.         
    return result[-1][-1]

#Test Run   
s1 = "serendipitous"
s2 = "precipitation"
LCS = lcs_dynamic_programming(s1 ,s2)
print(LCS)
