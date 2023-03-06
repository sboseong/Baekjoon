# Test Case
T = int(input())

# DP list initialize
tmp = [i+1 for i in range(14)]
DP = [tmp[:]]

for f in range(1, 15):
    DP.append(tmp[:])

    for n in range(1, 14):
        DP[f][n] = DP[f-1][n] + DP[f][n-1]

for _ in range(T):
    # Floor, Number
    Floor = int(input())
    Number = int(input())

    # Output
    print(DP[Floor][Number-1])