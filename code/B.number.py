MOD = 998244353

# Function to calculate the number of pairs (p, q)
def count_pairs(N, A, B, M, C, D):
    # Calculate the prime factorizations of X and Y
    factors_X = {}
    factors_Y = {}
    
    for i in range(N):
        factors_X[A[i]] = B[i]
    
    for i in range(M):
        factors_Y[C[i]] = D[i]
    
    # Calculate all factors of X * Y
    factors_XY = {1}
    for factor in factors_X:
        factors_XY |= {factor**i * f for i in range(factors_X[factor] + 1) for f in factors_XY}
    
    # Calculate the count of pairs (p, q) such that p * q = F
    total_count = 1  # Initialize with 1 to account for the empty set
    for factor_F in factors_XY:
        count_F = 1
        for factor in factors_Y:
            count_F *= (factor_F * factor**(factors_Y[factor] + 1) - 1) // (factor - 1)
        total_count = (total_count * count_F) % MOD
    
    return total_count

# Read input
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# Calculate and print the result modulo 998244353
result = count_pairs(N, A, B, M, C, D)
print(result)
