# Print All 0’s and 1’s Separately
#  Given an array containing 0s and 1s, print all the 0s first and then all the 1s.
arr = [1, 0, 1, 0, 0, 1]

countZero = 0
countOne = 0

for num in arr:
    if num == 0:
        countZero += 1
    else:
        countOne += 1

# print 0s first
for i in range(countZero):
    print(0, end=" ")

# Then print 1s
for i in range(countOne):
    print(1, end=" ")
