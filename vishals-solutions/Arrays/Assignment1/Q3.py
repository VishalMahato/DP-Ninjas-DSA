# Q.3 - Find the Target in the Array
#       Write a program to find whether a given target value exists in the array or not.

arr = [4, 6, 9, 2, 10, 13]
target = 10 

# Approach 1
print("Approach 1 :")

for num in arr:
    if num == target:
        print("found:", num)
        # if need index then use index() ,then dont use for num in arr loop as it will only know the value not the index, though can return true or false
    


# Approach 2
print("Approach 2 :")
for i in range(len(arr)): 
    if arr[i] == target:   
        print("found:", i)

# Approach 3
print("Approach 3 :")
for index, value in enumerate(arr):
    if value == target:
        print("found :", index)

# Approach 4
print("Approach 4 :")
if ([True for x in arr if x == target])  : 
    print("target exists in array")
else:
    print("target does not exist in array")

# Approach 5
print("Approach 5 :")
if target in arr:
    print("target exists in array")
else:
    print("target does not exist in array")
#  in keyword checks if the target is present in the array or not and returns true or false
