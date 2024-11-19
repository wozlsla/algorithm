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
