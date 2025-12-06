#Q3. Find the Target in the Array
#Write a program to find whether a given target value exists in the array or not.

#input array
arr=[7,3,9,1]
#target value to search
target=9

def find_target(arr, target):
    # Step 1: Go through each index of the array
    for i in range(len(arr)):
        
        # Step 2: Check if the current element matches the target
        if arr[i] == target:
            print("Found at index", i)
            return i   # stop the function once found

    # Step 3: If loop finishes and nothing matched
    print("Not found")
    