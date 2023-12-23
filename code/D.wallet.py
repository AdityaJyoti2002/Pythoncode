import heapq

def max_total_money(N, M, K, arrays):
    total_money = 0
    max_heap = []

    for array in arrays:
        for i in range(M - K + 1):
            heapq.heappush(max_heap, -array[i])

    for p in range(1, M - K + 2):
        max_val = -heapq.heappop(max_heap)
        total_money += max_val

        for i in range(N):
            if arrays[i].count(max_val) > 0:
                x = i
                y = arrays[i].index(max_val)
                arrays[i][y] = 0
                if y + 1 < M:
                    heapq.heappush(max_heap, -arrays[i][y + 1])

    return total_money

# Read input
N, M, K = map(int, input().split())
arrays = []
for i in range(N):
    array = list(map(int, input().split()))
    arrays.append(array)

result = max_total_money(N, M, K, arrays)
print(result)  # This will print the maximum total money Chaneka can earn.
