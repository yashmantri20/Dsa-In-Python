# Triplet Sum in Array
class Solution:
    def find3Numbers(self,A, n, X):
   
        for i in range(n-1):
            s = set()
            curr_sum = X - A[i]
            for j in range(i + 1, n):
                if (curr_sum - A[j]) in s:
                    return 1
                s.add(A[j])
     
        return 0
 