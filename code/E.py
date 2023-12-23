def canMakeEqual(a, b):
    # Check if characters at the same positions are equal
    for i in range(len(a)):
        if a[i] != b[i]:
            return False

    # Check if a can be transformed into b
    count_a = count_b = 0
    for i in range(len(a)):
        if a[i] == '1':
            count_a += 1
        if b[i] == '1':
            count_b += 1
        if count_a != count_b:
            return False

    return True

# Read the number of test cases
t = int(input().strip())

# Process each test case
for _ in range(t):
    # Read strings a and b for this test case
    a = input().strip()
    b = input().strip()

    # Check if it's possible to make a and b equal
    result = canMakeEqual(a, b)

    # Output the result for this test case
    if result:
        print("YES")
    else:
        print("NO")
