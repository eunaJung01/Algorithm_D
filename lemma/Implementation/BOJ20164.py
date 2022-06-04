# 홀수 홀릭 호석

import sys


# 홀수 개수 반환
def count_odd(N):
    count = 0
    for n in N:
        if int(n) % 2 != 0:
            count += 1
    return count


def func(N, oddNum):
    global max_result, min_result

    if len(N) >= 3:
        oddNum += count_odd(N)

        # decompose N
        for i in range(1, len(N) - 1):
            for j in range(i + 1, len(N)):
                temp = str(int(N[:i]) + int(N[i:j]) + int(N[j:]))
                func(temp, oddNum)

    elif len(N) == 2:
        oddNum += count_odd(N)
        temp = str(int(N[0]) + int(N[1]))
        func(temp, oddNum)

    else:
        oddNum += count_odd(N)
        max_result = max(max_result, oddNum)
        min_result = min(min_result, oddNum)
        return


N = sys.stdin.readline().strip()

max_result = -1
min_result = 9999999999

func(N, 0)
print(min_result, max_result)
