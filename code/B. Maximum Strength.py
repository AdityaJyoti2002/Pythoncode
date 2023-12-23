def max_weapon_strength(L, R):
    max_strength = 0
    min_length = min(len(L), len(R))
    
    for i in range(min_length):
        diff = abs(int(L[i]) - int(R[i]))
        max_strength += diff
    
    if len(L) > len(R):
        max_strength += int(L[min_length:])
    elif len(R) > len(L):
        max_strength += int(R[min_length:])
    
    return max_strength

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    L, R = input().split()
    result = max_weapon_strength(L, R)
    print(result)

