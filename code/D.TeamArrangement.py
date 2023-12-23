from collections import deque

n = int(input())
results = list(map(int, input().split()))
teams = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

def solve(n, results, teams, k):
    priorities = [[] for _ in range(3 * n)]
    
    for team in teams:
        team.sort()
        for i in range(3):
            priorities[team[i] - 1] = [team[j] for j in range(3) if j != i]
    
    available = set(range(1, 3 * n + 1))
    for team in teams:
        available.difference_update(team)
    
    answer = []
    queue = deque([k])
    
    while queue:
        current = queue.popleft()
        answer.append(min(priorities[current - 1]))
        queue.append(priorities[current - 1][1])
        available.remove(current)
        available.remove(queue[-1])
    
    return answer



# Solve the problem and print the result
result = solve(n, results, teams, k)
print(' '.join(map(str, result)))
