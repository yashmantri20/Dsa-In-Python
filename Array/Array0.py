#Reverse the array

arr = [1,2,3,4,5,5,4,7,8,2]

#Using reversed Function
print(list(reversed(arr)))

#Directly
print(arr[::-1])

#Using Loop
j = len(arr) - 1
for i in range(len(arr)//2):
    arr[i], arr[j] = arr[j],arr[i]
    j -= 1
print(arr)