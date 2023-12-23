def castleGame(N, M, special_tiles):
    # Initialize the dp table with all zeros
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # Mark the special tiles as winning positions for the respective players
    for (x, y) in special_tiles:
        dp[x][y] = 1 if (x + y) % 2 == 0 else -1

    # Start filling the dp table from the bottom-right corner
    for i in range(N, 0, -1):
        for j in range(M, 0, -1):
            if dp[i][j] == 0:  # This position is not already marked as a win or lose
                # For Chaneka's turn
                chaneka_wins = False
                for r in range(i + 1, N + 1):
                    if dp[r][j] == -1:
                        chaneka_wins = True
                        break
                for c in range(j + 1, M + 1):
                    if dp[i][c] == -1:
                        chaneka_wins = True
                        break

                # For Bhinneka's turn
                bhinneka_wins = False
                for r in range(i + 1, N + 1):
                    if dp[r][j] == -1:
                        bhinneka_wins = True
                        break
                for c in range(j + 1, M + 1):
                    if dp[i][c] == -1:
                        bhinneka_wins = True
                        break

                # Determine the result for this position
                if chaneka_wins:
                    dp[i][j] = 1
                elif bhinneka_wins:
                    dp[i][j] = -1
                else:
                    dp[i][j] = 1  # Chaneka wins by default

    # The result at position (1, 1) will determine the winner of the game
    return "Chaneka" if dp[1][1] == 1 else "Bhinneka"

# Read input
N, M, K = map(int, input().split())
special_tiles = []
for _ in range(K):
    x, y = map(int, input().split())
    special_tiles.append((x, y))

# Determine the winner and print the result
winner = castleGame(N, M, special_tiles)
print(winner)
