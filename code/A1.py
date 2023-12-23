def construct_pseudotree(t, test_cases):
    results = []
    
    for i in range(t):
        n, degrees = test_cases[i]
        degree_counts = [0] * (n + 1)
        vertices = []
        edges = []

        for d in degrees:
            degree_counts[d] += 1

        # Check if it's impossible to construct a flower-like pseudotree
        if degree_counts[1] < 2 or degree_counts[n] != 1:
            results.append("No")
        else:
            u = v = 1
            success = True

            for d in degrees:
                if degree_counts[d] == 0:
                    success = False
                    break
                degree_counts[d] -= 1

                for _ in range(d):
                    vertices.append((u, v))
                    u, v = v, v + 1

                if degree_counts[d] > 0:
                    v = 1
                else:
                    u += 1

            if success:
                results.append("Yes")
                results.extend(f"{u} {v}" for u, v in vertices)
            else:
                results.append("No")

    return results


t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    degrees = list(map(int, input().split()))
    test_cases.append((n, degrees))

results = construct_pseudotree(t, test_cases)

for result in results:
    print(result)
