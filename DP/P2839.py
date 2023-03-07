# Kilogram
Kilogram = int(input())

# DP list initialize
DP = [-1 for _ in range(5001)]
DP[3] = 1
DP[5] = 1
DP[6] = 2
exception_number = [0, 1, 2, 4, 5, 7]

for idx in range(8, len(DP)):
    if idx in exception_number:
        continue

    tmp = 1
    answer_tmp = idx

    while True:
        if (idx-tmp) < tmp:
            break
        else:
            if DP[tmp] != -1 and DP[idx-tmp] != -1:
                answer_tmp = min(answer_tmp, DP[tmp] + DP[idx-tmp])

        tmp += 1

    DP[idx] = answer_tmp

# Output
print(DP[Kilogram])