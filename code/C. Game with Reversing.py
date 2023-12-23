def optimal_game_duration(n, s, t):
    common_chars = sum(1 for a, b in zip(s, t) if a == b)
    diff_chars = n - common_chars

    if diff_chars <= 1:
        return common_chars + diff_chars

    return 2 * common_chars + 2 * (diff_chars - 2)


def main():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n = int(input())  # Length of strings
        s = input()  # String s
        t = input()  # String t
        result = optimal_game_duration(n, s, t)
        print(result)


if __name__ == "__main__":
    main()
