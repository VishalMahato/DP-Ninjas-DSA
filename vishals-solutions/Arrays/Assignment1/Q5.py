# Print All 0’s and 1’s Separately
#  Given an array containing 0s and 1s, print all the 0s first and then all the 1s.

arr = [0,1,1,0,1,0]

# Approach 1
print("Approach 1:")    
count0=0

for num in arr:
    if num==0:
        count0+=1   

for i in range(count0):
    print(0, end=' ')
    
for i in range(len(arr)-count0):
    print(1, end=' ')

# output: 0 0 0 1 1 1