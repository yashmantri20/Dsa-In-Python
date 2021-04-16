# Find the Union and Intersection of the two sorted arrays

# Directly 

a = {1,2,2,3,4,5}
b = {1,2,2}
print(a | b)
print(a & b)

# Union

union = list(a)

for i in b:
    if i not in union:
        union.append(i)

print(union)

# Intersection

intersection = []
for i in b:
    if i in a:
        intersection.append(i)

print(intersection)