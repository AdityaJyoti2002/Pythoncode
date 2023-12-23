MOD = 998244353

def sum_of_costs(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for j in range(1, k + 1):
        dp[1][j] = 1

    for i in range(2, n + 1):
        for j in range(1, k + 1):
            for l in range(1, k + 1):
                if l != j:
                    dp[i][j] = (dp[i][j] + dp[i - 1][l]) % MOD

    total_cost = sum(dp[n]) % MOD
    return total_cost

# Read input
n, k = map(int, input().split())
result = sum_of_costs(n, k)
print(result)
