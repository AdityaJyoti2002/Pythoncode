def count_partitions(n):
    count = 0
    a = 1
    b = n - 1

    while a < b:
        count += 1
        a += 1
        b -= 1

    return count

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n = int(input())
    
    # Calculate the number of ways to distribute candies
    ways = count_partitions(n)
    
    print(ways)