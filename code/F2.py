def solve(n, player_cards, remaining_cards):
    total_player_cards = [sum(player_cards[i]) for i in range(n)]
    max_player_cards = max(total_player_cards)
    total_remaining_cards = sum(remaining_cards)
    
    max_points = []
    for i in range(n):
        possible_player_cards = total_player_cards[i] + total_remaining_cards
        max_possible_cards = max(possible_player_cards)
        if possible_player_cards[i] == max_possible_cards:
            max_points.append(max_possible_cards - max_player_cards)
        else:
            max_points.append(0)
    
    return max_points

# Read input
n = int(input())
player_cards = []
for _ in range(n):
    player_cards.append(list(map(int, input().split())))
remaining_cards = list(map(int, input().split()))

# Solve the problem and print the result
result = solve(n, player_cards, remaining_cards)
print(' '.join(map(str, result)))
