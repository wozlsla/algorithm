def sort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min][1] > arr[j][1]:
                min = j
        if min != i:
            arr[min], arr[i] = arr[i], arr[min]
    return arr


def table(times):
    sort(times)

    cnt = 1  # 첫 번째 작업은 항상 선택
    end = times[0][1]

    for i in range(1, len(times)):
        if end <= times[i][0]:
            cnt += 1
            end = times[i][1]

    return cnt


times = [(0, 6), (1, 4), (3, 5), (3, 8), (5, 7), (8, 9)]
times = [(1, 3), (2, 4), (5, 8), (6, 10), (8, 11), (10, 12)]

print(table(times))
