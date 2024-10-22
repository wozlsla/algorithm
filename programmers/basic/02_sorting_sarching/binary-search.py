def solution(L, x):
    left, right = 0, len(L) - 1

    while left <= right:
        mid = (left + right) // 2

        if x == L[mid]:
            return mid
        elif x < L[mid]:
            right = mid - 1
        elif x > L[mid]:
            left = mid + 1

    return -1
