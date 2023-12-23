# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    n = int(input())  # Read the length of the permutation
    p = list(map(int, input().split()))  # Read the permutation

    moves = 0  # Initialize the moves counter

    # Iterate through the permutation
    for i in range(n):
        if p[i] != i + 1:
            # Find the next index where p[j] = i + 1
            j = p.index(i + 1, i)
            # Swap elements p[i] and p[j]
            p[i], p[j] = p[j], p[i]
            moves += 1
    
    # Output the minimum number of operations for this test case
    print(moves)

