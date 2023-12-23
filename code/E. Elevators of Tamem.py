# Read input
N = int(input())
offensive_values = list(map(int, input().split()))
defensive_values = list(map(int, input().split()))
Q = int(input())

# Initialize offensive and defensive rankings for each player
offensive_rankings = [0] * N
defensive_rankings = [0] * N

# Function to calculate the overall ranking
def calculate_overall_ranking(player_index):
    overall_rank = 0
    for j in range(N):
        if offensive_rankings[j] + defensive_rankings[j] < offensive_rankings[player_index] + defensive_rankings[player_index]:
            overall_rank += 1
    return overall_rank

# Process events
for _ in range(Q):
    event = input().split()  # Read the event
    event_type = int(event[0])
    player_index = int(event[1]) - 1  # Adjust for 0-based indexing
    
    if event_type == 1:
        # Event type 1: Update offensive value
        c = int(event[2])
        offensive_rankings[player_index] += c
    elif event_type == 2:
        # Event type 2: Update defensive value
        c = int(event[2])
        defensive_rankings[player_index] += c
    elif event_type == 3:
        # Event type 3: Calculate and print overall ranking
        overall_rank = calculate_overall_ranking(player_index)
        print(overall_rank + 1)  # Add 1 to match the 1-based indexing in the problem statement
