# Function to determine if one of the numbers is the sum of the other two
def is_sum_of_two(a, b, c):
    if a + b == c or a + c == b or b + c == a:
        return "YES"
    else:
        return "NO"

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read the three integers
    a, b, c = map(int, input().split())
    
    # Check if one of them is the sum of the other two
    result = is_sum_of_two(a, b, c)
    
    # Output the result
    print(result)
