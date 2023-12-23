MOD = 998244353

# Function to calculate the sum of scores for a given test case
def calculate_scores(n, m):
    ans = 0
    
    # Calculate the maximum possible value of max_value for the given n
    max_value = 1
    while max_value * 2 <= n:
        max_value *= 2
    
    for i in range(1, max_value + 1):
        ans = (ans + min(i + m, n) - i + 1) % MOD
    
    return ans

# Input processing
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    result = calculate_scores(n, m)
    print(result)
