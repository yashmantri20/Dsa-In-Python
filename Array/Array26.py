# Array Subset of another array

def isSubset( a1, a2, n, m):
    for i in a2:
        if i not in a1:
            return "No"
    return "Yes"

    
def isSubset( a1, a2, n, m):
    a = list(set(a1) & set(a2))
    a.sort()
    a2.sort()
    if a == a2:
        return "Yes"
    else:
        return "No"