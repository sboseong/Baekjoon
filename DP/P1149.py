# N
N = int(input())

# Cost
Cost = [[int(value) for value in input().split()] for _ in range(N)]

# DP list initialize
DP = [[0, 0, 0] for _ in range(N+1)]

for idx in range(1, N+1):
    DP[idx][0] = Cost[idx-1][0] + min(DP[idx-1][1], DP[idx-1][2])
    DP[idx][1] = Cost[idx-1][1] + min(DP[idx-1][0], DP[idx-1][2])
    DP[idx][2] = Cost[idx-1][2] + min(DP[idx-1][0], DP[idx-1][1])

# Output
print(min(DP[N][0], DP[N][1], DP[N][2]))