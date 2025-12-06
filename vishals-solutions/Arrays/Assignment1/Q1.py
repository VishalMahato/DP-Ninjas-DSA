# Q1. Print an Array
# This program takes an array and prints each element in a single line.

arr = [2, 4, 6, 8] 

# Looping through each element and print it
for num in arr:
    print(num, end=' ')  # Using end=' ' , end do not print in new line and print a space instead or whatever is given in end=''

# Output: 2 4 6 8

# Approach 2 
print("Approach 2:")
for i in range(len(arr)): 
    print(arr[i], end=' ') 

# Approach 3
print("\nApproach 3:")

for index, value in enumerate(arr):
    #  enumerate creates enumerator that contains index and value 
    print(value, end=' ')

# Approach 4
print("\nApproach 4:")
print(*arr)  # The asterisk * unpacks the array elements and prints them separate like in Javascript's console.log(...arr)

# Approach 5
print("Approach 5:")
print(" ".join(map(str, arr)))  

#  join - joins the element with whatever is given in quotes
#  map - map repeats the function given to each element of array

# what does map method do genarally?
# The map() function in Python applies a specified function to each item of an iterable (like a list or array) and returns an iterator that produces the results.
# It doesn't modify the original iterable; instead, it creates a new iterator with the transformed items.
#  Here, map(str, arr) converts each integer in arr to a string so that join can concatenate them.
# also map returns an iterator and not a list so we need to convert it to list if we want to use it as a list.

