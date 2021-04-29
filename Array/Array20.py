# Find if there is any subarray with sum equal to 0

def subArrayExists(self,arr,n):
    sum_val = 0
    s = set()
    
    for i in range(n):
        sum_val += arr[i]
        if sum_val == 0 or sum_val in s:
            return True
        s.add(sum_val)
    
    return False