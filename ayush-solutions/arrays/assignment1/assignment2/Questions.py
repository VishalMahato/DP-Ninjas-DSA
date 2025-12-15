# Q.1 - Missing Number
arr  = [1, 2, 4, 5]
n = 5                           # n=5 isliye likha count kro ki array me kitne element hote missing wale ko bhi add krke 

Total_sum = n * (n+1) // 2      # ye formula 'n' jha tk hai sbko ek-ek krke add krne ka hai 
array_sum = sum(arr)            # yha pr arr me jitne elements hai unka addition kro

missing = Total_sum - array_sum   # yha pr total se arr ka minus kr rkha hai taki pta chle ki missing number kya hai 
print(f"Missing Number is: {missing}")








# Q.2 - Maximum Average Subarray 1 
def findMaxAverage(arr, k):
    # 'n' mein total elements ki ginti hai (6)
    n = len(arr) 

    # Pehli Window ka Sum
    window_sum = 0
    # Pehle 4 numbers (3, 9, 15, -4) ko jodega
    for i in range(k):
        window_sum += arr[i] 

    max_sum = window_sum # max_sum abhi 23 hai

    # Loop index 4 se shuru hoga
    for i in range(k, n):
        # Naya sum nikaalo: purana sum - bahar gaya number + andar aaya number
        window_sum = window_sum - arr[i - k] + arr[i]
        
        # Sabse bade sum ko yaad rakho
        if window_sum > max_sum:
            max_sum = window_sum

    # max_sum ko k se divide kar do
    return max_sum / k

my_array = [3, 9, 15, -4, -7, 5]
k_size = 4

# Function ko chalao aur result dekho
result = findMaxAverage(my_array, k_size)

print(f"Maximum Average: {result}")
