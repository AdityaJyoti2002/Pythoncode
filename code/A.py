# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    n, a, q = map(int, input().split())
    notifications = input().strip()

    # Initialize the number of subscribers online
    subscribers_online = a

    # Iterate through each notification
    result = "MAYBE"
    for notification in notifications:
        if notification == '+':
            subscribers_online += 1
        else:
            subscribers_online -= 1
        
        # Check conditions for guaranteed, impossible, or maybe scenarios
        if subscribers_online == n:
            result = "YES"
            break
        if subscribers_online == 0:
            result = "NO"
            break
    
    print(result)
