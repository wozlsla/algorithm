def bubblesort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selectionsort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        if min != i:
            arr[min], arr[i] = arr[i], arr[min]
    return arr


def insertionsort(arr):
    for i in range(len(arr) - 1):
        for j in reversed(range(1, i + 2)):  # 뒤에서부터
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break
    return arr


def quicksort(arr, st, end):
    """
    i: pivot보다 작은 요소들의 집합의 `경계`를 구하기 위함
      - pivot보다 작거나 같은 값들
      - 1회 순회 후 i+1 에 pivot이 위치하게 됨
    j: pivot과 배열 요소들의 값을 비교하기위해 이동하는 값
    """
    if st > end:
        return

    pivot = arr[end]
    i = st - 1
    for j in range(st, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]  # pivot <-> i

    quicksort(arr, st, i)  # i+1 : pivot
    quicksort(arr, i + 2, end)

    return arr
