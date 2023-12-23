MOD = 998244353

def calculate_scores(n, m, a):
    # Calculate the maximum value for all pairs (i, j)
    max_values = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        max_values[i][i] = a[i]
    
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            k = i
            max_val = a[i]
            while k != j:
                k //= 2
                max_val = max(max_val, a[k])
            max_values[i][j] = max_val
            max_values[j][i] = max_val
    
    # Compute the sum of scores for all possible travel plans
    total_score = 0
    
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            total_score += max_values[i][j]
            total_score %= MOD
    
    return total_score

# Input processing
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [0] + list(map(int, input().split()))  # Add a dummy element at the beginning
    result = calculate_scores(n, m, a)
    print(result)
