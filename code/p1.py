def solve_test_case(n, a):
    operations = []
    
    # Step 1: Check if all elements are already 0
    if all(x == 0 for x in a):
        return 0, []

    # Step 2: Perform operations
    k = 0
    while k < 8:
        i = 0
        while i < n:
            if a[i] != 0:
                j = i
                while j < n and a[j] != 0:
                    j += 1
                s = 0
                for x in range(i, j):
                    s ^= a[x]
                for x in range(i, j):
                    a[x] = s
                operations.append((i + 1, j))
                k += 1
            i += 1

    return k, operations

# Input
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    k, operations = solve_test_case(n, a)
    
    # Output
    print(k)
    for i, j in operations:
        print(i, j)
