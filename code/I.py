def can_make_equal_strings(a, b):
    count_0_a = a.count('0')
    count_1_a = a.count('1')
    count_0_b = b.count('0')
    count_1_b = b.count('1')
    
    if count_0_a != count_0_b or count_1_a != count_1_b:
        return False
    
    mismatch_positions = []
    for i in range(len(a)):
        if a[i] != b[i]:
            mismatch_positions.append(i)
    
    for position in mismatch_positions:
        l = position
        r = mismatch_positions[mismatch_positions.index(position) + 1] if mismatch_positions.index(position) + 1 < len(mismatch_positions) else len(a)
        
        substring_a = a[l+1:r]
        substring_b = b[l+1:r]
        
        if substring_a != substring_b:
            return False
    
    return True

# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read two strings for each test case
    a = input()
    b = input()
    
    result = can_make_equal_strings(a, b)
    if result:
        print("YES")
    else:
        print("NO")
