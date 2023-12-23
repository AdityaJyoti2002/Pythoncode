def solve():
    size = int(input())
    minus = input().count("-1")
    plus = size - minus
    total = 0
    
    while plus - minus < 0 or minus & 1:
        plus += 1
        minus -= 1
        total += 1
        
    print(total)
    
    
if __name__ == "__main__":
    for test in range(int(input())):
        solve()
        