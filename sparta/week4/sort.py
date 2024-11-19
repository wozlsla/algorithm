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


# sparta
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


# https://youtu.be/9KBwdDEwal8?si=2vyMNjCcsV9VXUX0
def quicksort2(arr, left, right):
    if left < right:
        pos = partition(arr, left, right)
        quicksort(arr, left, pos - 1)
        quicksort(arr, pos + 1, right)


def partition(arr, left, right):
    i = left
    j = right
    pivot = arr[right]

    while i < j:

        # i 이동 - left의 idx가 right의 idx보다 작고, left의 값이 pivot의 값보다 작다면
        while i < right and arr[i] < pivot:
            i += 1

        # j 이동 - right의 idx가 left의 idx보다 크고, right의 값이 pivot보다 크거나 같으면
        while j > left and arr[j] >= pivot:
            j -= 1

        if i < j:  # swap
            arr[i], arr[j] = arr[j], arr[i]

    # i가 멈춘 위치에서, pivot보다 큰 값이면 pivot의 위치와 스왑 -> pivot을 위치 결정
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


arr = [22, 11, 88, 66, 55, 77, 33, 44]
arr = [4, 2, 8, 6, 1]
# quicksort2(arr, 0, len(arr) - 1)
# print(arr)


def merge(arr1, arr2):
    res = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    # 남은 거 합침
    for idx in range(i, len(arr1)):
        res.append(arr1[idx])
    for idx in range(j, len(arr2)):
        res.append(arr2[idx])

    return res


def mergesort(arr):
    if len(arr) <= 1:
        return arr

    # 쪼갬
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    return merge(mergesort(left), mergesort(right))


def heapsort(arr):
    from week2.structures import BinaryMinHeap

    res = []
    heap = BinaryMinHeap()

    for i in arr:
        heap.insert(i)

    for _ in range(len(arr)):
        res.append(heap.extract())

    return res
    # return [heap.extract() for _ in range(len(arr))]
