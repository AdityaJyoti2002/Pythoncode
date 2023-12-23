# Given numbers
a, b, c, d= map(int, input().split())

# Calculate the sum of all four numbers
# x1 = a +b
# x2 = a + c
#  x3 = b = c
# x4 = a + b + c +d
# Calculate a, b, and c using the given equations
# if max(a,b,c,d) != (a, b,c,d):
x1 = max(a, b,c, d) - a (a != max(a,b,c,d))
x2 = max(a,b,c,d) - c (c != max(a,b,c,d) )
x3 = max(a, b,c, d) - d (d != max(a,b,c,d) )
x4 = max(a,b,c, d) - b (b != max(a,b,c,d) )


# Print the guessed values of a, b, and c in any order

# print(xa, xb, xc)
print(x1, x2 , x3, x4)
