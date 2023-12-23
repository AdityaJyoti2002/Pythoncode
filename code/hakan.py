n = int(input().strip())
mod = n % 2

if mod > 0:
    print("Weird")
elif mod == 0 and 2 <= n <= 5:
    print("Not Weird")
elif mod == 0 and 6 <= n <= 20:
    print("Werid")
else:
    print("Not Weird")
    
