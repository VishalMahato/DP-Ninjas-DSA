# Print All 0’s and 1’s Separately
#  Given an array containing 0s and 1s, print all the 0s first and then all the 1s.
arr = [1, 0, 1, 0, 0, 1, 1, 0]
arr.sort()   # array ko sort krega 

for item in arr:
    print(item, end=" ")
    