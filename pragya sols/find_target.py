arr = [7, 3, 9, 1]
target = 9
found = False

# Concept: Linear Search using enumerate to get both index and value
for i, val in enumerate(arr):
    if val == target:
        print(f"Output: Found at index {i}")
        found = True
        break

if not found:
    print("Target not found")