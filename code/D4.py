def reverse_substring(s, a, b):
    return s[:a] + s[a:b+1][::-1] + s[b+1:]

def process_test_case(n, k, s, l, r, q, x):
    for i in range(q):
        xi = x[i]
        for j in range(k):
            if l[j] <= xi <= r[j]:
                a = l[j] - 1
                b = r[j] - 1
                a_new = min(xi, b - a + 1)
                b_new = max(xi, b - a + 1)
                s = reverse_substring(s, a, b)
                x[i] = b_new
                break
    return s

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input()
        l = list(map(int, input().split()))
        r = list(map(int, input().split()))
        q = int(input())
        x = list(map(int, input().split()))
        result = process_test_case(n, k, s, l, r, q, x)
        print(result)

if __name__ == "__main__":
    main()
