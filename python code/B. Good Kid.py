# Function to calculate the maximum product for a given test case
def max_product(t, test_cases):
    results = []  # Store the results for each test case
    for i in range(t):
        n, digits = test_cases[i]
        max_digit = max(digits)  # Find the maximum digit in the array
        modified_digits = [d + 1 if d == max_digit and max_digit != 9 else d for d in digits]
        # Add 1 to the maximum digit if it's not 9
        product = 1
        for d in modified_digits:
            product *= d
        results.append(product)
    return results

# Input
t = int(input())  # Number of test cases
test_cases = []  # Store test cases as tuples (n, digits)
for _ in range(t):
    n = int(input())  # Number of digits in the array
    digits = list(map(int, input().split()))  # Digits in the array
    test_cases.append((n, digits))

# Calculate and output the results
results = max_product(t, test_cases)
for result in results:
    print(result)
