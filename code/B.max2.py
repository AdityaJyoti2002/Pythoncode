for _ in range(int(input())):

   l, r = input().split()
   a = len(r) - len(l)

if a > 0:
    l = '0' * a +l

n = len(r)

i=0

while i < n and l[i] == r[i]:
    i+=1
if i < n:
  print(int(r[i]) - int(l[i]) + 9 * (n-1-1))

else:
  print(0)