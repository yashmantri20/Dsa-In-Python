# Move all the negative elements to one side of the array

a = [-12, 11, -13, -5, 6, -7, 5, -3, -6]

left = 0
start = 0

while start < len(a):
    if a[start] < 0:
        a[start], a[left] = a[left], a[start]
        left += 1
    start += 1

print(a)