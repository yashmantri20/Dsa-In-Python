# find common elements In 3 sorted arrays

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        l = []
        arr = sorted(list(set(A) & set(B) & set(C)))
        return arr