# Q.2 - Print Array Elements After Multiplying by 5
#   Write a program that multiplies every element in the given array by 5 and prints the updated array.

# Approach 1
print("Approach 1:")
arr = [2, 4, 6, 8] 

for num in arr:
    print(num *5, end=' ') 

# Output: 2 4 6 8

# Approach 2 
print("\nApproach 2:")
for i in range(len(arr)): 
    print(arr[i] *5, end=' ') 

# Approach 3
print("\nApproach 3:")

for index, value in enumerate(arr):
   
    print(value *5, end=' ')

# Approach 4
print("\nApproach 4:")

print(*[x *5 for x in arr])  

# it is just like Approach 1 with soome sugar syntax of list comprehension 
# breakdown of the syntax:
# [x *5 for x in arr]
# Here, we are creating a new list by multiplying each element x in the original array arr by 5.
# how to use this type of syntax in other scenarios?
# you use this syntax when you want to create a new list by applying an operation to each element of an existing iterable (like a list or array).
# but you can also use this to filter elements by adding an if condition at the end like this:
# [x *5 for x in arr if x > 4]


# Approach 5
print("Approach 5:")
print(" ".join(map(lambda x: str(x *5), arr)))

# lambda function is an anonymous function as the cool guys say it but what its really means is that a function without a name.
# Here, lambda x: str(x *5) is a small function that takes an input x, multiplies it by 5, and converts the result to a string.
# This lambda function is applied to each element of arr using the map function.



