import math

X, Y = map(int, input().split())


def win_rate(total, wins):
    return math.floor((wins / total) * 100)


Z = win_rate(X, Y)


def update_win_rate(total, wins, rate):
    rest = total - wins
    cnt = 0
    for i in range(rest):
        cnt += 1
        Z = win_rate(total + (i + 1), wins + (i + 1))
        if Z == rate:
            continue
        else:
            return cnt
    return -1


print(update_win_rate(X, Y, Z))
