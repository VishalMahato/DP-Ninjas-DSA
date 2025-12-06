# Program to print all 0s first and then all 1s

# Step 1: Write the input array
arr = [1, 0, 1, 0, 0, 1]

# Step 2: Count how many 0s are in the array
zeroCount = arr.count(0)

# Step 3: Count how many 1s are in the array
oneCount = arr.count(1)

# Step 4: Make a new array with all 0s first, then all 1s
new_arr = [0] * zeroCount + [1] * oneCount

# Step 5: Print the final array
print(*new_arr)

