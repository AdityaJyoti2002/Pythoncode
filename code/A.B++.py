def main():
    x = 0
    n = int(input())
    
    for _ in range(n):
        statement = input()
        if "++" in statement:
            x += 1
        elif "--" in statement:
            x -= 1
    
    print(x)

if __name__ == "__main__":
    main()
