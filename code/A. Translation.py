def is_reversed_translation(s, t):
    return s == t[::-1]

# Read input
s = input().strip()
t = input().strip()

# Check if t is a reversed translation of s
if is_reversed_translation(s, t):
    print("YES")
else:
    print("NO")

