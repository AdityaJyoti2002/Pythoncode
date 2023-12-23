n, m = map(int, input().split())

# Initialize the maximum number of balls and the corresponding K
max_balls = 0
best_k = 1

# Iterate through possible values of K from 1 to M
for k in range(1, m + 1):
    total_balls = 0
    for j in range(1, n + 1):
        i = ((j * k - 1) % n) + 1
        total_balls += i
    if total_balls > max_balls:
        max_balls = total_balls
        best_k = k

print(best_k)
