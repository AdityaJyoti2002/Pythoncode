import math

def smallest_good_integer(n, arr):
    MAX_VAL = 10**9 + 1
    is_bad = [False] * MAX_VAL
    smallest_good = None
    
    for i in range(n):
        num = arr[i]
        factors = []
        
        # Find prime factors of num
        for factor in range(2, int(math.sqrt(num)) + 1):
            if num % factor == 0:
                factors.append(factor)
                while num % factor == 0:
                    num //= factor
        if num > 1:
            factors.append(num)
        
        # Mark multiples of factors as bad
        for factor in factors:
            if not is_bad[factor]:
                for multiple in range(factor, MAX_VAL, factor):
                    is_bad[multiple] = True
        
        # Find the smallest good integer
        if smallest_good is None:
            smallest_good = arr[i]
        else:
            smallest_good = min(smallest_good, arr[i])
        
    # Find the smallest good integer that is not marked as bad
    for i in range(smallest_good, MAX_VAL):
        if not is_bad[i]:
            return i

# Read input
num_tests = int(input())
for _ in range(num_tests):
    n = int(input())
    arr = list(map(int, input().split()))
    result = smallest_good_integer(n, arr)
    print(result)
