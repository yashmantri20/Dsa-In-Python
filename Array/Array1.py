# Find the maximum and minimum element in an array

a = [5,9,4,5,8,5]

# Directly
print(min(a),max(a))

# with loop 

min_val = a[0]
max_val = a[0]

for i in a:
    if min_val > i:
        min_val = i

    if max_val < i:
        max_val = i
print(min_val,max_val)