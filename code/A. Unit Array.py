# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the length of the array
    n = int(input())
    
    # Read the array elements
    arr = list(map(int, input().split()))
    pos_count = n - arr
    total = 0
    # Initialize counts
    neg_count = -1
    pos_count = 0
    
    # Count the number of "-1" and "1" elements
    for num in arr:
        if neg_count>pos_count:
            neg_count += 1((neg_count-pos_count)/2==0)
        else:
            pos_count += 1

    
    
    # Calculate the minimum operations required
    min_operations = min(neg_count, pos_count)
    
    # Print the result
    print(min_operations)
