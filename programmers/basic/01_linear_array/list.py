L = [20, 37, 58, 72, 91]


def solutions(L, x):
    if L[0] > x:
        L.insert(0, x)
        return L

    if L[-1] < x:
        # L.append(x)
        L.insert(len(L), x)
        return L

    for i in range(len(L)):
        if L[i] > x:
            L.insert(i, x)
            return L


def solution(L, x):

    if L[-1] < x:
        L.append(x)
        return L

    for idx, i in enumerate(L):
        print("for loop")
        if i > x:
            L.insert(idx, x)
            break

    return L


print(solution(L, 92))
