# 	Merge 2 sorted arrays without using Extra space.

import bisect

class Solution:
    def merge(self, arr1, arr2, n, m): 
        if len(arr2) < len(arr1):
            for i in arr2:
                arr1.insert(bisect.bisect(arr1, i),i)
            arr2.clear()
            return arr1,arr2
        else:
            for i in arr1:
                arr2.insert(bisect.bisect(arr2, i),i)
            arr1.clear()
            return arr1,arr2

class Solution:
    def merge(self, arr1, arr2, n, m): 
        arr1[:] = sorted(arr1+arr2)
        arr2.clear()
        return arr1, arr2

class Solution:
    def merge(self, arr1, arr2, n, m): 
        i = n - 1
        j = 0
        while j < m and i >= 0:
            if arr1[i] > arr2[j]:
                arr1[i] , arr2[j] = arr2[j] , arr1[i]
            j += 1
            i -= 1
        return arr1.sort(),arr2.sort()