# https://school.programmers.co.kr/learn/courses/30/lessons/42576 - 완주하지 못한 선수


def solution(participant, completion):
    dic = {}

    for e in participant:
        dic[e] = dic.get(e, 0) + 1

    for c in completion:
        if dic[c] == 1:
            dic.pop(c)
        else:
            dic[c] -= 1

    return next(iter(dic))


# print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
