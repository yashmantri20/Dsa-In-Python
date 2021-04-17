# Write a program to cyclically rotate an array by one.

a = [1,2,3,4,5,6,7]
n = len(a)
print(a[n-1:]+a[:n-1])