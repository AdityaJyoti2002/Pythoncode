# Read input
N = int(input())
arr = list(map(int, input().split()))

def min_operations_to_zero_product(arr):
    zero_count = arr.count(0)
    negative_count = sum(1 for num in arr if num < 0)
    positive_count = len(arr) - zero_count - negative_count
    
    # Case 1: If there are already zeros in the array, no additional operations needed.
    if zero_count > 0:
        return 0
    
    # Case 2: If negative_count is even, make all negative elements zero.
    if negative_count % 2 == 0:
        return negative_count
    
    # Case 3: If negative_count is odd, consider two options:
    # Option a: Make all negative elements zero (same as Case 2).
    # Option b: Choose one positive element and make it zero with one operation.
    # Return the minimum of these options.
    return min(negative_count, 1)

# Calculate and print the result
result = min_operations_to_zero_product(arr)
print(result)
