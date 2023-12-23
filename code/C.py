def mex(arr):
    # Find the smallest non-negative integer that doesn't exist in the array.
    s = set(arr)
    mex_val = 0
    while mex_val in s:
        mex_val += 1
    return mex_val

def perform_operations(n, k, a):
    for _ in range(k):
        m = mex(a)
        a = [m] * n
    return a

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    modified_array = perform_operations(n, k, a)
    print(*modified_array)
