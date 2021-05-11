# Chocolate Distribution Problem

class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        i = 0
        min_val = A[N-1] - A[0]
        while i < N - M + 1:
            a = A[i + M - 1] - A[i]
            if a < min_val:
                min_val = a
            i += 1
        return min_val