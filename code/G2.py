MOD = 998244353

def countArrays(N, K):
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    
    # Initialize base case
    dp[1][1:] = [1] * K
    
    for i in range(2, N + 1):
        for j in range(1, K + 1):
            # For each j, we can add j new elements to the last set,
            # and we can also add elements from the previous sets.
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
            dp[i][j] %= MOD
    
    total_ways = sum(dp[N]) % MOD
    
    return total_ways

N, K = map(int, input().split())
result = countArrays(N, K)
print(result)
