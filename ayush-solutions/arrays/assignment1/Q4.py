# Q.4 - Find Minimum and Maximum in an Array
#       Write a program to find the smallest (min) and largest (max) number in the array.

arr = [12, 5, 34, 2, 19]

# Assume first element is min and max
minimum = arr[0]
maximum = arr[0]

for num in arr:
    # Checking minimum
    if num < minimum:
        minimum = num
    # Checking maximum
    if num > maximum:
        maximum = num

print("Smallest number:", minimum)
print("Largest number:", maximum)
