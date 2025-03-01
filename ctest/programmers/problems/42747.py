# https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=python3 - H-Index


def solution(citations: list[int]) -> int:

    citations.sort(reverse=True)
    h_index = 0

    for i, citation_cnt in enumerate(citations):
        cnt = i + 1

        if citation_cnt >= cnt:
            h_index = cnt
        else:
            break

    return h_index


arr = [3, 0, 6, 1, 5]
print(solution(arr))


# 다른 사람 풀이
def solution(citations):
    citations = sorted(citations)
    n = len(citations)

    for i in range(n):
        if citations[i] >= n - i:
            return n - i
    return 0


def solution(citations):
    citations.sort(reverse=True)

    answer = max(map(min, enumerate(citations, start=1)))  # 순위를 1부터 시작하게 설정
    # 순위와 인용 횟수 중 작은 값을 선택하여 최대값을 찾음
    # citations = [6, 5, 3, 1, 0]일 때, 결과는 [(1, 6), (2, 5), (3, 3), (4, 1), (5, 0)]
    # 각 쌍에서 작은 값은 [1, 2, 3, 1, 0]이고, 최대값은 3
    return answer
