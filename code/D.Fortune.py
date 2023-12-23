n = int(input())  # Number of flowers
petals = list(map(int, input().split()))  # Petals on each flower

# Initialize the maximal number of petals to 0
max_petals = 0

# Iterate through the flowers
for petal in petals:
    # If the current flower has an odd number of petals, add its petals to the max_petals
    if petal % 2 == 1:
        max_petals += petal

# Print the maximal number of petals, which would result in "Loves"
print(max_petals)