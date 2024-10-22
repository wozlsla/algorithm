L = [64, 72, 83, 72, 54]
x = 72


# def solution(L, x):
#     idx = []
#     while 1:
#         if x in L:
#             i = L.index(x)
#             idx.append(i)
#             L.remove(x)
#             # del L[i]
#         else:
#             if len(idx) == 0:
#                 idx = [-1]
#             break

#     return idx


# def solution(L, x):
#     idx = []
#     if x in L:
#         for i in L:
#             print(i)
#             if i == x:
#                 idx.append(L.index(i))
#     else:
#         idx = [-1]

#     return idx


# def solution(L, x):
#     idx = []
#     if x in L:
#         for i, e in enumerate(L):
#             if e == x:
#                 idx.append(i)
#     else:
#         idx = [-1]

#     return idx


def solution(L, x):
    if x in L:
        return [i for i, y in enumerate(L) if y == x]
    else:
        return [-1]


def solution(L, x):
    idx = []
    left = 0
    while 1:
        if x in L:
            print(L)
            i = L.index(x) + left
            idx.append(i)
            left = i + 1
            L = L[left::]
        else:
            if len(idx) == 0:
                idx = [-1]
            break
    return idx


def solution(L, x):
    idx = []
    left = 0

    while left < len(L):
        try:
            i = L.index(x, left)
            idx.append(i)
            left = i + 1

        except ValueError:
            break

    if not idx:
        return [-1]

    return idx


print(solution(L, x))

"""
index(sol2) : 최악의 경우 list를 전체를 여러번 탐색해야 할 수 있음, O(n^2)
for(sol1) : O(n), list 길이에 비례
"""
