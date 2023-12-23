def is_consistent_sequence(sequence):
    array_length = 0
    is_sorted = True
    expected_next = '+'
    
    for char in sequence:
        if char == '+':
            array_length += 1
        elif char == '-':
            array_length -= 1
        else:  # '0' or '1'
            if array_length <= 1:
                expected_next = '1'
            else:
                expected_next = char
            
            if char == '0':
                if is_sorted:
                    return False
            elif char == '1':
                is_sorted = True
            else:
                return False  # Invalid character
            
        if array_length < 0:
            return False  # Trying to remove from an empty array
            
    return True

# Read the number of test cases
t = int(input())

for _ in range(t):
    sequence = input().strip()
    result = is_consistent_sequence(sequence)
    if result:
        print("YES")
    else:
        print("NO")
