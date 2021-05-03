 
 # Longest consecutive subsequence 
 # a = [2,6,1,9,4,5,3]
 # The consecutive numbers here are 1, 2, 3, 4, 5, 6. These 6 numbers form the longest consecutive subsquence.
class Solution:
    
    # arr[] : the input array
    # N : size of the array arr[]
    
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,arr, N):
        arr = list(set(arr))
        arr.sort()
        count = 1
        prev_count = 1
        for i in range(len(arr) - 1):
            if arr[i] + 1 == arr[i+1]:
                count += 1
            else:
                prev_count = max(count,prev_count)
                count = 0
        return max(prev_count,count)