n = int(input())
a = list(map(int, input().split()))
mod = 10**9 + 7

dp = [0] * (n + 1)
lastIndex = {}

for i in range(1, n + 1):
    dp[i] = dp[i - 1]
    if a[i - 1] in lastIndex:
        dp[i] = (dp[i] + dp[lastIndex[a[i - 1]]]) % mod
    lastIndex[a[i - 1]] = i

print(dp[n])
