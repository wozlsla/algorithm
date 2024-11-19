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

    # 남은 요소를 한번에 추가
    res.extend(arr1[i:])
    res.extend(arr2[j:])

    return res


def sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    return merge(sort(arr[:mid]), sort(arr[mid:]))


arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
arr1 = [10, 5, 15]
arr2 = [4, 11, 2]
print(sort(arr1 + arr2))


# 처음 생각했던 방법 : 두 배열을 따로 정렬 후 병합
# 두 배열의 크기가 크게 차이 난다면 이게 더 낫다고 한다.. (왜??)
def sort_separately(arr1, arr2):

    sorted_arr1 = sort(arr1)
    sorted_arr2 = sort(arr2)

    return merge(sorted_arr1, sorted_arr2)


print(sort_separately(arr1, arr2))
