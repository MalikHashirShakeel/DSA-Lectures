#Find the longest common subsequence =>

def longest_common_subsequense(seq_1 ,seq_2 ,idx_1 = 0 ,idx_2 = 0):
    #This case states that one of the two strings is completely exhausted.
    if idx_1 == len(seq_1) or idx_2 == len(seq_2):
        #Don't add anything to the length of the subsequence.
        return 0
    #If both the subsequences have their first element same.
    elif seq_1[idx_1] == seq_2[idx_2]:
        #find the length of longest common subsequence of remaining subsequence and add the common element's occurence to that subsequence.
        return 1 + longest_common_subsequense(seq_1 ,seq_2 ,idx_1 + 1 ,idx_2 + 1)
    #If both subsequences have first element different.
    else:
        #try first by removing the first element of subsequence 1 and find its longest common subsequence with sequence 2 and vice versa ,and whichever sequence is longer , we will consider that one.
        return max(longest_common_subsequense(seq_1 ,seq_2 ,idx_1 + 1 ,idx_2), longest_common_subsequense(seq_1 ,seq_2 ,idx_1 ,idx_2 + 1))

#Test Run   
s1 = "serendipitous"
s2 = "precipitation"
LCS = longest_common_subsequense(s1 ,s2)
print(LCS)