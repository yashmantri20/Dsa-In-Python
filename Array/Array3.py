# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
a = [0, 2, 1, 2, 0]

# Directly
a.sort()
print(a)

# without sort method
left = 0
right = len(a) - 1
mid = 0

while(mid <= right):
    if a[mid] == 0:
        a[mid], a[left] = a[left], a[mid]
        left += 1
        mid += 1
    elif a[mid] == 1:
        mid += 1
    elif a[mid] == 2:
        a[mid], a[right] = a[right], a[mid]
        right -= 1

print(a)