def is_possible_swap(n, candies):
    total_candies = sum(candies)
    
    if total_candies % n != 0:
        return "No"  # If the total candies cannot be evenly distributed, return "No"

    target_candies = total_candies // n  # The target number of candies each person should have

    for candy_count in candies:
        if candy_count > target_candies:
            return "No"  # If anyone has more candies than the target, return "No"

    return "Yes"

# Input processing
t = int(input())
for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    
    result = is_possible_swap(n, candies)
    print(result)
