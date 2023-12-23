def main():
    x = int(input())

    Numberofsteps = (x // 5) + (1 if x % 5 > 0  else 0)
    print(Numberofsteps)

if __name__ == "__main__":
    main()



