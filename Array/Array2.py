# Find the "Kth" max and min element of an array

a = [2,5,1,8,3,7,9]
K = 2

# Directly
a.sort()
print(a[K - 1],a[len(a) - K])

# if no direct function then use merge sort