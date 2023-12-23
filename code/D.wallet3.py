# Read input
N, M, K = map(int, input().split())
arrays = []
for _ in range(N):
    array = list(map(int, input().split()))
    arrays.append(array)

# Initialize total money earned
total_money = 0

# Perform operations
for p in range(1, M - K + 2):
    max_value = 0
    max_i = -1
    max_j = -1
    for i in range(N):
        for j in range(M - K + 1):
            subarray_sum = sum(arrays[i][j:j+K])
            if subarray_sum > max_value:
                max_value = subarray_sum
                max_i = i
                max_j = j
    total_money += max_value
    # Change the chosen elements to 0
    for j in range(max_j, max_j + K):
        arrays[max_i][j] = 0

# Print the result
print(total_money)
