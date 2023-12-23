def solve(k, s):
    char_count = [0] * 26
    for char in s:
        if char != '?':
            char_count[ord(char) - ord('a')] += 1
    
    left = [''] * k
    right = [''] * k
    left_idx = 0
    right_idx = k - 1
    
    for i in range(k):
        while left_idx < k and char_count[i] > 0:
            left[left_idx] = chr(ord('a') + i)
            right[right_idx] = chr(ord('a') + i)
            left_idx += 1
            right_idx -= 1
            char_count[i] -= 2
    
    if left_idx <= right_idx:
        return "IMPOSSIBLE"
    
    palindrome = ''.join(left) + ''.join(right)
    
    if len(palindrome) % 2 == 1:
        middle_char = chr(ord('a') + k - 1)
        palindrome = palindrome[:len(palindrome) // 2] + middle_char + palindrome[len(palindrome) // 2:]
    
    return palindrome

# Read input
k = int(input())
s = input()

# Call the solve function
result = solve(k, s)
print(result)
