arr = [5, 2, 9, 1, 7, 6]

for x in arr:
    print(x)

print("Sum:", sum(arr))
print("Max:", max(arr))
print("Min:", min(arr))

arr.insert(3, 10) 
del arr[1]          
print("After changes:", arr)

even = [x for x in arr if x % 2 == 0]
odd = [x for x in arr if x % 2 != 0]
print("Even:", even)
print("Odd:", odd)

