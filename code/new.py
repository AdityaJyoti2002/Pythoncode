def update(bit, idx, val):
    while idx < len(bit):
        bit[idx] = min(bit[idx], val)
        idx += idx & -idx

def query(bit, idx):
    min_val = float('inf')
    while idx > 0:
        min_val = min(min_val, bit[idx])
        idx -= idx & -idx
    return min_val

def solve_typewriter(n, p, queries):
    bit = [float('inf')] * (n + 1)
    ans = []

    for pi in p:
        update(bit, pi, 0)

    ans.append(query(bit, n))

    for query in queries:
        t = query[0]

        if t == 1 or t == 2:
            k = query[1]
            ans.append(min(query(bit, n), query(bit, k)))
        elif t == 3:
            ans.append(query(bit, n))

    return ans

# Read input
n = int(input())
p = list(map(int, input().split()))
q = int(input())
queries = []

for _ in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

# Solve and output
ans = solve_typewriter(n, p, queries)
for val in ans:
    print(val)
