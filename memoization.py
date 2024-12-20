#Function for memoization.
def memoized(seq_1 ,seq_2):
    #Initialize the dictionary that will track the indices that are already computed.
    memo = {}
    #Actual function of recursion
    def recurse(idx_1 ,idx_2):
        #create a key that will store the index of computation.
        key = (idx_1 ,idx_2)
        #If key already exists in memo(dictionary).
        if key in memo:
            #return the number of occurence of the subsequense.
            return memo[key]
        #If one of the subsequence is exhausted.
        elif idx_1 == len(seq_1) or idx_2 == len(seq_2):
            #set that particular indice occurence to zero.
            memo[key] = 0
        #If both sequence have their first occurence same.
        elif seq_1[idx_1] == seq_2[idx_2]:
            #Add one to the subsequence and increment the indices.
            memo[key] = 1 + recurse(idx_1 + 1 ,idx_2 + 1)
        #If the indices of both the sequences are not same.
        else:
             #try first by removing the first element of subsequence 1 and find its longest common subsequence with sequence 2 and vice versa ,and whichever sequence is longer , we will consider that one.
            memo[key] = max(recurse(idx_1 + 1 ,idx_2) ,recurse(idx_1 ,idx_2 + 1))
        
        #return the number of occurence of the subsequense.
        return memo[key]
    #Run the function with both indices initially at (0 ,0)
    return recurse(0 ,0)

#Test Run   
s1 = "serendipitous"
s2 = "precipitation"
LCS = memoized(s1 ,s2)
print(LCS)