import sys
import math

def min_airfare_cost(n, k, a, b, cities):
    major_cities = cities[:k]
    other_cities = cities[k:]

    # Calculate the direct flight cost between major cities
    direct_flight_cost = [0] * k
    for i in range(k):
        for j in range(k):
            if i != j:
                direct_flight_cost[i] = max(direct_flight_cost[i], abs(major_cities[i][0] - major_cities[j][0]) + abs(major_cities[i][1] - major_cities[j][1]))

    # Find the minimum cost to travel from city 'a' to city 'b'
    min_cost = math.inf
    for i in range(k):
        cost_from_a = abs(cities[a - 1][0] - major_cities[i][0]) + abs(cities[a - 1][1] - major_cities[i][1])
        for j in range(k):
            cost_to_b = abs(cities[b - 1][0] - major_cities[j][0]) + abs(cities[b - 1][1] - major_cities[j][1])
            if i == j:
                min_cost = min(min_cost, cost_from_a + cost_to_b)
            else:
                min_cost = min(min_cost, cost_from_a + direct_flight_cost[i] + cost_to_b)

    return min_cost

def main():
    t = int(input())
    for _ in range(t):
        n, k, a, b = map(int, input().split())
        cities = [tuple(map(int, input().split())) for _ in range(n)]
        result = min_airfare_cost(n, k, a, b, cities)
        print(result)

if __name__ == "__main__":
    main()

# Example Input:
# 5
# 6 2 3 5
# 0 0
# 1 -2
# -2 1
# -1 3
# 2 -2
# -3 -3
# 2 0 1 2
# -1000000000 -1000000000
# 1000000000 1000000000
# 7 5 4 2
# 154 147
# -154 -147
# 123 456
# 20 23
# 43 20
# 998 244
# 353 100
# 3 1 3 1
# 0 10
# 1 20
# 2 30
# 4 3 2 4
# 0 0
# -100 100
# -1 -1
# -1 0

# Expected Output:
# 4
# 4000000000
# 0
# 22
# 1
