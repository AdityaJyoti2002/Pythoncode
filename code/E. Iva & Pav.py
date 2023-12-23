def minimum_m_values(test_cases):
    results = []
    for n, a in test_cases:
        m = 0
        elements_set = set(a)
        current_mex = 0
        
        for _ in range(n):
            while current_mex in elements_set:
                current_mex += 1
            m += current_mex
            elements_set.add(current_mex)
        
        results.append(m)
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Calculate and print results
results = minimum_m_values(test_cases)
for result in results:
    print(result)
