def solve_test_case(n, m, topics):
    # Create a list to store the changes in hand height for each student
    changes = [0] * n

    # Iterate through each student's learned topics and calculate the changes
    for i in range(n):
        l, r = topics[i]
        changes[i] = l - 1  # Lower the hand by 1 for topics before the learned range
        changes[i] -= i     # Lower the hand by 1 for each topic learned before student i

    # Sort the changes in descending order
    changes.sort(reverse=True)

    # Calculate the maximum difference in hand heights
    max_difference = 0
    cur_height = 0
    for i in range(n):
        cur_height += changes[i]
        max_difference = max(max_difference, cur_height)

    return max_difference

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    n, m = map(int, input().split())
    topics = [tuple(map(int, input().split())) for _ in range(n)]
    result = solve_test_case(n, m, topics)
    print(result)
