# Q.3 - Find the Target in the Array
#       Write a program to find whether a given target value exists in the array or not.
arr = [4, 6, 9, 2, 10, 13]
target = 10

for i in range(len(arr)):  # yha pr humne len() function ka use isliye kiya kyunki humko output index value me chaiye tha 
    if arr[i] == target:   # yha pr i and target ka compare hoga 
        print("Found at index:", i)