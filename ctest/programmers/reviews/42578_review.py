# https://school.programmers.co.kr/learn/courses/30/lessons/42578 - 의상


def solution(clothes: list[list[str, str]]) -> int:
    items = {}
    cnt = 1

    for val, key in clothes:
        if key not in items:
            items[key] = []  # 초기화
            # items[key] = val 만약 있으면 2번 추가하게 되니까
        items[key].append(val)

    for i in items.keys():
        cnt *= len(items[i]) + 1

    return cnt - 1


clothes = [
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"],
]

clothes = [
    ["crow_mask", "face"],
    ["blue_sunglasses", "face"],
    ["smoky_makeup", "face"],
]

print(solution(clothes))
