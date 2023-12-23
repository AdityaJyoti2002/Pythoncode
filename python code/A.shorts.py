# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the input string
    s = input()

    # Check if the string can be transformed to "abc" with one swap
    if s == "abc" or s == "acb" or s == "bac" or s =="cba":
        print("YES")
    else:
        print("NO")
