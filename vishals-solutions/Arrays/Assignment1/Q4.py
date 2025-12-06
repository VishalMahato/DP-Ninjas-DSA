# Q.4 - Find Minimum and Maximum in an Array
#    Write a program to find the smallest (min) and largest (max) number in the array.

# Approch 1 
arr = [2, 6, 9, 15, 29, 7]
minimum = min(arr)
maximum = max(arr)
print("min is ", minimum)
print("max is ", maximum)

# Approch 2 
print("Approch 2 :")
min = arr[0]
max = arr[0]
#  get the first value and jsut compare with next for lower or higher and if fount the variable 

for num in arr:
    if num < min:
        min = num
    if num > max:
        max_val = num

print("min is ", min)
print("max is ", max)

# output:
# min is  2
# max is  29