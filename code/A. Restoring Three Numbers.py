a = [int (v) for v in input().split()]
vmax = max(a)

b = [vmax - v for v in a if vmax != v]


b.sort(reverse=True)

print(*b)