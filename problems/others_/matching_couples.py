import math


def match(arr):
    boys, girls, n = arr
    pair_size = n // 2  # 각 필요한 인원 수 : 짝 지으려는 사람 수 // 2

    # 필요한 남자 수와 여자 수가 1명일 경우
    if pair_size == 1:
        return boys * girls
    else:
        # 각 조합
        boy_comb = math.comb(boys, pair_size)
        girl_comb = math.comb(girls, pair_size)

        # 팩토리얼 : 남/녀 짝짓는 경우의 수 (순서 고려)
        return boy_comb * girl_comb * math.factorial(pair_size)


# 예시 테스트
print(match([5, 3, 2]))  # 출력: 15
print(match([10, 5, 4]))  # 출력: 900
print(match([5, 5, 4]))  # 출력: 200
print(match([2, 2, 2]))  # 출력: 4
print(match([10, 10, 6]))  # 출력: 86400
print(match([15, 10, 6]))  # 출력: 327600
