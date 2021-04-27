# find all pairs on integer array whose sum is equal to given number

class Solution:
    def getPairsCount(self, arr, n, k):
        count = 0
        d = {}
        
        for i in range(n):
            x = k - arr[i]
        
            if x in d:
                count += d[x]
    
            d[arr[i]] = d.get(arr[i],0) + 1
        
        return count
     