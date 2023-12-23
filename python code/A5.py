def find_missing_team_efficiency(n, efficiencies):
    # Calculate the sum of efficiencies of the given teams
    total_efficiency = sum(efficiencies)
    
    # Calculate the sum of their opponents' efficiencies
    total_opponents_efficiency = sum(map(abs, efficiencies))
    
    # Calculate the missing team's efficiency
    missing_team_efficiency = total_efficiency - total_opponents_efficiency
    
    return missing_team_efficiency

# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the number of teams
    n = int(input())
    
    # Read the efficiencies of n-1 teams
    efficiencies = list(map(int, input().split()))
    
    # Find and print the efficiency of the missing team
    result = find_missing_team_efficiency(n, efficiencies)
    print(result)
