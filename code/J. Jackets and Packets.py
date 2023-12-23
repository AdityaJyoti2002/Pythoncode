from collections import defaultdict

# Input
N, X, Y = map(int, input().split())
colors = list(map(int, input().split()))

# Initialize variables
left_stack = colors
right_stack = []
color_counts = defaultdict(int)
total_time = 0

# Iterate through colors and pack jackets
for color in left_stack:
    if color in right_stack:
        # Perform packing from the right stack
        right_stack.remove(color)
        total_time += X
    elif color_counts[color] > 0:
        # Perform packing from the left stack
        color_counts[color] -= 1
        total_time += X
    else:
        # Perform packing for the current jacket from the left stack
        left_stack.remove(color)
        total_time += X
    color_counts[color] += 1

# Move remaining jackets from left stack to right stack
while left_stack:
    left_stack.pop([])
    right_stack.append(colors.pop([]))
    total_time += Y

print(total_time)
